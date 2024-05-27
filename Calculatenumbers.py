import wolframalpha
import pyttsx3
import speech_recognition

# Initialize the text-to-speech engine
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

def WolfRamAlpha(query):
    apikey = "HEVXUJ-T9P3G7YK76"
    requester = wolframalpha.Client(apikey)
    response = requester.query(query)
    try:
        answer = next(response.results).text
        # print(answer)
        speak(answer)
        return answer  
    except StopIteration:
        speak("I'm sorry, I don't have an answer to that question")
        return None

def Calc(query):
    Term = str(query)
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("divide", "/")
    Term = Term.replace("Daisy", "")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        if result:
            print(result)
            # speak(result)
    except Exception as e:
        print(f"Error: {e}")
        speak("I'm sorry, I don't have an answer to that question")

