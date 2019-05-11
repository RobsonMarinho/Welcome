from gtts import gTTS

voz = gTTS("Olá, mundo, vamos sintetizar voz com python", lang='pt')  # texto que a voz irá falar e o idioma
voz.save("voz.mp3")  # Cria um arquivo mp3 reproduto de voz
