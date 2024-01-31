from dotenv import load_dotenv
load_dotenv() #for loading all environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
#function to load gemini PRO model and get responses
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#initialize our streamlit app

st.set_page_config(page_title = "Q&A Demo")
st.header('Gemini LLM Application')
input = st.text_input('Input: ', key='input')
submit = st.button('Ask the question')

#when submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader('The Resposne is')
    st.write(response)

