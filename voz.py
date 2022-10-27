import speech_recognition as sr
import pyttsx3
from funcoes.funcoes import horaF, trabalharF

rec = sr.Recognizer()
gigi = pyttsx3.init()

def executarComandos():
    try:
        with sr.Microphone(device_index=2) as mic: # 2 desktop e 8 notebook Ubuntu
            rec.adjust_for_ambient_noise(mic)
            audio = rec.listen(mic)
            frase = rec.recognize_google(audio, language="pt-BR")
            frase = frase.lower()
            print(frase)
        return frase
    except:
        return "nada"

def comandoUser(): #funcionando
    global frase
    frase = executarComandos()
    if "nada" in frase:
        return
    elif "gigi" in frase:
        frase = frase.replace("gigi", "")
        comandosMaquina()
    else:
        return

def comandosMaquina():
    if "horas" in frase:
        horaF()
        print("Executou Horas")
    elif "trabalhar" in frase:
        # trabalharF()
        return
    else:
        return


while True:
    comandoUser()