from dotenv import load_dotenv
import os
import requests

load_dotenv()
apiKey=os.getenv("GEMINI_API_KEY")
apiURL=os.getenv("GEMINI_API_ENDPOINT_URL")

def Gemini(prompt):
    body={"contents": [
      {
        "parts": [
          {
            "text": prompt
          }
        ]
      }
    ]}
    headers={"Content-Type":"application/json"}

    response=requests.post(apiURL+apiKey,json=body,headers=headers).json()
    data=response["candidates"][0]["content"]["parts"][0]["text"]
    return data

if __name__=="__main__":
  print(Gemini("Hello Gemini!This is API test."))