import requests

url="https://api.cartesia.ai/tts/bytes"
key="sk_car_uAFeAZBW21UQDeTLofYaar"

def cartesia(text,lang):
    payload={
        "model_id":"sonic-2",
        "transcript":f"{text}",
        "voice":{
            "mode":"id",
            "id":"bf0a246a-8642-498a-9950-80c35e9276b5"
        },
        "output_format":{
            "container":"wav",
            "encoding":"pcm_f32le",
            "sample_rate":44100
        },
        "language":f"{lang}"
    }

    headers={
        "Cartesia-Version":"2025-04-16",
        "Authorization":f"Bearer {key}",
        "Content-Type":"application/json"
    }

    response=requests.post(url,json=payload,headers=headers)

    with open("output.wav","wb") as f:
        f.write(response.content)
        

cartesia("Hello Cartesia!","en")