from doctran import Doctran

doctran = Doctran(openai_api_key="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")
document = doctran.parse(content="your_content_as_string")
print(document)