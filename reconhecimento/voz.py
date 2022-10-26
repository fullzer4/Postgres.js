import time
import speech_recognition as sr

global frase, mic

rec = sr.Recognizer()

def IniciarDesk():
    with sr.Microphone(device_index=8) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("fale alguma coisa")
        audio = rec.listen(mic)
        frase = rec.recognize_google(audio, language="pt-BR")
        print(frase)
    time.sleep(5)
    if "Gabriel" in frase:
        print("foi")

while True:
    IniciarDesk()
