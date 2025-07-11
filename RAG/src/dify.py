import requests

key="app-uUXuHsvzqJ18yNA0B9qaDaFm"
header={
    "Authorization": f"Bearer {key}",
    "Content-Type":"application/json"  
}

body={
    "inputs": {},
    "query": "自然豊かな場所は？",
    "response_mode": "blocking",
    "conversation_id": "",
    "user": "abc-123",
    "files": []
}

response=requests.post("http://localhost/v1/chat-messages",headers=header,json=body)
print(response.json()["answer"])