import requests
from dotenv import load_dotenv
import os

load_dotenv()
apiKey=os.getenv("CARTESIA_API_KEY")
apiURL=os.getenv("CARTESIA_API_ENDPOINT_URL")

def cartesia(text,lang):
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

    headers={
        "Cartesia-Version":"2025-04-16",
        "Authorization":f"Bearer {apiKey}",
        "Content-Type":"application/json"
    }

    response=requests.post(apiURL,json=payload,headers=headers)
    return response