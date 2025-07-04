# src/dialect_translator.py
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# データセットのパス
DATASET_PATH = "./RAG/data/dialect_corpus.csv"

def load_dialect_dataset():
    try:
        df = pd.read_csv(DATASET_PATH, encoding="utf-8")
        return df
    except FileNotFoundError:
        print(f"エラー: データセットファイルが見つかりません - {DATASET_PATH}")
        return None

def find_examples(dataframe, query, n=3):
    query_words = set(query.split())
    
    dataframe['match_count'] = dataframe['標準語'].apply(lambda x: len(set(x.split()) & query_words))
    
    top_n = dataframe.sort_values(by='match_count', ascending=False).head(n)
    
    examples = []
    for _, row in top_n.iterrows():
        if row['match_count'] > 0:
            examples.append(f"- 標準語: 「{row['標準語']}」 -> 大分弁: 「{row['大分弁']}」")
            
    return "\n".join(examples)


def translate_to_oita_dialect(standard_japanese_text: str) -> str:
    dataset = load_dialect_dataset()
    if dataset is None:
        return "エラー: 方言データセットを読み込めませんでした。"
    
    # 1. RAG: データセットから関連性の高いお手本を検索
    examples = find_examples(dataset, standard_japanese_text)
    
    # 2. プロンプトを作成
    prompt_template = f"""あなたはプロの大分弁翻訳家です。
以下の[お手本]を最優先で参考にして、[入力文]を自然で正確な大分弁に翻訳してください。

[お手本]
{examples}

[入力文]
{standard_japanese_text}
"""
    
    # 3. LLMで翻訳を実行
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    
    try:
        response = llm.invoke(prompt_template)
        return response.content
    except Exception as e:
        print(f"LLMの呼び出し中にエラーが発生しました: {e}")
        return "エラー: 翻訳中に問題が発生しました。"


# --- このファイルが直接実行された際のテスト用コード ---
if __name__ == '__main__':
    if not os.getenv("GOOGLE_API_KEY"):
        print("エラー: 環境変数 'GOOGLE_API_KEY' が設定されていません。")
    else:
        # 翻訳したい標準語の文
        input_text = "このラーメンはとても美味しいですね"
        
        # 大分弁に翻訳
        oita_text = translate_to_oita_dialect(input_text)
        
        print(f"標準語: {input_text}")
        print(f"大分弁: {oita_text}")

        print("-" * 20)

        input_text_2 = "もう帰ります"
        oita_text_2 = translate_to_oita_dialect(input_text_2)
        print(f"標準語: {input_text_2}")
        print(f"大分弁: {oita_text_2}")