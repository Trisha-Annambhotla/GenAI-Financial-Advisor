import streamlit as st
from qa_chain import load_qa_chain

st.set_page_config(page_title="GenAI Financial Chatbot", layout="centered")

st.title("💬 Financial FAQ Chatbot")
st.markdown("Ask a question based on your uploaded financial FAQs.")

# Load QA chain
try:
    qa_chain = load_qa_chain()
except Exception as e:
    st.error(f"❌ Failed to load QA chain: {e}")
    st.stop()

# Initialize session state
st.session_state.setdefault("chat_history", [])
st.session_state.setdefault("input_text", "")

# Input row: text box and submit button
col1, col2 = st.columns([6, 1])
with col1:
    query = st.text_input(
        label="💡 Ask your question:",
        value=st.session_state.input_text,
        label_visibility="collapsed",
        key="input_text_box"
    )
with col2:
    submitted = st.button("Submit")

# Process query
if submitted and query.strip():
    with st.spinner("Generating answer..."):
        answer = qa_chain(query.strip())

    st.session_state.chat_history.append({
        "question": query.strip(),
        "answer": answer
    })

    st.session_state.input_text = ""
    st.rerun()

# Display chat history
for chat in reversed(st.session_state.chat_history):
    st.markdown(f"""
        <div style='background-color:#2c2f33;padding:10px;border-radius:10px;margin-bottom:10px;'>
            <p style='color:#00acee;'><strong>You:</strong> {chat['question']}</p>
            <p style='color:#b9fbc0;'><strong>Bot:</strong> {chat['answer']}</p>
        </div>
    """, unsafe_allow_html=True)
