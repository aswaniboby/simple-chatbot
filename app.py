import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Simple Chatbot")

st.title("🤖 Simple Chatbot")

user_input = st.text_input("Type your message:")

if st.button("Send"):
    if user_input:
        response = get_response(user_input)
        st.write("### Bot:")
        st.write(response)