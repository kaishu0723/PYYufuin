from src.retriever import retriever
from src.generate import generate

user_query="トイレどこ？"
context=retriever(user_query)

answer=generate(user_query,context)

print(user_query)
print(answer)