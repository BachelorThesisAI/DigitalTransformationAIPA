import streamlit as st
from components.podcastmanager import PodcastManager
from components.llmservice import LLMService
import key

llmService = LLMService()
podcastManager = PodcastManager()

st.title("Podcast-Durchführung")

if podcastManager.isPodcastStructureSet():
    st.success("Podcast ist bereit zum Durchführen!")
    with st.sidebar:
        st.radio(
            label = "Podcast-Struktur",
            options = podcastManager.getSectionNames(),
            disabled=True,
            index=podcastManager.getCurrentSection()
        )
    if st.button(f"Weiter zu {podcastManager.getSectionByIndex(podcastManager.getCurrentSection())}"):
        podcastManager.nextSection()
    
else:
    st.subheader("Bitte nutzen Sie zunächst den Podcast-Planer")