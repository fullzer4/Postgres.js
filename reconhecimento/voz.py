from email.mime import audio
from tkinter import W
import speech_recognition as sr

rec = sr.Recognizer()

print("\n",sr.Microphone().list_microphone_names())
with sr.Microphone(device_index=8) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("fale alguma coisa")
    audio = rec.listen(mic)
    frase = rec.recognize_google(audio, language="pt-BR")
    print(frase)