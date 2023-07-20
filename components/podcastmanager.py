import streamlit as st
from typing import List

class PodcastManager:
    def __init__(self):
        self.CURRENT_SECTION_KEY = "CURRENT_SECTION"
        self.SET_PODCAST_KEY = "SET_PODCAST"
        self.podcast_structure_key = "podcast_structure"

        self.BG_INFO_KEY = "bg"
        self.REQUIREMENTS_KEY = "requirements"
        self.init()

    
    def init(self):
        try:
            st.session_state[self.CURRENT_SECTION_KEY]
        except:
            st.session_state[self.CURRENT_SECTION_KEY] = 0
        try:
            st.session_state[self.podcast_structure_key]
        except:
            st.session_state[self.podcast_structure_key] = []

    def getCurrentSection(self) -> int:
        return st.session_state[self.CURRENT_SECTION_KEY]
    
    def setPodcastStructure(self):
        st.session_state[self.SET_PODCAST_KEY] = True
    
    def getSectionNames(self) -> List[str]:
        return [x for x in st.session_state[self.podcast_structure_key].keys()]
    
    def isPodcastStructureSet(self) -> bool:
        if self.SET_PODCAST_KEY in st.session_state:
            return True
        else:
            return False
    
    def getSectionByIndex(self, index: int):
        return [key for key in st.session_state[self.podcast_structure_key].keys()][index+1]
    
    def nextSection(self):
        if st.session_state[self.CURRENT_SECTION_KEY] < len(st.session_state[self.podcast_structure_key].keys())-1:
            st.session_state[self.CURRENT_SECTION_KEY] = st.session_state[self.CURRENT_SECTION_KEY]+1