from os import environ
from langchain.llms import OpenAI
from streamlit import session_state
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain, RetrievalQA
from langchain.prompts import  PromptTemplate
import key
from prompts import *
from components.podcastmanager import PodcastManager
from typing import List, Tuple
#from components.vectordb import VectorDatabaseService

class LLMService:

    def __init__(self) -> None:
        self.OPENAI_API_KEY = "OPENAI_API_KEY"
        self.init()

        # context query input variable keys
        self.summary_list_key = "summaries"
        self.requirements_key = "requirements"
        self.background_information_key = "background_information"
        # podcast structure input variable keys
        self.research_key = "research"
        self.json_example_key = "json_example"
    
    def init(self):
        try:
            session_state[self.OPENAI_API_KEY] = environ[self.OPENAI_API_KEY]
        except:
            pass

    def setAPIKey(self, API_KEY):
        environ[self.OPENAI_API_KEY] = API_KEY
        try:
            llm = OpenAI(temperature=0.9) # type: ignore
            llm("")
            print("We did it here")
            session_state[self.OPENAI_API_KEY] = API_KEY
            return True
        except Exception as e:
            return False
    
    def isAPIKeySet(self):
        try:
            key = session_state[self.OPENAI_API_KEY]
            if key == "":
                return False
            return True
        except:
            return False
    
    def createPodcastStructure(self, retriever):
        # init llm
        llm = self.buildLLM(0.9)
        # create context queries for vector database
        contextQueryChain = LLMChain(
            prompt = PromptTemplate(
                input_variables = [self.summary_list_key, self.requirements_key, self.background_information_key],
                template = podcast_structure_planning_template,
            ),
            llm=llm
        )

        # retrieven von kontext
        # erstellen der struktur
    
    def buildLLM(self, temperature: float):
        return OpenAI(temperature = temperature) # type: ignore
    
    def generateContextQueries(self, summaries_list: List[str], requirements: str, background_information: str):
        # init llm
        llm = self.buildLLM(0.9)
        # create context queries for vector database
        contextQueryChain = LLMChain(
            prompt = PromptTemplate(
                input_variables = [self.requirements_key, self.background_information_key, self.summary_list_key],
                template = podcast_structure_context_queries,
            ),
            llm=llm
        )

        resp = contextQueryChain(inputs = {
            self.summary_list_key: "\n".join(summaries_list),
            self.requirements_key: requirements,
            self.background_information_key: background_information
        })
        print(resp)
        cleaned_queries = None
        try:
            cleaned_queries = [x.replace("\n", "") for x in str(resp["text"]).split("*") if x is str and x != ""]
        except:
            pass
        return cleaned_queries
    
    def retrieveContextualInformation(self, retriever, queries: List[str]) -> List[Tuple[str, List[str]]]:

        # init qa chain, specialized on responding to questions
        rqa = RetrievalQA.from_chain_type(llm=self.buildLLM(0.5), 
                                  chain_type="stuff", 
                                  retriever=retriever, 
                                  return_source_documents=True)
        
        contexts_and_sources = [
            (print(f"Query: {query}"), rqa(query))[1] for query in queries
        ]
        contexts_and_sources = [(cas["result"], [source.page_content for source in cas["source_documents"]]) for cas in contexts_and_sources]

        return contexts_and_sources
    
    def generatePodcastStructure(self, background_information, requirements, research):
        podcastStructurePrompt = PromptTemplate(
            template = podcast_structure_planning_template,
            input_variables = [
                self.background_information_key,
                self.requirements_key,
                self.research_key,
                self.json_example_key
            ]
        )

        podcast_structure_chain = LLMChain(
            prompt=podcastStructurePrompt,
            llm=self.buildLLM(0.9)
        )
        concatenated_research = "\n".join(research)
        return podcast_structure_chain({
            self.background_information_key: background_information,
            self.requirements_key: requirements,
            self.research_key : concatenated_research,
            self.json_example_key: podcast_structure_json_example
        })
