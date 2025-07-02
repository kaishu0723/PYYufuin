import pandas as pd
from langchain.docstore.document import Document
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from rank_bm25 import BM25Okapi
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import pickle

DATA_PATH = "./RAG/data/data.csv"
CHROMA_DB_DIR = "./RAG/vector_store"
BM25_INDEX_PATH = "./RAG/bm25_index.pkl"

# load data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path,encoding="utf-8")
    except Exception as e:
        print(f"Error loading data: {e}")
        return []
    
    documents = []
    for _,row in df.iterrows():
        page_content = f"スポット名: {row['name']}\n都道府県: {row['prefecture']}\n説明: {row['description']}"
        metadata = {
            "source":file_path,
            "name":row["name"],
            "prefecture":row["prefecture"]
        }
        
        doc=Document(page_content=page_content,metadata=metadata)
        documents.append(doc)
    
    return documents


# split documents
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documents)
    return chunks


# create index
def create_index(chunks):
    chunk_texts=[chunk.page_content for chunk in chunks]
    tokenized_corpus=[doc.split() for doc in chunk_texts]
    bm25=BM25Okapi(tokenized_corpus)
    with open(BM25_INDEX_PATH,"wb") as f:
        pickle.dump({"bm25_index":bm25,"chunk_texts":chunk_texts},f)
        
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    vectorstore=Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )
    

def indexing():
    documents = load_data(DATA_PATH)
    create_index(split_documents(documents))
    

if __name__ == "__main__":
    indexing()