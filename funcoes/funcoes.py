from turtle import tilt
import pyttsx3
import datetime
import subprocess, sys
from winotify import Notification, audio

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

def noticiasF():
    toast = Notification(app_id="GigiDesktopHelper", title="Mensagem", msg="conteudo", duration="short") #icon="someimg.png"
    toast.set_audio(audio.LoopingAlarm2, loop=False)
    toast.add_actions(label="Ver mais sobre", launch="")
    toast.show()