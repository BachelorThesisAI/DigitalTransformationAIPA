import api_key
import streamlit as st
from constants import *
from prompts import *
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.prompts import PromptTemplate

sections = [
    "Podcast-Struktur-Planung",
    "Podcast-Fragen-Planung"
]
current_section = 0

# Podcast progress sidebar
with st.sidebar:
    st.title("Podcast-Phasen")
    add_radio = st.radio(
        " ",
        sections,
        disabled=True,
    )

def getSection():
    return sections[current_section]


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


if current_section == 0:
    st.write(k_podcast_planning_general_explanation)
    st.write(" ")
    st.write(" ")
    with st.form("planning_form"):
        st.write(k_podcast_planning_guest_backgroundinfo_explanation)
        st.text_area("Informationen über den Gast und/oder ein Unternehmen")
        st.divider()
        st.write(k_podcast_planning_requirements_explanation)
        st.text_area("Anforderungen an Podcast-Struktur")
        st.divider()
        st.write(k_podcast_planning_file_upload_explanation)
        st.divider()
        st.file_uploader("PDF Dateien")
        if st.form_submit_button("Podcast-Struktur generieren"):
            with st.spinner('Generating response...'):
                # response = rqa(prompt, return_only_outputs=True)
                # answer = response['result']
                # response = seq(prompt, return_only_outputs=True)
                response = reg_chain.run(prompt)
                st.write(response)
                if st.button('Übernehmen'):
                    if prompt:
                        with st.spinner('Generating response...'):
                            st.write("XX")



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

    if st.button(getSection()):
        st.write("XXX")