import pickle
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from chromadb.config import Settings
import os

CHROMA_DB_DIR = "./RAG/vector_store"
BM25_INDEX_PATH = "./RAG/bm25_index.pkl"

def load_indexes():
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore=Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings,
        client_settings=Settings(anonymized_telemetry=False)
    )
    
    with open(BM25_INDEX_PATH,"rb") as f:
        bm25_data=pickle.load(f)
    bm25_index=bm25_data["bm25_index"]
    chunk_texts=bm25_data["chunk_texts"]
    
    return vectorstore,bm25_index,chunk_texts

def search_documents(query,vectorstore,bm25_index,chunk_texts,n=3):
    # keyword search
    tokenized_query=query.split()
    bm25_results=bm25_index.get_top_n(tokenized_query,chunk_texts,n=n)

    # vector search
    vector_results_docs=vectorstore.similarity_search(query,k=n)
    vector_results_texts=[doc.page_content for doc in vector_results_docs]

    combined_results=vector_results_texts+bm25_results
    unique_results=list(dict.fromkeys(combined_results))

    return unique_results[:n]

def retriever(query) -> str:
    response=""
    vectorstore,bm25_index,chunk_texts=load_indexes()
    user_query=query
    retriever_docs=search_documents(user_query,vectorstore,bm25_index,chunk_texts)
    for i,doc in enumerate(retriever_docs,1):
        response=response+"\n"+str(i)+"\n"+doc+"\n"+"-"*20
    
    return response
        
if __name__ == "__main__":
    print(retriever("静かで自然豊かな場所は？"))