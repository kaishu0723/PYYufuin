import requests
from dotenv import load_dotenv
import os

load_dotenv()
apiKey=os.getenv("CARTESIA_API_KEY")

def cartesia(text,lang,method):
    apiURL=os.getenv("CARTESIA_API_ENDPOINT_URL")+method
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

if __name__=="__main__":
    print(cartesia("Hello Cartesia!","en"))

# event :chunk
# data:{"...":"...","data":"..."}

# event :chunk
# data:{}

# --[省略]--


# event :done
# data:{}