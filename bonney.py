from email.mime import audio
import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipediaapi
import webbrowser
import random
import subprocess

# Configure logging
LOG_DIR = "logs"
LOG_FILE_NAME="app.log"
os.makedirs(LOG_DIR, exist_ok=True)

log_path= os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(
    filename= log_path,
    format="[%(asctime)s] - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Initializing voice engine
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 190)  
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)   # ZIRA - id: 1, David - id: 0 

#wiki
wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='BonneyAssistant'
)
def wiki_summary(query):
    page = wiki.page(query)
    if page.exists():
        return page.summary[0:500]
    else:
        return "sorry boss, I couldn't find any info on that topic."
    
#speak function
def speak(text):
    """
    func to convert text to speech
    Args: text (str): The text to be spoken.
    returns: voice output
    """
    engine.say(text)
    engine.runAndWait()    
# speak("Initializing Bonney. Listening for your command...")

#recognize the speech & convert it to text
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again please...")
        return "None"
    return query

def greeting():
    hour= int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning boss! What a beautiful day!")
    elif 12 <= hour < 18:
        speak("Good Afternoon boss! Hope you are having a great day!")
    else:
        speak("Good Evening boss! How was your day?")
    # speak("I am Bonney. How may I assist you today?")

#play music
def playMusic():
    music_dir = "./music"
    try:
        songs = os.listdir(music_dir)
        if songs:
            song = random.choice(songs)
            speak(f"Playing {song} from your music library.")
            os.startfile(os.path.join(music_dir, song))
            logging.info(f"Playing music: {song}")
        else:
            speak("Your music directory is empty.")
            logging.info("Music directory is empty.")
    except Exception as e:
        speak("Sorry boss, couldn't access your music directory.")
        logging.error(f"Error accessing music directory: {e}")

greeting()
while True:
    q= takeCommand().lower() 
    print(q)

    if "your name" in q or "who are you" in q:
        speak("Hello! My name is Bonney. I am your voice assistant.")
        logging.info("Provided name information.")
    
    elif "how are you" in q or "what about you" in q:
        speak("All systems operational boss")
        logging.info("Responded to 'how are you' query.")

    elif "who made you" in q:
        speak("According to all records—and my own source code—you did, boss")

    elif "time" in q:
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Boss, the time is {strTime}")
        logging.info(f"Time requested: {strTime}")

    #open calculator
    elif "open calculator" in q:
        speak("Boss here's the Calculator")
        subprocess.Popen("calc.exe")
        logging.info("Opened Calculator application.")
    #open notebook
    elif "open notepad" in q:
        speak("Boss here's the Notepad")
        subprocess.Popen("notepad.exe")
        logging.info("Opened Notepad application.")
    
    #play music
    elif "play music" in q:
        playMusic()

    #open facebook
    elif "facebook" in q:
        speak("Boss here's your Facebook")
        webbrowser.open("https://www.facebook.com/")
        logging.info("Opened Facebook website.")
    #open youtube
    elif "youtube" in q:
        speak("Boss here's your YouTube")
        webbrowser.open("https://www.youtube.com/")
        logging.info("Opened YouTube website.")
    #open github
    elif "github" in q:
        speak("Boss here's your GitHub")
        webbrowser.open("https://www.github.com/")
        logging.info("Opened GitHub website.")
    #open google
    elif "google" in q:
        speak("Boss here's Google")
        webbrowser.open("https://www.google.com/")
        logging.info("Opened Google website.")
    
    #open versity portal
    elif "university portal" in q:
        speak("Boss here's your University Portal")
        webbrowser.open("https://portal.aiub.edu/")
        logging.info("Opened University Portal website.")

    #open wikipedia
    elif "who is" in q or "what is" in q:
        speak("Searching Wikipedia...")
        q = q.replace("who is", "").replace("what is", "").strip()
        results = wiki_summary(q)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        logging.info(f"Wikipedia search for: {q}")
    
    elif "thank" in q:
        speak("welcome boss! Always happy to help.")
        logging.info("Responded to 'thank you' query.")
    
    elif "exit" in q or "stop" in q:
        speak("Goodbye boss! Have a nice day!")
        logging.info("Exit command received. Shutting down.")
        # break
        exit()
    else:
        speak("I am sorry, I didn't understand that command.")