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
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("alarmtext.txt", "r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    currenttime = datetime.datetime.now().strftime("%H:%M:%S")  # Define currenttime here
    timeset = str(time)
    timenow = timeset.replace("daisy", "")
    timenow = timeset.replace(" and ", "")
    timenow = timenow.replace("set an alarm", "")
    Alarmtime = str(timenow)
    print(f"Alarm set for {Alarmtime}")
    while True:
        if currenttime == datetime.datetime.now().strftime("%H:%M:%S"):
            speak("Wake up sir, It's time")
            if currenttime == Alarmtime:
                speak("Wake up sir, It's time")
                os.startfile("music.mp3")
            elif currenttime + "00:00:30" == Alarmtime:
                exit()

ring(Time)
