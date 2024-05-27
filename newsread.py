import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break
engine.setProperty("rate", 170)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def latest_news():
    apidict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3529f3b21a4c43c796e555937e7802f8",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3529f3b21a4c43c796e555937e7802f8",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3529f3b21a4c43c796e555937e7802f8",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=3529f3b21a4c43c796e555937e7802f8",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3529f3b21a4c43c796e555937e7802f8",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3529f3b21a4c43c796e555937e7802f8",
        "general": "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=3529f3b21a4c43c796e555937e7802f8"
    }

    speak("Which news category would you like to hear? [business, entertainment, health, science, sports, technology, general]")
    field = input("Which news category would you like to hear? [business, entertainment, health, science, sports, technology, general] : ").lower()
    
    url = apidict.get(field)
    if not url:
        speak("Invalid category")
        return
    
    news = requests.get(url).text
    news_dict = json.loads(news)
    speak("Here are some top news headlines")
    arts = news_dict["articles"]
    for article in arts:
        title = article["title"]
        speak(title)
        print(title)
        news_url = article["url"]
        print(f"For more info visit: {news_url}")

        a = input("Would you like to read more news? [yes/no] : ")
        if a.lower() == "no":
            break
        else:
            continue
        speak("That's all for now")

        


