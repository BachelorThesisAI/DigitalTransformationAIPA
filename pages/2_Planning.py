import api_key
import key
import streamlit as st
from constants import *
from prompts import *
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.prompts import PromptTemplate
from components.llmservice import LLMService
from components.podcastmanager import PodcastManager
from components.vectordb import VectorDatabaseService
from io import StringIO, BytesIO

# initiate components
llmService = LLMService()
podcastManager = PodcastManager()
vectordb = VectorDatabaseService()

st.title(title_string)
st.write(general_explanation)
st.write(" ")
st.write(" ")


with st.form("planning_form"):
    st.write(guest_backgroundinfo_explanation)
    bg_info = st.text_area(guest_backgroundinfo_prompt)
    st.divider()
    st.write(requirements_explanation)
    requirements = st.text_area(requirements_prompt)
    st.divider()
    if st.form_submit_button(generate_button_text):
        # files
        st.session_state[podcastManager.BG_INFO_KEY] = bg_info
        st.session_state[podcastManager.REQUIREMENTS_KEY] = requirements
        # bg_info
        # requirements
        pass

st.divider()
st.subheader("Dokumentenverarbeitung")
st.write(podcast_database_creation_explanation)
st.write("")
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
st.subheader("Anfragenerstellung")
st.write("Basierend auf in der Datenbank hinterlegten Dokumenten, Hintergrundinformationen und Anforderungen zum Podcast werden hier Anfragen generiert. Bei jeder Änderung der abhängigen Eingaben sollten diese neu generiert werden")
if st.button("Anfragen generieren"):
    with st.spinner(spinner_generate_queries_text) as spin:
        st.session_state[llmService.queries_key] = llmService.generateContextQueries(
            st.session_state[vectordb.SUMMARIES_KEY],
            st.session_state[podcastManager.REQUIREMENTS_KEY],
            st.session_state[podcastManager.BG_INFO_KEY]
        )
if llmService.queries_key in st.session_state:
    if st.session_state[llmService.queries_key] == None:
        st.error(error_generate_queries_text)
    else:
        st.success(success_generate_queries_text)
        with st.expander(expander_queries_text):
            st.write(st.session_state[llmService.queries_key])

st.divider()

st.subheader("Recherche")
st.write("Hier werden Abfragen an die Datenbank durchgeführt. Falls Sie neue Anfragen generieren, sollte dieser Schritt nochmal durchgeführt werden.")
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

if st.button("Generiere Podcast-Struktur"):
    with st.spinner(spinner_generate_podcast_structure):
        st.session_state[llmService.podcast_structure_key] = llmService.generatePodcastStructure(
            background_information = bg_info,
            requirements = requirements,
            research = [cas[0] for cas in st.session_state[llmService.contexts_and_sources_key]]
        )
if llmService.podcast_structure_key in st.session_state:
    if st.session_state[llmService.podcast_structure_key] != None:
        st.success(success_generate_podcast_structure)
        st.write(st.session_state[llmService.podcast_structure_key])