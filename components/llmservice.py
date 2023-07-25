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
from json import loads, dumps

class LLMService:

    def __init__(self) -> None:
        self.OPENAI_API_KEY = "OPENAI_API_KEY"
        self.queries_key = "QUERIES_KEY"
        self.contexts_and_sources_key = "contexts_and_sources"
        self.podcast_structure_key = "podcast_structure"
        self.init()

        self.message_key = "message"
        self.target_audience_key = "target_audience"
        self.topic_key = "topic"
        self.topic_gen_key = "topic_gen"
        self.bg_info_key = "bg_info"
        self.questions_key = "questions"
        self.keywords_key = "keywords"
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
            llm("SAY YES:")
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
    
    def generateContextQueries(self, topic, background_information, target_audience, message, keywords, questions, summaries_list: List[str]):
        # init llm

        llm = self.buildChatCompletionsLLM(0.9)
        # create context queries for vector database
        
        resp = self.runSingleChatCompletionsLLM(
            llm,
            prompt = self.buildContextQueryPrompt(
                topic, background_information, target_audience, message, keywords, questions, "\n".join(summaries_list)
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
        #queries = [queries[0]]
        contexts_and_sources = [
            (print(f"Query: {query}"), rqa(query))[1] for query in queries
        ]
        contexts_and_sources = [(cas["result"], [source.page_content for source in cas["source_documents"]]) for cas in contexts_and_sources]

        return contexts_and_sources
    
    def generatePodcastStructure(self, topic, background_information, target_audience, message, keywords, questions, research):
        llm = self.buildChatCompletionsLLM(0.9)
        concatenated_research = "\n".join(research)
        research = "\n".join(session_state["SUMMARIES"])
        try:
            resp = self.runSingleChatCompletionsLLM(
                llm,
                prompt = self.buildPodcastStructurePrompt(topic, background_information, target_audience, message, keywords, questions, research
                )
            )
            print(f"PODCAST-Structure: {resp}")
            return loads(resp)
        except Exception as e:
            print(f"GOT EXCEPTION {e}")
            return None
    
    def buildContextQueryPrompt(self, topic, background_information, target_audience, message, keywords, questions, summaries) -> str:
        return PromptTemplate(
                input_variables = [
                    self.topic_key,
                    self.bg_info_key,
                    self.target_audience_key,
                    self.message_key,
                    self.keywords_key,
                    self.questions_key,
                    self.summary_list_key
                ],
                template = podcast_structure_context_queries,
            ).format(
                topic = topic,
                bg_info = background_information,
                target_audience = target_audience,
                message = message,
                keywords = keywords,
                questions = questions,
                summaries = summaries
            )
    
    def buildPodcastStructurePrompt(self, topic, background_information, target_audience, message, keywords, questions, research) -> str:
        return PromptTemplate(
            template = podcast_structure_planning_template,
            input_variables = [
                self.topic_key,
                self.bg_info_key,
                self.target_audience_key,
                self.message_key,
                self.keywords_key,
                self.questions_key,
                self.research_key,
                self.json_example_key
            ]
        ).format(
            topic = topic,
            bg_info = background_information,
            target_audience = target_audience,
            message = message,
            keywords = keywords,
            questions = questions,
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
    
    def runMultipleChatCompletionsLLM(self, llm, messages) -> str:
        try:
            response = llm(messages)
            return response.content
        except:
            return ""
            
    
    def getSystemMessage(self):
        msg = PromptTemplate(
            input_variables = [
                self.podcastManager.bg_info_key,
                self.podcastManager.target_audience_key,
                self.summary_list_key,
                self.podcastManager.podcast_structure_key
            ],
            template=podcast_system_message_prompt
        ).format(
            bg_info = self.podcastManager.getStateVariableByKey(self.podcastManager.bg_info_key),
            target_audience = self.podcastManager.getStateVariableByKey(self.podcastManager.bg_info_key),
            summaries = self.podcastManager.getStateVariableByKey(self.summary_list_key),
            podcast_structure = self.podcastManager.getStateVariableByKey(self.podcastManager.bg_info_key)
        )
        return SystemMessage(content=msg)
    
    def generateContentForCurrentSection(self):
        nextContent = "UNDEFINED"
        if self.podcastManager.hasNextContent():
            nextContent = self.podcastManager.getNextContent()
        llm = self.buildChatCompletionsLLM(0.9)
        prompt = PromptTemplate(
            input_variables=[
                "section_content_a",
                "followup_example",
                "section_content_b",
                "bg_info",
                "target_audience",
                "summaries",
                "current_section",
                "last_question",
                "guest_response"
            ],
            template=podcast_decision_message_prompt
        ).format(
            section_content_a = podcast_decision_section_exp1,
            followup_example = podcast_followup_json_example,
            section_content_b = podcast_decision_section_exp1,
            bg_info = self.podcastManager.getStateVariableByKey("bg_info"),
            target_audience = self.podcastManager.getStateVariableByKey("target_audience"),
            summaries = self.podcastManager.getStateVariableByKey("summaries"),
            current_section = dumps(self.podcastManager.getContentForCurrentSection(), ensure_ascii=False, indent=4),
            last_question = self.podcastManager.getCurrentContent(),
            guest_response = self.podcastManager.getGuestResponse()
        )
        #try:
        resp = self.runSingleChatCompletionsLLM(
            llm, prompt
        )

        json_resp = loads(resp.lower())
        rqa = RetrievalQA.from_chain_type(llm=self.buildLLM(0.5), 
                                chain_type="stuff", 
                                retriever=session_state["RETRIEVER"], 
                                return_source_documents=True)
        
        database_response = rqa(json_resp["abfrage"])["result"]

        print(f"Current Content: {self.podcastManager.getCurrentContent()}")
        print(f"Guest Response: {self.podcastManager.getGuestResponse()}")
        print(f"First resp: {resp}")
        print(f"Database response: {database_response}")

        content_content_insertion_prompt = PromptTemplate(
            input_variables=[
                "database_response",
                "followup_question"
            ],
            template=podcast_content_insertion_prompt
        ).format(
            database_response=database_response,
            followup_question=json_resp["folgefrage"]
        )

        merged_question = self.runSingleChatCompletionsLLM(
            llm, content_content_insertion_prompt
        )

        print(f"Merged question: {merged_question}")
        
        if isinstance(merged_question, str):
            return merged_question
        else:
            return None
        #except Exception as e:
        #    print(f"Exception: {e}")
        #    return None
    
    def generatePodcastSummary(self):
        session_state["podcast_summary"] = "PODCAST SUMMARY"