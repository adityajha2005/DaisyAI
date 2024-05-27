import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import time  # Import time module for sleep function
import pyautogui
import keyboard
import random
import webbrowser
import wolframalpha

for(i) in range(3):
    a = input("Enter the password to open Daisy : ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("Welcome to Daisy, Speak [WAKE UP]")
        break
    elif (i==2 & a != pw):
        print("Incorrect password, Try again")
        continue
    elif(a!=pw):
        print("Incorrect password, Try again")
        continue
    

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
        speak("Invalid time format. Please provide time in HH:MM AM/PM format.")

        return None
    return alarm_time

from GreetMe import greetMe

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up daisy" in query:
            greetMe()
            
            while True:
                        query = takeCommand().lower()
                        if "sleep" in query:
                            speak("Ok sir, You can call me anytime")
                            break
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

                        elif "tired" in query:
                            speak("Playing some music for you")
                            a=(1,2,3)
                            music = random.choice(a)
                            if music == 1:
                                webbrowser.open("https://www.youtube.com/watch?v=syFZfO_wfMQ")
                            elif music == 2:
                                webbrowser.open("https://youtu.be/JGwWNGJdvx8?si=eYFYvE5DoUjMZ6VR")
                            elif music == 3:
                                webbrowser.open("https://youtu.be/7wtfhZwyrcc?si=QZy2b1e6Q7m2lYb2")

                        elif "pause" in query:
                            pyautogui.press("k")
                            speak("Paused")
                        elif "play" in query:
                            pyautogui.press("k")
                            speak("Playing")
                        elif "next" in query:
                            pyautogui.press("l")
                            speak("Next")
                        elif "previous" in query:
                            pyautogui.press("j")
                            speak("Previous")
                        elif "mute" in query:
                            pyautogui.press("m")
                            speak("Muted")
                        elif "full screen" in query:
                            pyautogui.press("f")
                            speak("Full screen")
                        elif "exit full screen" in query:
                            pyautogui.press("esc")
                            speak("Exit full screen")
                        elif "forward" in query:
                            pyautogui.press("right")
                            speak("Forward")
                        elif "backward" in query:
                            pyautogui.press("left")
                            speak("Backward")
                        elif "volume up" in query:
                            from keyboard import volumeUp
                            volumeUp()
                            speak("Volume up")
                        elif "volume down" in query:
                            from keyboard import volumeDown
                            volumeDown()
                            speak("Volume down")
                    
                    
                        
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
                        elif "news" in query:
                            from newsread import latest_news
                            latest_news()
                        elif "calculate" in query:
                            from Calculatenumbers import WolfRamAlpha
                            from Calculatenumbers import Calc
                            query = query.replace("calculate", "")
                            query = query.replace("Daisy", "")
                            Calc(query)
                            
                        elif "whatsapp" in query:
                            from Whatsapp import sendMessage
                            sendMessage()
                        
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

                        elif "remember that" in query:
                            remembermessage = query.replace("remember", "")
                            remembermessage = query.replace("daisy", "")
                            remembermessage = query.replace("that", "")
                            speak("You asked me to remember that" + remembermessage)
                            Remember = open("data.txt", "a")
                            Remember.write(remembermessage)
                            Remember.close()
                        elif "what do you remember" in query:
                            Remember = open("data.txt", "r")
                            speak("You told me " + Remember.read())

                        elif "shutdown system" in query:
                            speak("Are you sure you want to shutdown the system?")
                            shutdown =input("Are you sure you want to shutdown the system? (yes/no): ")
                            if "yes" in shutdown:
                                os.system("shutdown /s /t 1")
                            elif "no" in shutdown:
                                speak("Shutdown cancelled")
                                break
