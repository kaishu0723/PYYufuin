from module.cartesia import cartesia
from module.playRaw import playSse
import json

bytesData=cartesia("Hello Cartesia","en","sse")

# SSE
chunk_list=[]
for chunk in bytesData.iter_lines(decode_unicode=True):
    chunk_list.append(chunk)

for text in chunk_list:
    data=(text.partition("data: ")[2])
    if data:
        jsondata=json.loads(data)
        if "data" in jsondata:
            playSse(jsondata["data"].encode())