from module.cartesia import cartesia
from module.playRaw import playBytes

data=cartesia("Hello World","en")
playBytes(data.content)