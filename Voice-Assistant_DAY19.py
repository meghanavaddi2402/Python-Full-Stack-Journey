import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing.....")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except Exception:
        print("Sorry, please say that again.")
        return ""
def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning\nI am your virtual assistant")
    elif hour < 18:
        speak("Good afternoon\nI am your virtual assistant")
    else:
        speak("Good evening\nI am your virtual assistant")
wish_user()
while True:
    command = take_commands()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open LinkedIns" in command:
        webbrowser.open("https://www.linkedin.com/in/meghana-vaddi-5902722a7/")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "who is" in command:
        person = command.replace("Who is", "")
        info = wikipedia.summary(command, 2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("GoodBye")
        break
