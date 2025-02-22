# -*- coding: utf-8 -*-
"""genai_google.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UDSG3RptpEnHmZc41dYMYYM9InkNDs59
"""

!pip install -q -U google-generativeai

!pip install python-dotenv

import os
import pathlib
import textwrap

import google.generativeai as genai

from dotenv import load_dotenv

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

load_dotenv()

rr = open(".env", "w")
rr.write("GEMINI_API_KEY=key-bWRZPvc")
rr.close()

# Or use `os.getenv('GEMINI_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if ("generateContent" in m.supported_generation_methods
       and "flash-thinking" in m.name):
        print(m.name)

model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")

response = model.generate_content("What is the meaning of life?")

to_markdown(response.text)
