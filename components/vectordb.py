from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
import streamlit as st
from io import BytesIO
from langchain.docstore.document import Document
from typing import List


class VectorDatabaseService:

    def __init__(self) -> None:
        self.SUMMARIES_KEY = "SUMMARIES"
        self.docsearch = None
        self.retriever = None

    def readLocalPDF(self, filename):
        doc_reader = PdfReader(f"./content/{filename}")
        # read data from the file and put them into a variable called raw_text
        raw_text = ''
        for i, page in enumerate(doc_reader.pages):
            text = page.extract_text()
            if text:
                raw_text += text
        
        return raw_text

    def createDBfromPDFs(self, files: List[BytesIO]):
        # raw read pdfs
        raw_texts = []
        localPDFs = ["businessmodels.pdf",] #"conceptualizing.pdf"]
        [raw_texts.append(self.readLocalPDF(fname))
         for fname in localPDFs]
        # read uploaded pdfs
        [raw_texts.append(self.readUploadedlPDF(updf)) for updf in files]

        # summarize PDFs
        st.session_state[self.SUMMARIES_KEY] = [self.summarize_text(text) for text in raw_texts]

        # cut texts in pieces for vector database
        all_texts_chunks = []
        [
            [all_texts_chunks.append(chunk) for chunk in self.splitText(raw_text)]
            for raw_text in raw_texts
        ]
        # create db
        self.createFAISS(all_texts_chunks)

    def summarize_text(self, text):
        llm = OpenAI(temperature=0.9) # type: ignore
        split_text = self.splitText(text)
        docs = [Document(page_content=t) for t in split_text]
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(docs)   
        return summary
    
    def readUploadedlPDF(self, stream: BytesIO):
        doc_reader = PdfReader(stream)
        # read data from the file and put them into a variable called raw_text
        raw_text = ''
        for i, page in enumerate(doc_reader.pages):
            text = page.extract_text()
            if text:
                raw_text += text

        return raw_text
    
    
    def splitText(self, txt: str):
        # Splitting up the text into smaller chunks for indexing
        text_splitter = CharacterTextSplitter(        
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap  = 200, #striding over the text
            length_function = len,
        )
        texts = text_splitter.split_text(txt)
        return texts
    

    def createFAISS(self, texts):
        embeddings = OpenAIEmbeddings() # type: ignore
        self.docsearch = FAISS.from_texts(texts, embeddings)
        self.retriever = self.docsearch.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 6}
        )
        st.session_state["FAISS"] = self.retriever
        st.session_state["docsearch"] = self.docsearch