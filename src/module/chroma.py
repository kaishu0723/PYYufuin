import chromadb
from chromadb.utils import embedding_functions
import Gemini

# 永続化クライアントを作成 (指定したパスにデータが保存される)
client = chromadb.PersistentClient(path="./chroma_db_storage") # "./chroma_db_storage" は保存先のディレクトリ

collection_name="test_info"
default_ef=embedding_functions.DefaultEmbeddingFunction()
collection=client.get_or_create_collection(
    name=collection_name,
    embedding_function=default_ef
)

my_name="Kaishu Matsuo"
my_birthplace="Hirokawa in Fukuoka"

document_context=my_birthplace
document_id=my_name

collection.add(
    documents=[document_context],
    metadatas=[{"name":my_name,"birthplace":my_birthplace,"type":"test_record"}],
    ids=[document_id]
)

retrieved_data=collection.get(ids=[document_id],include=['documents','metadatas'])
info=retrieved_data["documents"][0]
name="Kaishu Matsuo"
prompt=f"""
以下の情報は{name}の出身地です。その情報をもとにユーザーからの質問に応えてください。
情報：{info}
ユーザーからの質問：「Kaishu Matsuoの出身地はどこですか？」
"""

print(Gemini.Gemini(prompt))