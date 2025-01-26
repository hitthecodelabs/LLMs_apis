# Source:  https://github.com/Strvm/meta-ai-api

# pip install meta-ai-api

from meta_ai_api import MetaAI

prompt = "Whats the weather in San Francisco today? And what is the date?"

ai = MetaAI()
response = ai.prompt(message=prompt)

print(response)
