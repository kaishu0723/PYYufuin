from src.retriever import retriever
from src.generate import generate
from src.translator import translate_to_oita_dialect


# $env:GOOGLE_API_KEY="AIzaSyCFyZwVbHneCGs3vQqUr7qotTrnSrRi5qI"
user_query="自然豊かな場所は？"
context=retriever(user_query)

answer=generate(user_query,context)
translate_answer=translate_to_oita_dialect(answer)

print(user_query)
print(answer)
print(translate_answer)