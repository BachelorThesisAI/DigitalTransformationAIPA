#import api_key
#import key
import streamlit as st
from constants import *
from components.llmservice import LLMService
from components.podcastmanager import PodcastManager
from components.vectordb import VectorDatabaseService
from io import StringIO, BytesIO

# initiate components
llmService = LLMService()
podcastManager = PodcastManager()
vectordb = VectorDatabaseService()

def renderListContent(contentList):
    contentString = ''
    for content in contentList:
        contentString += "- " + content + " \n"
    st.markdown(contentString)

st.title(title_string)
st.write(general_explanation)
st.write(" ")

if not llmService.isAPIKeySet():
    st.error("Bitte zunächst API-Schlüssel hinzufügen.")
elif podcastManager.bg_info_key not in st.session_state:
    st.error("Keine Informationen zum Podcast eingegeben. Bitte gehen Sie auf die Seite zur Informationseingabe und korrigieren dies.")
elif st.session_state[podcastManager.topic_key] == "UNDEFINED":
    st.error("Kein Thema zum Podcast angegeben. Bitte geben Sie es an oder nutzen Sie den Themengenerator")
else:
    st.divider()
    st.write(file_upload_explanation)

    files = st.file_uploader(file_upload_prompt, accept_multiple_files=True)
    if st.button("Dokumente verarbeiten"):
        with st.spinner(spinner_db_text):
            if files is None:
                files = []
            st.session_state[vectordb.SUMMARIES_KEY] = []
            vectordb.createDBfromPDFs(
                files = [
                    BytesIO(uploaded_file.getvalue())
                            for uploaded_file in files
                ]
            )
        
    if vectordb.SUMMARIES_KEY in st.session_state:
        if st.session_state[vectordb.SUMMARIES_KEY] != []:
            st.success(success_db_text)
            with st.expander("Zusammenfassungen der Dokumente"):
                for summary in st.session_state[vectordb.SUMMARIES_KEY]:
                    st.write(summary)
        else:
            st.error("Zusammenfassungen konnten nicht erstellt werden")

    st.divider()
    st.subheader("Generierung von Anfragen")
    st.write("Da die KI nicht alle Dokumente vollständig einlesen kann werden in diesem Schritt Anfragen generiert, um wichtige Informationen aus den Dokumenten herauszuholen. Die KI entscheidet dabei auf Grundlage der bisher eingegebenen Informationen und der Zusammenfassungen der hochgeladenen Dokumente, was sie für die Podcast-Planung alles wissen kann und soll. Bei jeder Änderung der abhängigen Eingaben sollten diese neu generiert werden")
    if st.button("Anfragen generieren"):
        with st.spinner(spinner_generate_queries_text) as spin:
            st.session_state[llmService.queries_key] = llmService.generateContextQueries(
                st.session_state[vectordb.SUMMARIES_KEY],
                podcastManager.buildPodcastRequirementsString(),
                st.session_state[podcastManager.bg_info_key]
            )
    if llmService.queries_key in st.session_state:
        if st.session_state[llmService.queries_key] == None:
            st.error(error_generate_queries_text)
        else:
            st.success(success_generate_queries_text)
            with st.expander(expander_queries_text):
                renderListContent(st.session_state[llmService.queries_key])

    st.divider()

    st.subheader("Datenbank-Recherche")
    st.write("Durch Klicken von 'Frage Dokumente ab' wird die Datenbank mit den im letzten Schritt generierten Anfragen abgefragt und Antworten generiert. Die Antworten auf jede Anfrage werden danach angezeigt, zusammen mit den zugehörigen Quellen für jede Antwort. Damit kannst du entscheiden, ob du diese so lassen oder Änderungen an Dokumenten und anderen Informationen vornehmen möchtest, bevor du zum nächsten Schritt übergehst.")
    if st.button("Frage Dokumente ab"):
        with st.spinner(spinner_retrieve_context_text):
            st.session_state[llmService.contexts_and_sources_key] = llmService.retrieveContextualInformation(
                retriever = st.session_state[vectordb.retriever_key],
                queries = st.session_state[llmService.queries_key]
            )
    if llmService.contexts_and_sources_key in st.session_state:
        if len(st.session_state[llmService.contexts_and_sources_key]) == 0:
            st.error(error_retrieve_context_text)
        else:
            st.success(success_retrieve_context_text)
            for cas in st.session_state[llmService.contexts_and_sources_key]:
                with st.expander(cas[0]):
                    st.write(cas[1])

    st.divider()
    st.subheader("Generierung des Podcast-Plans")
    st.write("In diesem letzten Schritt wird, basierend auf den Informationen aus der Informationseingabeseite sowie den Antworten aus der Datenbank der Podcast-Plan generiert. Nach der Generierung wird der Podcast-Plan als Liste von Abschnitten zusammen mit den dazugehörigen Fragen und Inhalten, darstellt, damit du ihn überprüfen kannst")
    if st.button("Generiere Podcast-Plan"):
        with st.spinner(spinner_generate_podcast_structure):
            st.session_state[llmService.podcast_structure_key] = llmService.generatePodcastStructure(
                background_information = podcastManager.getStateVariableByKey(podcastManager.bg_info_key),
                requirements = podcastManager.buildPodcastRequirementsString(),
                research = [cas[0] for cas in st.session_state[llmService.contexts_and_sources_key]]
            )
    if llmService.podcast_structure_key in st.session_state:
        if st.session_state[llmService.podcast_structure_key] != None and st.session_state[llmService.podcast_structure_key] != []:
            st.success(success_generate_podcast_structure)
            for key in st.session_state[llmService.podcast_structure_key].keys():
                with st.expander(key):
                    renderListContent(st.session_state[llmService.podcast_structure_key][key])
            st.write("")
            if st.button("Übernehmen", help="Damit wird der Podcast-Plan übernommen, sodass diese auf der Seite zur Podcast-Durchführung angezeigt wird."):
                podcastManager.setPodcastStructure()
            st.divider()
            st.write("Es wird empfohlen den Zustand in einer Datei zu sichern. Klicken Sie dafür auf 'Podcast-Plan herunterladen'. **Hinweis:** Es werden alle Informationen außer der Datenbank gesichert. Wenn also in der nächsten Sitzung der Podcast-Plan wiederhergestellt wird, müssen Dokumente nochmals hochgeladen und die Datenbank erstellt werden.")
            st.info("Wenn Sie die Seite verlassen oder neu laden, gehen alle Informationen verloren.")
            st.download_button("Podcast-Plan herunterladen", podcastManager.buildPodcastPlan(), file_name="podcastPlan.json")