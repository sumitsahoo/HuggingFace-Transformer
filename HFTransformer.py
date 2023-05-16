from transformers.tools import HfAgent
import textract

token = 'HUGGING_FACE_API_KEY'

# eBook source: https://opensource.com/sites/default/files/open_source_eBook_AnOpenWorld_web.pdf
text = textract.process('data/AnOpenWorld.pdf').decode('utf-8')
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder", token=token)
agent.run ("Give me a summary of the `text`", text=text)
