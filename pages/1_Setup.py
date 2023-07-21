import streamlit as st
import streamlit as st
from components.llmservice import LLMService

st.set_page_config(
    page_title= "ChatGPT-Setup",
)

llmService = LLMService()

st.title("API-Schlüssel-Seite")

st.write("In diesem Bereich geben Sie Ihren API-Schlüssel für die KI-Funktionen ein. Dieser Schlüssel ermöglicht die Kommunikation zwischen unserem Tool und der KI, die zum Generieren von Themen, Erstellen von Fragen und Durchführen weiterer Funktionen genutzt wird. Stellen Sie sicher, dass Sie einen gültigen Schlüssel besitzen und diesen korrekt eingeben, um die volle Funktionalität des Tools nutzen zu können.")
API_KEY = st.text_input("API-Schlüssel: ")
if st.button('Absenden'):
    isSet = llmService.setAPIKey(API_KEY)
    print(f"API KEY IS {isSet}")
    if not isSet:
        st.info("Der API-Schlüssel ist falsch")
    else:
        st.info("Der API-Schlüssel ist korrekt")