from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(chunks, embeddings)
    return db