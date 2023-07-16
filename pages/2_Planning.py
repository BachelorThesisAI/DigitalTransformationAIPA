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
    st.write(file_upload_explanation)
    st.divider()
    files = st.file_uploader(file_upload_prompt, accept_multiple_files=True)
    if st.form_submit_button(generate_button_text):
        with st.spinner(spinner_db_text):
            if files is None:
                files = []
            vectordb.createDBfromPDFs(
                files = [
                    BytesIO(uploaded_file.getvalue())
                            for uploaded_file in files
                ]
            )
        st.success(success_db_text)
        with st.spinner(spinner_generate_queries_text) as spin:
            queries = llmService.generateContextQueries(
                vectordb.readPDFnames,
                requirements,
                bg_info
            )
        if queries == None:
            st.error(error_generate_queries_text)
        else:
            st.success(success_generate_queries_text)
            with st.expander(expander_queries_text):
                st.write(queries)
            
            contexts_and_sources = []
            with st.spinner(spinner_retrieve_context_text):
                contexts_and_sources = llmService.retrieveContextualInformation(
                    retriever = vectordb.retriever,
                    queries = queries
                )
            if len(contexts_and_sources) == 0:
                st.error(error_retrieve_context_text)
            else:
                st.success(success_retrieve_context_text)
                for cas in contexts_and_sources:
                    with st.expander(cas[0]):
                        st.write(cas[1])
                response = None
                with st.spinner(spinner_generate_podcast_structure):
                    response = llmService.generatePodcastStructure(
                        background_information = bg_info,
                        requirements = requirements,
                        research = [cas[0] for cas in contexts_and_sources]
                    )
                st.success(success_generate_podcast_structure)
                st.write(response)
