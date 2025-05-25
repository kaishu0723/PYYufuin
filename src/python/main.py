from cartesia import cartesia
import playRaw
import json


bytesData=cartesia("Hello Cartesia","en")
chunk_list=[]
for chunk in bytesData.iter_lines(decode_unicode=True):
    chunk_list.append(chunk)

for text in chunk_list:
    data=(text.partition("data: ")[2])
    if data:
        jsondata=json.loads(data)
        if "data" in jsondata:
            audio_file=playRaw.playRawBytes(jsondata["data"].encode())
            playRaw.playRaw(audio_file)