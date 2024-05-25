import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

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

dictapp={"command prompt" : "cmd","paint":"paint","notepad":"notepad","calculator":"calc","wordpad":"write","chrome":"chrome","firefox":"firefox","edge":"msedge","explorer":"explorer","vlc":"vlc","player":"wmplayer","music":"wmplayer","video":"wmplayer","photos":"ms-photos","camera":"windows.camera","calendar":"outlookcal","mail":"outlookmail","maps":"bingmaps","news":"bingnews","weather":"bingweather","store":"ms-windows-store","settings":"ms-settings","control panel":"control","task manager":"taskmgr","device manager":"devmgmt.msc","disk management":"diskmgmt.msc","services":"services.msc","event viewer":"eventvwr.msc","system information":"msinfo32","registry editor":"regedit","powershell":"powershell","windows powershell":"powershell","windows terminal":"wt","windows security":"windowsdefender","windows security center":"windowsdefender","windows security settings":"windowsdefender","windows security configuration":"windowsdefender","vscode":"code","powerpoint":"powerpnt"}
def openApp(query):
    
    if ".com" in query or ".co.in" in query or ".org:" in query or ".net" in query:
        query=query.replace("open","")
        query=query.replace("daisy","")
        query=query.replace("launch","")
        speak("Launching "+query)
        webbrowser.open(f"https://{query}")
        speak("Launching "+query)
    else:
        query=query.replace("open","")
        query=query.replace("daisy","")
        query=query.replace("launch","")
        speak("Launching "+query)
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}.exe")
                break

def closeappweb(query):
    query=query.replace("open","")
    query=query.replace("daisy","")
    query=query.replace("launch","")
    query=query.replace("close","")
    speak("Closing "+query)
    if "tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("Tab closed")
    elif "2 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    elif "3 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")    
    elif "window" in query:
        pyautogui.hotkey("ctrl","shift","w")
        speak("Window closed")

    else :
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                break

