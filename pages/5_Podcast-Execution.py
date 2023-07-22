import streamlit as st
from components.podcastmanager import PodcastManager
from components.llmservice import LLMService
#import key

llmService = LLMService()
podcastManager = PodcastManager()

def onSend():
    with st.spinner("Generiere nächste Frage"):
        
        content = llmService.generateContentForCurrentSection()
        if content:
            podcastManager.setCurrentContent(content)
        elif content == None and podcastManager.hasNextContent():
            podcastManager.nextContent()
        else:
            podcastManager.setCurrentContent("Bitte zum nächsten Abschnitt fortfahren")


st.title("Podcast-Durchführung")
st.write("Willkommen auf der Podcast-Durchführungsseite. Hier können Sie Ihren vorbereiteten Podcast live führen. Basierend auf Ihrer vorher erstellten Struktur, finden Sie hier die generierten Fragen und Inhalte. Sie können Antworten Ihres Gastes mithilfe einer Transkriptionssoftware eingeben und unser Tool wird darauf basierend weitere Folgefragen generieren. Am Ende Ihrer Session können Sie eine Zusammenfassung Ihres Podcasts erstellen, um Ihren Zuhörern einen klaren und zusammenfassenden Überblick zu bieten.")
if not llmService.isAPIKeySet():
    st.error("Bitte zunächst API-Schlüssel hinzufügen.")
elif not podcastManager.isPodcastStructureSet():
    st.error("Bitte nutzen Sie zunächst den Podcast-Planer")
else:
    if not podcastManager.isPodcastStarted():
        st.success("Podcast ist bereit zum Durchführen!")
    with st.sidebar:
        st.radio(
            label = "Podcast-Struktur",
            options = podcastManager.getSectionNames(),
            disabled=True,
            index=podcastManager.getCurrentSection()
        )
        if podcastManager.isPodcastStarted():
            st.divider()
            st.radio(
                label="Jetziger Abschnitt",
                options=podcastManager.getContentForCurrentSection(),
                index=podcastManager.getCurrentContentIndex()
            )

    # WHEN PODCAST IS RUNNING
    if podcastManager.isPodcastStarted():
        
        with st.chat_message("Podcast-Assistant"):
            st.write(podcastManager.getCurrentContent())

        podcastManager.setGuestResponse(st.text_area("GastAntwort"))

        col1, col2 = st.columns(2)

        with col1:
            st.button("Senden", on_click=onSend)

        if podcastManager.hasNextContent():
            with col2:
                st.button("Überspringen", on_click=podcastManager.nextContent)
        
        st.divider()
        if podcastManager.hasNextSection():
            st.button(f"Weiter zu {podcastManager.getSectionByIndex(podcastManager.getCurrentSection()+1)}", on_click=podcastManager.nextSection)
        else:
            podcastManager.finishPodcast()
    
    # AFTER PODCAST IS FINISHED
    elif podcastManager.isPodcastFinished():
        with st.spinner("Erstelle Zusammenfassung"):
            llmService.generatePodcastSummary()
        if st.session_state["podcast_summary"]:
            st.success("Zusammenfassung erstellt")

    # BEFORE PODCAST STARTED
    else:
        st.button("Starte Podcast", on_click=podcastManager.startPodcast)