import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language="en-in")
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()
engine = pyttsx3.init("sapi5")  
voices = engine.getProperty("voices")   
for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("daisy","")
        query = query.replace("google search","")
        query = query.replace("search","")
        query = query.replace("google","")
        speak("Searching google for "+query)
        speak("Here is what I found")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            speak(result)
        except Exception as e:
            speak("Sorry, I could not find any information on that")
    
def searchYoutube(query):
    if "youtube" in query:
        query = query.replace("daisy","")
        query = query.replace("youtube search","")
        query = query.replace("search","")
        query = query.replace("youtube","")
        web="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done sir, Here is what I found")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia..")
        query = query.replace("daisy","")
        query = query.replace("wikipedia search","")
        query = query.replace("search","")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia..")
        print(result)
        speak(result)
      