import base64

with open('./src/module/maou_se_system49.wav','rb') as f:
    audioData=base64.b64encode(f.read()).decode('utf-8')

with open('./src/module/test.txt','w') as f:
    f.write(audioData)