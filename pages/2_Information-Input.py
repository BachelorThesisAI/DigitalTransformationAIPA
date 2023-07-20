#import api_key
import key
import streamlit as st
from constants import *
from components.llmservice import LLMService
from components.podcastmanager import PodcastManager
from components.vectordb import VectorDatabaseService
from io import StringIO, BytesIO

# initiate podcast manager component
podcastManager = PodcastManager()
vectordb = VectorDatabaseService()

st.title(title_string)
st.write(general_explanation)
st.divider()
st.subheader("Informationen zum Gast und seinem Hintergrund")
st.write(guest_backgroundinfo_explanation)
bg_info = st.text_area("")
st.divider()
st.subheader("Zielgruppe")
st.write("Angestrebte Zielgruppe: An wen richten Sie diesen Podcast hauptsächlich? Sollen es Fachleute aus einer bestimmten Branche sein, ein breiteres Publikum oder eine spezifische demografische Gruppe? Ihre Zielgruppe kann die Art der Fragen und die Diskussionstiefe beeinflussen.")
target_audience = st.text_area(" ")
st.divider()
st.subheader("Thema (optional)")
st.write("Beschreibe kurz und prägnant dein Thema oder lasse das Feld aus und nutze den **Themen-Generator**")
if podcastManager.topic_key in st.session_state:
    st.session_state.topic_gen = podcastManager.getStateVariableByKey(podcastManager.topic_key)
topic = st.text_area("   ", key="topic_gen")
st.divider()
st.subheader("Kernbotschaft")
st.write("Kernbotschaft explanation")
message = st.text_area("    ")
st.divider()
st.subheader("Fragen")
st.write("Fragen explanation")
questions = st.text_area("     ")
st.divider()
st.subheader("SEO-Keywords")
st.write("SEO-Keywords explanation")
keywords = st.text_area("      ")

st.divider()

if st.button(generate_button_text):
    podcastManager.setStateVariableByKey(
        podcastManager.bg_info_key,
        bg_info
    )
    podcastManager.setStateVariableByKey(
        podcastManager.target_audience_key,
        target_audience
    )
    podcastManager.setStateVariableByKey(
        podcastManager.topic_key,
        topic
    )
    podcastManager.setStateVariableByKey(
        podcastManager.message_key,
        message
    )
    podcastManager.setStateVariableByKey(
        podcastManager.questions_key,
        questions
    )
    podcastManager.setStateVariableByKey(
        podcastManager.keywords_key,
        keywords
    )