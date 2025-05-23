import requests
from dotenv import load_dotenv
import os

# 環境変数の呼び出し
load_dotenv()
apiKey=os.getenv("CARTESIA_API_KEY")
apiURL=os.getenv("CARTESIA_API_ENDPOINT_URL")


def cartesia(text,lang):
    # リクエストボディ
    payload={
        "model_id":"sonic-2",
        "transcript":f"{text}",
        "voice":{
            "mode":"id",
            "id":"bf0a246a-8642-498a-9950-80c35e9276b5"
        },
        "output_format":{
            "container":"raw",
            "encoding":"pcm_f32le",
            "sample_rate":44100
        },
        "language":f"{lang}"
    }

    # リクエストヘッダ
    headers={
        "Cartesia-Version":"2025-04-16",
        "Authorization":f"Bearer {apiKey}",
        "Content-Type":"application/json"
    }

    # POSTリクエストを送信
    response=requests.post(apiURL,json=payload,headers=headers)
    return response