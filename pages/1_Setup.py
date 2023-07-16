import streamlit as st
import streamlit as st
from components.llmservice import LLMService

st.set_page_config(
    page_title= "ChatGPT-Setup",
)

llmService = LLMService()

st.title("API-Schlüssel-Seite")

st.write("Bitte fügen Sie Ihren ChatGPT-API-Schlüssel ein")
API_KEY = st.text_input("API-Schlüssel: ")
if st.button('Absenden'):
    isSet = llmService.setAPIKey(API_KEY)
    print(f"API KEY IS {isSet}")
    if not isSet:
        st.info("Der API-Schlüssel ist falsch")
    else:
        st.info("Der API-Schlüssel ist korrekt")