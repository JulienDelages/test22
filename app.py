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
