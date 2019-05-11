import pyttsx3

en = pyttsx3.init()
en.setProperty('rate', 125)  # Velocidade de fala
en.setProperty('volume', 0.80)  #Volume do som de fala
en.say("Olá mundo, seja bem vindo! ")
en.setProperty('voice', b'brazil')  # Escolha de idioma
en.startLoop("teste")
en.runAndWait()
