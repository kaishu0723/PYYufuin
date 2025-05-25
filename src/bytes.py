import pyaudio
from module.cartesia import cartesia

data=cartesia("Hello World","en")
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True)
    
stream.write(data.content)
stream.stop_stream()
stream.close()
p.terminate()