from os import environ
from langchain.llms import OpenAI

class LLMService:

    def __init__(self) -> None:
        pass

    def setAPIKey(self, API_KEY):
        environ["OPENAI_API_KEY"] = API_KEY
        try:
            llm = OpenAI(temperature=0.9) # type: ignore
            llm("")
            return True
        except Exception as e:
            print(e)
            return False


x = LLMService().setAPIKey("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")

print(x)
print("hello world")