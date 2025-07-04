from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

import sys
# chatbot.py


class HFSeq2SeqPipeline:
    def __init__(self, model_name="google/flan-t5-large"):
        self.pipe = pipeline("text2text-generation", model=model_name)

    def __call__(self, prompt: str, max_new_tokens=1024):
        result = self.pipe(
            prompt,
            max_new_tokens=max_new_tokens,  # ✅ Use this instead of max_length
            do_sample=False,
            clean_up_tokenization_spaces=True,
        )
        return result[0]["generated_text"]



# Load the vector store
def load_vectorstore(index_path: str = "faiss_index"):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)
    return db

# Perform retrieval
def retrieve_documents(db, query: str, k: int = 3):
    docs = db.similarity_search(query, k=k)
    return docs

# Create prompt with context + question
def build_prompt(context_docs: list[Document], query: str):
    context = "\n\n".join([doc.page_content for doc in context_docs])
    prompt = f"Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
    return prompt

# Main chat function
def chat(query: str, db_path="faiss_index"):
    print(f"User: {query}")
    db = load_vectorstore(db_path)
    docs = retrieve_documents(db, query)

    # Join all retrieved document texts with two newlines (preserves formatting)
    retrieved_text = "\n\n".join([doc.page_content for doc in docs])

    print(f"Bot (retrieved text):\n{retrieved_text}")
    return retrieved_text



# CLI mode for testing
if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
        chat(user_query)
    else:
        while True:
            user_query = input("You: ")
            if user_query.lower() in ["exit", "quit"]:
                break
            chat(user_query)
