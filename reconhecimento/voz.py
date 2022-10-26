from tkinter import W
import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(device_index=3) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Reconhecimento de voz")
    audio = rec.listen(mic)
    frase = rec.recognize_google(audio, language="pt-BR")
    print(frase)