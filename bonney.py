from email.mime import audio
import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
# import wikipedia
import webbrowser
import random
import subprocess

# try:
#     import wikipedia
#     WIKIPEDIA_AVAILABLE = True
# except ImportError as e:
#     print(f"Wikipedia module not available: {e}")
#     WIKIPEDIA_AVAILABLE = False

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
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)  # ZIRA - id: 1, David - id: 0 

#speak function
def speak(text):
    """
    func to convert text to speech
    Args: text (str): The text to be spoken.
    returns: voice output
    """
    engine.say(text)
    engine.runAndWait()
    
speak("Initializing Bonney")