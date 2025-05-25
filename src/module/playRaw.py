import pyaudio
import base64
import numpy as np

def playRaw(raw_data):
    # Base64デコード
    decoded_data = base64.b64decode(raw_data)
    
    # バイトデータをnumpy配列に変換
    audio_data = np.frombuffer(decoded_data, dtype=np.float32)
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paFloat32,
                   channels=1,
                   rate=44100,
                   output=True)
    
    try:
        stream.write(audio_data.tobytes())
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()