from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings

class VectorDatabaseService:

    def __init__(self) -> None:
        docsearch = None
        retriever = None

    def readPDF(self, filename):
        doc_reader = PdfReader(f"/Users/filipp.einik/Desktop/Bachelorarbeit/ai_app/content/{filename}")
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