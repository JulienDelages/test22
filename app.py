import requests
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer " + os.getenv('API_KEY')}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

st.title('Hello World!')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')


if submit_button:
    output = query(text)
    st.subheader('Data')
    st.write(output)
    st.write({"text": text})
