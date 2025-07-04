# import streamlit as st
# from qa_chain import load_qa_chain
# from src.risk_profile import calculate_profile, get_profile, render_pie_chart

# st.set_page_config(page_title="GenAI Financial Advisor", layout="centered")

# # Sidebar navigation
# page = st.sidebar.selectbox("Navigation", ["Risk Profiler", "Chatbot"])

# if page == "Risk Profiler":
#     st.title("📊 Advanced Risk Profiler")

#     score, responses = calculate_profile()

#     if st.button("Get My Profile"):
#         if score is None:
#             st.warning("⚠️ Please answer all questions before generating your profile.")
#         else:
#             profile, allocation = get_profile(score)
#             st.success(f"**Your Risk Profile: {profile}**")
#             st.info(f"**Score:** {score} / 24")
#             render_pie_chart(allocation)

# elif page == "Chatbot":
#     st.title("💬 Financial FAQ Chatbot")
#     st.markdown("Ask a question based on your uploaded financial FAQs.")

#     # Load QA chain once
#     qa_chain = load_qa_chain()

#     st.markdown("Ask a question based on your uploaded financial FAQs.")


#     # Initialize session state
#     st.session_state.setdefault("chat_history", [])
#     st.session_state.setdefault("input_text", "")

#     # Input row: text box and submit button
#     col1, col2 = st.columns([6, 1])
#     with col1:
#         query = st.text_input(
#             label="💡 Ask your question:",
#             value=st.session_state.input_text,
#             label_visibility="collapsed",
#             key="input_text_box"
#         )
#     with col2:
#         submitted = st.button("Submit")

#     # Process submitted query
#     if submitted and query.strip():
#         with st.spinner("Generating answer..."):
#             answer = qa_chain(query.strip())

#         st.session_state.chat_history.append({
#             "question": query.strip(),
#             "answer": answer
#         })
#         st.session_state.input_text = ""
#         st.experimental_rerun()

#     # Display chat history
#     for chat in st.session_state.chat_history:
#         st.markdown(f"""
#             <div style='background-color:#2c2f33;padding:10px;border-radius:10px;margin-bottom:10px;'>
#                 <p style='color:#00acee;'><strong>You:</strong> {st.write("You:", chat['question'])}</p>
#                 <p style='color:#b9fbc0;'><strong>Bot:</strong> {st.write("Bot:", chat['answer'])}</p>
#             </div>
#         """, unsafe_allow_html=True)

# app.py

import streamlit as st

st.set_page_config(page_title="GenAI Financial Advisor", layout="centered")

st.title("🏠 Welcome to the GenAI Financial Advisor")
st.markdown("""
Use the sidebar to navigate:

- 📁 Upload FAQs to build your knowledge base
- 💬 Chat with your financial FAQ bot
""")
