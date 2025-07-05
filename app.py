
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="GenAI Financial Advisor", layout="centered")

st.title("🏠 Welcome to the GenAI Financial Advisor")
st.markdown("""
Use the sidebar to navigate:

-  Generate Risk Profile
- 💬 Chat with your financial FAQ bot
""")
