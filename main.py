from cartesia import cartesia
import playRaw

# cartesia
bytesData=cartesia("Hello Cartesia","en")
print(len(bytesData.content))

# playRaw
# audioFile=playRaw.playRawBytes(bytesData.content)
# playRaw.playRaw(audioFile)
playRaw.saveAsWav(bytesData.content)