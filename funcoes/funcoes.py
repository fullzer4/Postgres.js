import pyttsx3
import datetime
import subprocess, sys

gigi = pyttsx3.init()

def horaF():
    hora = datetime.datetime.now().strftime("%H:%M")
    print("foi " + hora)
    gigi.say("Ola lindo")
    gigi.say("São"+hora)
    gigi.runAndWait()

def trabalharF():
    path_dir="C:/Users/yfullzer4/Desktop/atalhos/vs.lnk"
    open_dir= "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call((open_dir, path_dir))
