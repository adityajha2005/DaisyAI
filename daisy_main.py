import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import time  # Import time module for sleep function

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

def ring_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time.strftime("%H:%M:%S"):
            speak("Wake up sir, It's time")
            os.startfile("music.mp3")  # Start playing music
            break
        else:
            time.sleep(1)  # Wait for 1 second before checking again

def convert_to_datetime(alarm_time_str):
    # Convert user input string to datetime object
    try:
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%I:%M %p")
    except ValueError:
        speak("Invalid time format. Please provide time in HH:MM AM/PM format.") #eg 5:47 PM

        return None
    return alarm_time

from GreetMe import greetMe

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up daisy" in query:
            greetMe()

        elif "sleep daisy" in query:
            speak("Ok sir, You can call me anytime")
            break
        elif "hello" in query:
            speak("Hello sir, How can I help you?")
        elif "how are you" in query:
            speak("I am fine sir, How can I help you?")
        elif "who are you" in query:
            speak("I am Jarvis, Your personal assistant") 
        elif "what can you do" in query:
            speak("I can do a lot of things, Just tell me what you want me to do")
        elif "thank you" in query:
            speak("You are welcome, sir")

        elif "open" in query:
            from Dictapp import openApp
            openApp(query)
        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)


        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
        elif "temperature" in query:
            search = "temperature here is "
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url) 
            data = BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"Temperature here is {temp}")
        elif "weather" in query:
            search = "temperature here is "
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url) 
            data = BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"Temperature here is {temp}")

        elif "set an alarm" in query:
            print("Input time for alarm (HH:MM AM/PM)")
            speak("Set the time for the alarm (HH:MM AM/PM)")
            alarm_time_str = input("Please tell me the time (HH:MM AM/PM) :- ")
            alarm_time = convert_to_datetime(alarm_time_str)
            speak("Alarm set")
            if alarm_time:
                ring_alarm(alarm_time)
                os.startfile("music.mp3")

                

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "the date" in query:
            strDate = datetime.datetime.now().strftime("%d:%m:%Y")
            speak(f"Sir, the date is {strDate}")
        
        elif "finally sleep" in query:
            speak("Going to sleep , sir")
