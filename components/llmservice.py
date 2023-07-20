from os import environ
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from streamlit import session_state
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain, RetrievalQA
from langchain.prompts import  PromptTemplate
#import key
from prompts import *
from components.podcastmanager import PodcastManager
from typing import List, Tuple
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from json import loads

class LLMService:

    def __init__(self) -> None:
        self.OPENAI_API_KEY = "OPENAI_API_KEY"
        self.queries_key = "QUERIES_KEY"
        self.contexts_and_sources_key = "contexts_and_sources"
        self.podcast_structure_key = "podcast_structure"
        self.init()

        # context query input variable keys
        self.summary_list_key = "summaries"
        self.requirements_key = "requirements"
        self.background_information_key = "background_information"
        # podcast structure input variable keys
        self.research_key = "research"
        self.json_example_key = "json_example"
        self.podcastManager = PodcastManager()
    
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
    
    def buildLLM(self, temperature: float):
        return OpenAI(temperature = temperature) # type: ignore
    
    def generatePodcastTopics(self, bg_info, target_audience, questions, keywords, message):
        llm = self.buildChatCompletionsLLM(0.9)
        prompt = self.buildPodcastTopicsPrompt(bg_info, target_audience, questions, keywords, message)
        print(prompt)
        resp = self.runSingleChatCompletionsLLM(
            llm,
            prompt=prompt
        )

        print(f"RESPONSE: {resp}")

        cleaned_queries = None
        try:
            cleaned_queries = [x for x in resp.split("*")]
            print(f"Cleaned queries: {cleaned_queries}")
            cleaned_queries = [x.replace("\n", "") for x in cleaned_queries if type(x) is str and x != ""]
            print(f"Cleaned queries: {cleaned_queries}")
        except:
            pass
        return cleaned_queries
    
    def buildPodcastTopicsPrompt(self, bg_info, target_audience, questions, keywords, message):
        return PromptTemplate(
            input_variables=[
                self.podcastManager.bg_info_key,
                self.podcastManager.target_audience_key,
                self.podcastManager.questions_key,
                self.podcastManager.keywords_key,
                self.podcastManager.message_key
            ],
            template=podcast_topics_generation_template
        ).format(
            bg_info=bg_info,
            target_audience=target_audience,
            questions=questions,
            keywords=keywords,
            message=message
        )
    
    def generateContextQueries(self, summaries_list: List[str], requirements: str, background_information: str):
        # init llm
        print(f"Summaries : {summaries_list}")
        print(f"Req : {requirements}")
        print(f"bg : {background_information}")

        llm = self.buildChatCompletionsLLM(0.9)
        # create context queries for vector database
        
        resp = self.runSingleChatCompletionsLLM(
            llm,
            prompt = self.buildContextQueryPrompt(
                requirements, background_information, "\n".join(summaries_list)
            )
        )
        print(f"Antwort: {resp}")
        cleaned_queries = None
        try:
            cleaned_queries = [x for x in resp.split("*")]
            print(f"Cleaned queries: {cleaned_queries}")
            cleaned_queries = [x.replace("\n", "") for x in cleaned_queries if type(x) is str and x != ""]
            print(f"Cleaned queries: {cleaned_queries}")
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
        llm = self.buildChatCompletionsLLM(0.9)
        concatenated_research = "\n".join(research)
        try:
            resp = self.runSingleChatCompletionsLLM(
                llm,
                prompt = self.buildPodcastStructurePrompt(
                    background_information, requirements, research
                )
            )
            print(f"PODCAST-Structure: {resp}")
            return loads(resp)
        except Exception as e:
            print(f"GOT EXCEPTION {e}")
            return None
    
    def buildContextQueryPrompt(self, requirements, background_information, summaries) -> str:
        return PromptTemplate(
                input_variables = [self.requirements_key, self.background_information_key, self.summary_list_key],
                template = podcast_structure_context_queries,
            ).format(
                requirements = requirements,
                background_information = background_information,
                summaries = summaries
            )
    
    def buildPodcastStructurePrompt(self, background_information, requirements, research) -> str:
        return PromptTemplate(
            template = podcast_structure_planning_template,
            input_variables = [
                self.background_information_key,
                self.requirements_key,
                self.research_key,
                self.json_example_key
            ]
        ).format(
            background_information = background_information,
            requirements = requirements,
            research = research,
            json_example = podcast_structure_json_example
        )
    
    def buildChatCompletionsLLM(self, temperature: float):
        llm = ChatOpenAI(
            model="gpt-3.5-turbo-16k",
            temperature=temperature
        ) # type: ignore
        return llm
    
    def runSingleChatCompletionsLLM(self, llm, prompt: str) -> str:
        messages = [
            HumanMessage(content=prompt)
        ]
        try:
            response = llm(messages)
            return response.content
        except:
            return ""