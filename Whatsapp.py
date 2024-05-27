import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))
def sendMessage():
    speak("Who do you want to send the message to?")
    a = int(input("Aditya - 1 , Babita - 2 \n Enter the number:"))

    if a == 1:
        speak("What message do you want to send?")
        message = str(input("Enter the message: "))

        pywhatkit.sendwhatmsg("+9199XX3XXXX", message, time_hour=strTime,time_min=update)
        speak("Message sent successfully")
    elif a == 2:
        speak("What message do you want to send?")
        message = str(input("Enter the message: "))
        pywhatkit.sendwhatmsg("+9198XX35XXX", message, time_hour=strTime,time_min=update)
        speak("Message sent successfully")

