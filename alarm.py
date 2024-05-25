import pyttsx3
import datetime
import os

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

extractedtime = open("alarmtext.txt", "r")
time = extractedtime.read().strip()  # Remove trailing whitespaces
extractedtime.close()

deletetime = open("alarmtext.txt", "r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == time:
            speak("Wake up sir, It's time")
            os.startfile("music.mp3")
            break  # End the loop once alarm time is reached
        else:
            continue

ring(time)
