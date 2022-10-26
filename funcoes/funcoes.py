import pyttsx3
import datetime

gigi = pyttsx3.init()

def horaF():
    hora = datetime.datetime.now().strftime("%H:%M")
    print("foi " + hora)
    gigi.say("Ola lindo")
    gigi.say("São"+hora)
    gigi.runAndWait()