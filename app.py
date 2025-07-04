import streamlit as st
from qa_chain import load_qa_chain
from src.risk_profile import calculate_profile, get_profile, render_pie_chart

st.set_page_config(page_title="GenAI Financial Advisor", layout="centered")

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Risk Profiler", "Chatbot"])

if page == "Risk Profiler":
    st.title("📊 Advanced Risk Profiler")

    score, responses = calculate_profile()

    if st.button("Get My Profile"):
        if score is None:
            st.warning("⚠️ Please answer all questions before generating your profile.")
        else:
            profile, allocation = get_profile(score)
            st.success(f"**Your Risk Profile: {profile}**")
            st.info(f"**Score:** {score} / 24")
            render_pie_chart(allocation)

elif page == "Chatbot":
    st.title("💬 Document Chatbot")

    qa_chain = load_qa_chain()

    query = st.text_input("Ask a question:")

    if query:
        with st.spinner("Generating answer..."):
            answer = qa_chain(query)
            st.write(answer)
