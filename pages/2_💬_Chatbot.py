# pages/2_💬_Chatbot.py

import streamlit as st
from qa_chain import load_qa_chain

st.set_page_config(page_title="GenAI Financial Chatbot", layout="centered")

st.title("💬 Financial FAQ Chatbot")
st.write("Ask a question based on your uploaded financial FAQs.")

qa_chain = load_qa_chain()

question = st.text_input("🔎 Ask your question:")

if question:
    with st.spinner("🤖 Thinking..."):
        response = qa_chain(question)
        st.success(response)
