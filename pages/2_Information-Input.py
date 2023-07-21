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
if file != None:
    podcastManager.loadPodcastPlan(StringIO(file.getvalue().decode("utf-8")).read())
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
st.write("Geben Sie hier das Hauptthema Ihres Podcasts an. Falls Sie unsicher sind, lassen Sie das Feld leer - das KI-Tool hilft Ihnen im nächsten Schritt dabei, ein passendes Thema zu generieren.")
if podcastManager.topic_key in st.session_state:
    st.session_state.topic_gen = podcastManager.getStateVariableByKey(podcastManager.topic_key)
topic = st.text_area("   ", key="topic_gen")
st.divider()
st.subheader("Kernbotschaft")
st.write("Definieren Sie hier die zentrale Aussage oder Botschaft, die Ihre Hörer aus dem Podcast mitnehmen sollen. Diese wird als Leitlinie für die Generierung der Podcast-Struktur genutzt.")
message = st.text_area("    ")
st.divider()
st.subheader("Fragen")
st.write("Geben Sie hier Fragen an, die Sie während des Podcasts stellen möchten. Diese werden in die Podcast-Struktur aufgenommen.")
questions = st.text_area("     ")
st.divider()
st.subheader("SEO-Keywords")
st.write("Fügen Sie hier die SEO-Keywords ein, die zu Ihrem Podcast-Thema passen. Diese werden bei der Erstellung des Podcast-Plans berücksichtigt, um die Auffindbarkeit Ihres Podcasts zu optimieren.")
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