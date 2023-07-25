import streamlit as st
from typing import List
from json import loads, dumps
from langchain.schema.messages import HumanMessage, AIMessage

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
        self.format_key = "format"
        self.podcast_summary = "podcast_summary"

        self.current_content_key = "current_content"
        self.current_content_index_key = "current_content_index"

        self.started_podcast_key = "started"
        self.podcast_topics_selection_key = "topicselection"
        self.chat_history_key = "chat_history"
        self.guest_response_key = "guest_response"
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
        return [key for key in st.session_state[self.podcast_structure_key].keys()][index]
    
    def getCurrentContentIndex(self):
        return st.session_state[self.current_content_index_key]
    
    def nextSection(self):
        st.session_state[self.current_content_index_key] = 0
        st.session_state[self.CURRENT_SECTION_KEY] = st.session_state[self.CURRENT_SECTION_KEY]+1
        st.session_state[self.current_content_key] = self.getContentForCurrentSection()[0]
        
    def hasNextSection(self):
        if st.session_state[self.CURRENT_SECTION_KEY] < len(st.session_state[self.podcast_structure_key].keys())-1:
            return True
        return False

    def nextContent(self):
        nextIndex = st.session_state[self.current_content_index_key] + 1
        st.session_state[self.current_content_index_key] = nextIndex
        st.session_state[self.current_content_key] = self.getContentForCurrentSection()[nextIndex]

    def getNextContent(self):
        nextIndex = st.session_state[self.current_content_index_key] + 1
        st.session_state[self.current_content_key] = self.getContentForCurrentSection()[nextIndex]

    def hasNextContent(self):
        try:
            self.getContentForCurrentSection()[self.getCurrentContentIndex() + 1]
            return True
        except:
            return False
    
    def buildPodcastPlan(self) -> str:
        podcastPlan = [
            self.getStateVariableByKey(self.topic_key),
            self.getStateVariableByKey(self.bg_info_key),
            self.getStateVariableByKey(self.target_audience_key),
            self.getStateVariableByKey(self.questions_key),
            self.getStateVariableByKey(self.keywords_key),
            self.getStateVariableByKey(self.message_key),
            self.getStateVariableByKey(self.podcast_structure_key),
        ]
        return dumps(podcastPlan, ensure_ascii=False, indent=4)
    
    def loadPodcastPlan(self, podcastPlan: str):
        keys = [self.topic_key, self.bg_info_key, self.target_audience_key, self.questions_key, self.keywords_key, self.message_key, self.podcast_structure_key]
        planList = loads(podcastPlan)

        for i, key in enumerate(keys):
            self.setStateVariableByKey(key, value=planList[i])
    
    def getContentForCurrentSection(self):
        return st.session_state[self.podcast_structure_key][self.getSectionByIndex(self.getCurrentSection())]
    
    def startPodcast(self):
        st.session_state[self.started_podcast_key] = True
        st.session_state[self.current_content_index_key] = 0
        st.session_state[self.current_content_key] = self.getContentForCurrentSection()[0]
    
    def isPodcastStarted(self):
        try:
            st.session_state[self.started_podcast_key]
            return True
        except:
            return False
    
    def finishPodcast(self):
        st.session_state["podcast_finished"] = True

    def isPodcastFinished(self):
        try:
            return st.session_state["podcast_finished"]
        except:
            return False
    
    def setCurrentContent(self, content):
        st.session_state[self.current_content_key] = content
    
    def getChatHistory(self):
        return st.session_state[self.chat_history_key]
    
    def getChatHistoryAsString(self):
        chat_history = self.getChatHistory()
        new_string = ""
        for msg in chat_history:
            if isinstance(msg, HumanMessage):
                new_string += f"\nGast: {msg.content}\n"
            elif isinstance(msg, AIMessage):
                new_string += f"\nPodcast-Host: {msg.content}\n"
        return new_string
    
    def setGuestResponse(self, response):
        st.session_state[self.guest_response_key] = response
    
    def getGuestResponse(self):
        return st.session_state[self.guest_response_key]
    
    def addToChatHistory(self):
        history = []
        try:
            history = self.getChatHistory()
        except:
            pass
        history.append(
            AIMessage(content=self.getCurrentContent())
        )
        history.append(
            HumanMessage(content=self.getGuestResponse())
        )
        st.session_state[self.chat_history_key] = history
    
    def getCurrentContent(self):
        return st.session_state[self.current_content_key]
    