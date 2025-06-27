import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pywhatkit
import psutil

# Initialize TTS engine
machine = pyttsx3.init()
machine.setProperty('rate', 150)
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female

def speak(text):
    machine.say(text)
    machine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am your assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"You said: {query}")
    except Exception:
        print("Could you please repeat that?")
        return "None"
    return query.lower()

def close_browser():
    # Close Chrome
    for proc in psutil.process_iter():
        if proc.name().lower() in ["chrome.exe", "msedge.exe", "firefox.exe"]:
            proc.kill()
            speak("Browser closed.")
            return
    speak("No supported browser was running.")

def run_assistant():
    wish_me()
    while True:
        query = take_command()

        if 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif 'open linkedin' in query:
            speak("Opening LinkedIn...")
            webbrowser.open("https://www.linkedin.com/in/manoj0902")

        elif 'open github' in query:
            speak("Opening GitHub...")
            webbrowser.open("https://www.github.com/Manojr17")

        elif 'open chatgpt' in query:
            speak("Opening ChatGPT...")
            webbrowser.open("https://chatgpt.com")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp...")
            webbrowser.open("https://www.whatsapp.com")

        elif 'play' in query and 'song' in query:
            song = query.replace('play', '').replace('song', '').strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)


        elif 'close browser' in query or 'close youtube' in query:
            close_browser()


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    run_assistant()
