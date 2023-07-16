import api_key
import key
import streamlit as st
from constants import *
from prompts import *
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain, RetrievalQAWithSourcesChain
from langchain.prompts import PromptTemplate
from components.llmservice import LLMService
from components.podcastmanager import PodcastManager
from components.vectordb import VectorDatabaseService
from io import StringIO


llmService = LLMService()
podcastManager = PodcastManager()
vectordb = VectorDatabaseService()

# Podcast progress sidebar
with st.sidebar:
    st.title("Podcast-Phasen")
    add_radio = st.radio(
        " ",
        podcastManager.getSections(),
        disabled=True,
    )

unmentionedTemplate = PromptTemplate(
    input_variables = ["requirements"],
    template = podcast_structure_planning_template
)

reg_llm = OpenAI(temperature=0.9) # type: ignore

reg_chain = LLMChain(
    llm = reg_llm,
    prompt = unmentionedTemplate,
    verbose = True
)

st.title("Digital Transformation AI Podcast Assistant")

#prompt = st.text_input(label = "Eingabe")


if podcastManager.current_section == 0:
    st.write(k_podcast_planning_general_explanation)
    st.write(" ")
    st.write(" ")
    with st.form("planning_form"):
        st.write(k_podcast_planning_guest_backgroundinfo_explanation)
        bg_info = st.text_area("Informationen über den Gast und/oder ein Unternehmen")
        st.divider()
        st.write(k_podcast_planning_requirements_explanation)
        requirements = st.text_area("Anforderungen an Podcast-Struktur")
        st.divider()
        st.write(k_podcast_planning_file_upload_explanation)
        st.divider()
        files = st.file_uploader("PDF Dateien", accept_multiple_files=True)
        if st.form_submit_button("Podcast-Struktur generieren"):
            print(files)
            with st.spinner('Generating response...'):
                if files != None:
                    vectordb.createDBfromPDFs(
                        files = [StringIO(uploaded_file.getvalue().decode("utf-8"))
                                 for uploaded_file in files]
                    )
                    
                # response = rqa(prompt, return_only_outputs=True)
                # answer = response['result']
                # response = seq(prompt, return_only_outputs=True)
                #response = reg_chain.run(prompt)
                #st.write(response)
    st.write("After")

else:

    if st.button('Absenden'):
        if prompt:
            with st.spinner('Generating response...'):
                # response = rqa(prompt, return_only_outputs=True)
                # answer = response['result']
                # response = seq(prompt, return_only_outputs=True)
                response = reg_chain.run(prompt)
                
                st.write(response)
    else:
        st.warning('Please enter your prompt')

    if st.button(podcastManager.getSection()):
        st.write("XXX")