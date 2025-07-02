import socket,json,base64
from cartesia import cartesia

HOST='127.0.0.1'
PORT=30010

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
print("WaitStartGame")

conn,addr=server.accept()
print("Connected by",addr)

with open('./output.wav','wb') as f:
    f.write(cartesia("Hello World","en").content)

with open('./output.wav','rb') as f:
    audioData=base64.b64encode(f.read()).decode('utf-8')
# audioData=base64.b64encode(cartesia("Hello World","en").content).decode('utf-8')

sendJsonData={"message":"日本語対応可","audio":audioData}
sendStringData=json.dumps(sendJsonData)

while True:
    data=conn.recv(1024)
    if not data:
        break
    receiveJsonData=json.loads(data.decode())
    print("Received:",receiveJsonData["message"])
    conn.sendall(sendStringData.encode())
    # conn.sendall(audioData)
    
conn.close()