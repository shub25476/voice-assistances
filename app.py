import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time
import sounddevice as sd
import numpy  as np
from scipy.io.wavfile import write
import speech_recognition as sr
#---------------------------------------SPEAK FUCTION------------------------------------
def speak(audio):
    """Fuction to convert text to speech"""
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',175)#set speaking speed
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    time.sleep(1)#small pause to avoid overlap between speech and mic

    #------------------------- WISH FUCTION ---------------------------------

def wishMe():
        """Fuction to great user based on time """
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak(" Ram ram thakurji ")
        elif hour>=12 and hour<16:
            speak(" jay shree ram ")
        else:
            speak(" jai mata di ")
        speak("i am siri thakurji.please tell me how can i help you")

    #------------------------------------ LISTEN FUCTION ---------------------------------------------------
def takecommand():
    fs = 16000      # sample rate
    seconds = 5   # recording duration

    print("Listening...")
    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )
    sd.wait()

    write("temp.wav", fs, recording)
    r = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio = r.record(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
        return query
    except:
        print("Could not understand audio")
        return "none"

#------------------------------- DATA TAKE -----------------------------------------------
Jokes = [
     "Why did the computer go to the doctor?,Because it caught a virus.",
     "Why was the math book sad?,Because it had too many problems.",
     "why girls give stupid answer of any question?,because girls think with their knees.",
     "Why dont robots get tired?,cause they recharge.",
     "Why did the AI cross the road?, To optimize the other side.",
     "I would tell you a joke about Wi-Fi… ,But I’m not sure you’d get the connection.",
     "Why do programmers prefer dark mode?, Because light attracts bugs.",
]
fun_fact = [
    "In english we say you are looking very very beautiful :, but in sayari aladin sad :, tum vo channd ho jisme koi daag nhi :, tum iti sundar ho jiska koi hisab nhi",
    "Mujhe chand dhekna pasand hai:use chand sa dhikna pasand :, vo bhi apne daag nhi chupati :, akho me kajal mathe pe bindi nhi lagati :,  hoto ko uni ke haal pe chor deti :, haste huye duniya jaha ke sare bhand tor deti hai",
    "ki tum jab aaogi to khoya hua paogi :, ki mere kamre me kitabo ke sivaye kuch nhi :,  mere kamar ko sajane ki tamana hai tumhe :, mere kamre me khabo ke shiavye kuch nhi",
    "Har koi mohabbat mein fana nhi hota :, kisi ko chahana koi gunah nhi hota :,  vo puchte hai ki tum kitna chahte ho mujhe :,  vo kya jaane pyaar lafzon mein bayan nahi hota....!",
]

songs = [
    "https://open.spotify.com/track/6JARNpkUypyzQEltxZM95O?si=56f2a51290004b2e",
    "https://open.spotify.com/track/0ZMi5XnYZDQB6dOFhxWFTM?si=678a54c587884f1b",
    "https://open.spotify.com/track/2ZxFXUnvprVMI9IXBcnnAk?si=8bb8ef1420634cf0",
    "https://open.spotify.com/track/7oFrQLTu7Bi1xmTYLbBxHf?si=695d2c8d2ea049fd",
    "https://open.spotify.com/track/7ipocikxlJX318tXE4S5nE?si=daaa73e3c4904732",
    
]

#---------------------------------------- Main fuction --------------------------------
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if query == "none":
            continue

        #wikipedia search
        if 'wikipedia' in query:
            speak("searchiing wikipedia.......")
            query = query.replace("wikipedia","").strip()
            if not query:
                speak("please tell me what you want to search in a wikipedia.")
                continue
            try:
                results = wikipedia.summary(query,sentences=2)
                speak("according to wikipedia here some results")
                print(results)
                speak(results)
            except Exception as e :
                speak("sorry,I couldn't find any result on wikipedia.")
                print(f"wikipedia error : {e}")
        elif query.startswith(("tell me about","who is","what is")):
            topic = query.replace("tell me about","").replace("what is","").replace("what is","").strip()
            if topic:
                speak(f"searching wikipedia for {topic}...")
                try:
                    results = wikipedia.summary(topic,sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("sorry,i couldn't find any result on wikipedia.")
                    print(f"wikipedia error:{e}")
            else:
                speak("please specify what you want to know about.")
# Open websites
        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("https://google.com")

        elif 'open stack overflow' in query:
            speak("Opening Stack Overflow.")
            webbrowser.open("https://stackoverflow.com")

        elif 'open github' in query:
            speak("Opening GitHub.")
            webbrowser.open("https://github.com")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp Web.")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open facebook' in query:
            speak("Opening Facebook.")
            webbrowser.open("https://facebook.com")

        elif 'open instagram' in query:
            speak("Opening Instagram.")
            webbrowser.open("https://www.instagram.com/accounts/edit/?__pwa=1")

        elif 'open chatgpt'in query:
            speak("opening chatgpt")
            webbrowser.open("https://chatgpt.com/")

        elif 'open mail'  in query:
            speak("khol raha hu na")
            webbrowser.open("https://mail.google.com/mail/u/0/?hl=en#inbox")
        
        elif 'Tell me weather' in query:
            speak("kyo kha jana hai bata bhi de")
            webbrowser.open("https://in.search.yahoo.com/search?fr=mcafee&type=E210IN1590G0&p=weather")

        elif 'Income tax' in query:
            speak("opening income tax")
            webbrowser.open("https://eportal.incometax.gov.in/iec/foservices/#/login?language-code=en")
        
        elif 'Gst portal' in query:
            speak("opening gst portal")
            webbrowser.open("https://services.gst.gov.in/services/login")

        
# Time
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ma'am, the time is {strTime}")

        # Open VS Code
        elif 'open code' in query:
            speak("Opening Visual Studio Code.")
            os.startfile("code")

        # Jokes, sayari, music
        elif 'joke' in query:
            joke = random.choice(Jokes)
            speak(joke)
            print(joke)

        elif 'poem'in query:
            fun_facts = random.choice(fun_fact)
            speak(fun_facts)
            print(fun_facts)


        elif any(word in query for word in ['play a song', 'play music', 'play song']):
            song_url = random.choice(songs)
            speak("Playing a Bollywood hit song on spotify!") 
            webbrowser.open(song_url)

        # Fun actions
        elif 'flip a coin' in query:
            result = random.choice(['Heads', 'Tails'])
            speak(f"It's {result}!")
            print(f"Coin flip: {result}")

        elif 'roll a dice' in query or 'roll a die' in query:
            dice = random.randint(1, 6)
            speak(f"You rolled a {dice}!")
            print(f"Dice roll: {dice}")

        # Exit
        elif 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Goodbye pandat ji ! have a nice day")
            break

                




