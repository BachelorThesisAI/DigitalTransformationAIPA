#import api_key
#import key
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
st.subheader("Bestehenden Podcast-Plan hochladen")
st.write("Sollten Sie bereits einen Podcast-Plan haben, können Sie diesen hier hochladen. Der hochgeladene Plan wird verwendet, um Ihre früheren Informationen wiederherzustellen und den Planungsprozess zu beschleunigen.")
file = st.file_uploader(label="Podcast-Plan hochladen")

if st.button("Podcast laden"):
    if file != None:
        podcastManager.loadPodcastPlan(StringIO(file.getvalue().decode("utf-8")).read())
        podcastManager.setPodcastStructure()
        st.success("Daten geladen, Sie können zur Podcast-Durchführung übergehen!")
st.divider()
st.subheader("Informationen zum Gast und seinem Hintergrund")
st.write(guest_backgroundinfo_explanation)
if podcastManager.bg_info_key in st.session_state:
    st.session_state.bg_info_gen = podcastManager.getStateVariableByKey(podcastManager.bg_info_key)
bg_info = st.text_area("", key="bg_info_gen")
st.divider()
st.subheader("Zielgruppe")
st.write("Angestrebte Zielgruppe: An wen richten Sie diesen Podcast hauptsächlich? Sollen es Fachleute aus einer bestimmten Branche sein, ein breiteres Publikum oder eine spezifische demografische Gruppe? Ihre Zielgruppe kann die Art der Fragen und die Diskussionstiefe beeinflussen.")
if podcastManager.target_audience_key in st.session_state:
    st.session_state.target_audience_gen = podcastManager.getStateVariableByKey(podcastManager.target_audience_key)
target_audience = st.text_area(" ", key="target_audience_gen")
st.divider()
st.subheader("Thema (optional)")
st.write("Geben Sie hier das Hauptthema Ihres Podcasts an. Falls Sie unsicher sind, lassen Sie das Feld leer - das KI-Tool hilft Ihnen im nächsten Schritt dabei, ein passendes Thema zu generieren.")
if podcastManager.topic_key in st.session_state:
    st.session_state.topic_gen = podcastManager.getStateVariableByKey(podcastManager.topic_key)
topic = st.text_area("   ", key="topic_gen")
st.divider()
st.subheader("Kernbotschaft")
st.write("Definieren Sie hier die zentrale Aussage oder Botschaft, die Ihre Hörer aus dem Podcast mitnehmen sollen. Diese wird als Leitlinie für die Generierung der Podcast-Struktur genutzt.")
if podcastManager.message_key in st.session_state:
    st.session_state.message_gen = podcastManager.getStateVariableByKey(podcastManager.message_key)
message = st.text_area("    ", key="message_gen")
st.divider()
st.subheader("Fragen")
st.write("Geben Sie hier Fragen an, die Sie während des Podcasts stellen möchten. Diese werden in die Podcast-Struktur aufgenommen.")
if podcastManager.questions_key in st.session_state:
    st.session_state.questios_gen = podcastManager.getStateVariableByKey(podcastManager.questions_key)
questions = st.text_area("     ", key="questions_gen")
st.divider()
st.subheader("SEO-Keywords")
st.write("Fügen Sie hier die SEO-Keywords ein, die zu Ihrem Podcast-Thema passen. Diese werden bei der Erstellung des Podcast-Plans berücksichtigt, um die Auffindbarkeit Ihres Podcasts zu optimieren.")
if podcastManager.keywords_key in st.session_state:
    st.session_state.keywords_gen = podcastManager.getStateVariableByKey(podcastManager.keywords_key)
keywords = st.text_area("      ", key="keywords_gen")
st.divider()
st.subheader("Format")
st.write("""Definieren Sie hier das Format Ihres Podcast. Schreiben Sie dazu nacheinander die einzelnen Abschnitte hin, die der Podcast enthalten und für die dann die Fragen erstellt werden sollen.  
  
**Hinweis**: Einleitung und Schlussteil sind bereits immer enthalten und müssen nicht erwähnt werden""")
if podcastManager.format_key in st.session_state:
    st.session_state.format_gen = podcastManager.getStateVariableByKey(podcastManager.format_key)
format = st.text_area("      ", key="format_gen")

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
    podcastManager.setStateVariableByKey(
        "format",
        format
    )