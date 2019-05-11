import pyttsx3

from datetime import datetime

#
agora = datetime.now()

# Contém nome do usuário
nome = "Robson"

# Exibe a hora atual
hora = agora.hour

# Exibe o minuto atual
minuto = agora.minute

texto = "Olá " + str(nome) + " seja bem vindo! Agora são " + str(hora) + " horas e " + str(minuto) + " minutos."

en = pyttsx3.init()
en.setProperty('rate', 125)  # propriedade de velocidade
en.setProperty('volume', 1)  # propriedade de volume
en.setProperty('voice', b'brazil')  # propriedade de idioma
en.say(texto)  # propriedade de texto falado
en.runAndWait()
