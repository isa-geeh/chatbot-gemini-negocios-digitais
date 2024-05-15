import os
import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyANyiDGTaSm4mkjkmccQ80Dug9ES3-URYo"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

st.title("Abra seu Negócio Digital !")

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role
    
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("I possess a well of knowledge. what would you like to know"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)