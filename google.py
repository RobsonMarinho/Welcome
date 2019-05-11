from gtts import gTTS
import os

voz = gTTS("Olá, vamos sintetizar voz com python", lang='pt')  # texto que a voz irá falar e o idioma
voz.save('voz1.mp3')

os.system('voz1.mp3')