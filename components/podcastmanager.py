import streamlit as st
from typing import List

class PodcastManager:
    def __init__(self):
        self.CURRENT_SECTION_KEY = "CURRENT_SECTION"
        self.SECTIONS_KEY = "SECTIONS"

        self.BG_INFO_KEY = "bg"
        self.REQUIREMENTS_KEY = "requirements"
        
    
    def init(self):
        try:
            st.session_state[self.CURRENT_SECTION_KEY]
        except:
            st.session_state[self.CURRENT_SECTION_KEY] = 0
        try:
            st.session_state[self.SECTIONS_KEY]
        except:
            st.session_state[self.SECTIONS_KEY] = []

    def getCurrentSection(self) -> int:
        return st.session_state[self.CURRENT_SECTION_KEY]
    
    def setSections(self, sections: List[str]):
        return st.session_state[self.SECTIONS_KEY]
    
    def getSections(self) -> List[str]:
        return st.session_state[self.SECTIONS_KEY]