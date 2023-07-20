import streamlit as st
from typing import List

class PodcastManager:
    def __init__(self):
        self.CURRENT_SECTION_KEY = "CURRENT_SECTION"
        self.SET_PODCAST_KEY = "SET_PODCAST"
        self.podcast_structure_key = "podcast_structure"

        self.message_key = "message"
        self.target_audience_key = "target_audience"
        self.topic_key = "topic"
        self.topic_gen_key = "topic_gen"
        self.bg_info_key = "bg_info"
        self.questions_key = "questions"
        self.keywords_key = "keywords"

        self.podcast_topics_selection_key = "topicselection"
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
    
    def getStateVariableByKey(self, key) -> str:
        try:
            state = st.session_state[key]
            return state if state != "" else "UNDEFINED"
        except:
            return "UNDEFINED"
    
    def setStateVariableByKey(self, key, value, update_widget = False):
        st.session_state[key] = value
        if update_widget:
            try:
                st.session_state.key = value
            except:
                pass
    
    def buildPodcastRequirementsString(self) -> str:
        return f"""
        Zielgruppe:
        {self.getStateVariableByKey(self.target_audience_key)}

        Thema:
        {self.getStateVariableByKey(self.topic_key)}

        Fragen:
        {self.getStateVariableByKey(self.questions_key)}

        SEO-Keywords:
        {self.getStateVariableByKey(self.keywords_key)}

        Kernbotschaft:
        {self.getStateVariableByKey(self.message_key)}
        """

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

    def isPodcastInfoSet(self) -> bool:
        if self.target_audience_key in st.session_state:
            return True
        else:
            return False
    
    def getSectionByIndex(self, index: int):
        return [key for key in st.session_state[self.podcast_structure_key].keys()][index+1]
    
    def nextSection(self):
        if st.session_state[self.CURRENT_SECTION_KEY] < len(st.session_state[self.podcast_structure_key].keys())-1:
            st.session_state[self.CURRENT_SECTION_KEY] = st.session_state[self.CURRENT_SECTION_KEY]+1