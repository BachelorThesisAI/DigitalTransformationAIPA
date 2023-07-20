import streamlit as st
from components.podcastmanager import PodcastManager
from components.llmservice import LLMService

# init components
podcastManager = PodcastManager()
llmService = LLMService()

selection = None

def setSelection():
    podcastManager.setStateVariableByKey(podcastManager.topic_gen_key, selection, update_widget=True)
    podcastManager.setStateVariableByKey(podcastManager.topic_key, selection)

st.title("Themen-Generator")
st.write("")
if podcastManager.isPodcastInfoSet():
    st.write("themen-generator explanation")
    
    if st.button("Generiere Themen"):
        with st.spinner("Generiere Themen ..."):
            st.session_state[podcastManager.podcast_topics_selection_key]= llmService.generatePodcastTopics(
                bg_info=podcastManager.getStateVariableByKey(podcastManager.bg_info_key),
                target_audience=podcastManager.getStateVariableByKey(podcastManager.target_audience_key),
                questions=podcastManager.getStateVariableByKey(podcastManager.questions_key),
                keywords=podcastManager.getStateVariableByKey(podcastManager.keywords_key),
                message=podcastManager.getStateVariableByKey(podcastManager.message_key)
            )
    
    if podcastManager.podcast_topics_selection_key in st.session_state:
        if st.session_state[podcastManager.podcast_topics_selection_key] == None:
            st.error("Fehler beim Generieren der Themen, versuche erneut")
        else:
            selection = st.radio(
                label="Wähle Thema aus",
                options=st.session_state[podcastManager.podcast_topics_selection_key]
            )

            st.button("Thema übernehmen", on_click=setSelection)

    
else:
    st.error("Bitte geben Sie zunächst Informationen zum Podcast ein.")
