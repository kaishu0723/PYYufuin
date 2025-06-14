import socket,json

HOST='127.0.0.1'
PORT=30010

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
print("WaitStartGame")

conn,addr=server.accept()
print("Connected by",addr)

with open('./src/module/maou_se_system49.wav','rb') as f:
    audioData=f.read()

# sendJsonData={"message":"日本語対応可","audio":audioData}
# sendStringData=json.dumps(sendJsonData)

while True:
    data=conn.recv(1024)
    if not data:
        break
    jsonData=json.loads(data.decode())
    print("Received:",jsonData["message"])
    # conn.sendall(sendStringData.encode())
    conn.sendall(audioData)
    
conn.close()