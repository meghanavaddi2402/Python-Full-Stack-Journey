#text = gTTS("Hello guys, How are you doing?")
#text.save("audio.mp3")
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os
import random
#Listen function
def listen():
    """Function for speech recognition"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source,phrase_time_limit = 30)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: ",data)
    except sr.UnknownValueError as e:
        print("Request failed")
    except sr.RequestError as e:
        print("Speak clearly request is failing")
    return data
'''
listen()
    tts = gTTS(data)
    tts.save("new.mp3")
    playsound.playsound("new.mp3")
listen()
'''
def respond(string):
    """Function to respond back"""
    print(string)
    tts = gTTS(string)
    tts.save("speech.mp3")
    filename = "speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def rock_paper_scissors():
    """Function for rock paper scissors"""
    choices = ["rock", "paper", "scissors"]
    respond("let's begin rock paper scissors")
    while True:
        respond("Choose rock, paper or scissors")
        user = listen()
        if not user:
            continue
        user = user.lower().strip()

        if user == "stop":
            respond("Okay, game stopped")
            break

        if user not in choices:
            respond("Please say rock, paper or scissors")
            continue
        computer = random.choice(choices)

        print("You:", user)
        print("Computer:", computer)

        if user == computer:
            respond("It's a tie")

        elif(user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or(user == "scissors" and computer == "paper"):
            respond("You won")

        else:
            respond("Computer won")
def guess_game():
    """Function for number guessing game"""

    number = random.randint(1, 10)

    respond("Let's play the guessing game")
    respond("I have selected a number between 1 and 10")
    respond("You have three guesses")

    for i in range(3):

        respond(f"Guess number {i + 1}")

        user = listen()

        if not user:
            continue

        user = user.lower().strip()

        try:
            guess = int(user)

            if guess == number:
                respond("Correct! You won")
                return

            elif guess < number:
                respond("Try a higher number")

            else:
                respond("Try a lower number")

        except ValueError:
            respond("Please say a number")

    respond(f"Your three guesses are over. The correct answer was {number}")
def va(data):
    """Virtual Assistance with actions"""
    if "how are you" in data.lower():
        listening = True
        respond("baguna thank you")
    elif "how are you doing" in data.lower():
        listening = True
        respond("all good")
    elif "time" in data.lower():
        listening = True
        respond(f"time is {time.ctime()}")
    elif "open google" in data.lower():
        listening = True
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in data.lower():
        listening = True
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in data.lower():
        listening = True
        webbrowser.open("https://www.linkedin.com/in/meghana-vaddi-5902722a7/")
    elif "open codegnan" in data.lower():
        listening = True
        webbrowser.open("https://www.placements.codegnan.com/student/performance")
    elif "play rps" in data.lower():
        listening = True
        rock_paper_scissors()
    elif "play guess game" in data.lower():
        listening = True
        guess_game()
    elif "open github" in data.lower():
        listening = True
        webbrowser.open("https://github.com/meghanavaddi2402")
    elif "where is" in data.lower():
        listening = True
        webbrowser.open("https://www.google.com/maps/search/"+ data.replace("locate",""))
    elif "inka chalu" in data.lower():
        listening = False
        respond("sare mari byee unta")
    else:
        return True
    try:
        return listening
    except UnboundLocalError as e:
        print("Speak louder")
respond("hey maggiee.... ")
listening = True
while listening:
    data = listen()
    listening = va(data)


    
