import requests
from dotenv import load_dotenv

load_dentenv()

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer" + os.getenv('API_KEY')}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query("Can you please let us know more details about your ")

import streamlit as st
from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

st.title('Hello World!')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    generation = generator(text, max_length=30, num_return_sequences=5)
    st.subheader('Data')
    st.write(generation)
    st.write({"text": text})
