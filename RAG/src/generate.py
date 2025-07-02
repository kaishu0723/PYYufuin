from langchain_google_genai import ChatGoogleGenerativeAI
import os

def generate(query:str,context_docs:list[str]) -> str:
    context="\n---\n".join(context_docs)

    prompt_template=f"""
    以下の情報のみに基づいて、質問に大分弁で回答してください。情報に答えがない場合は、「わかりません」と答えてください。
    
    「情報」
    {context}

    [質問]
    {query}
    """
    
    llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0)
    
    try:
        response=llm.invoke(prompt_template)
        return response.content
    except Exception as e:
        print(e)
        return "generate error"
    
if __name__ == "__main__":
    dummy_query = "金閣寺について教えて"
    dummy_context = [
        "名称: 金閣寺\n都道府県: 京都府\n説明: 正式名称を鹿苑寺といい、舎利殿「金閣」が特に有名であるため通称金閣寺と呼ばれる。",
        "名称: 龍安寺\n都道府県: 京都府\n説明: 石庭で知られる禅寺。15個の石が配置されており、どの角度から見ても必ず1つは隠れるように設計されている。"
    ]
    
    answer=generate(dummy_query,dummy_context)
    print(answer)