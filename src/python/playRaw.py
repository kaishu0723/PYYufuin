import pyaudio
import tempfile

def playRawBytes(rawBytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".raw") as tmp:
        tmp.write(rawBytes)
        tmp.flush()
        return tmp.name


def playRaw(rawFile):
    
    p=pyaudio.PyAudio()
    channels=1
    rate=44100
    format=pyaudio.paFloat32
    chunk=4096
    
    stream=p.open(format=format,
                  channels=channels,
                  rate=rate,
                  output=True)
    
    try:
        with open(rawFile,'rb') as f:
            data=f.read(chunk)
            while data:
                stream.write(data)
                data=f.read(chunk)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        
