# Bonney-Voice-Assistant-System

Bonney is a python-based voice assistant that can interact with the user through speech recognition, perform tasks like opening applications, seraching on Google or wikipedia, playing music, telling jokes and having small chit chats.

The project uses speech recognition and text-to-speech (TTS) to provide a hands-free assistant experience to Tony Stark's iconic JARVIS assistant.

## 🤖 Features
- Greet the user according to the time of day
- Recognize voice commands using Google Speech Recognition
- Speak responses using pyttsx3
- Time & date announcements
- Wikipedia search with spoken summary
- Open websites like Google, Facebook, Youtube
- Play random music from a specific folder
- Open system application: calculator, notepad, cmd
- Open Google Calander (via browser)
- Tell jokes and respond to basic small talk
- Exit gracefully with a voice command
and many more to come in near future...

## Requirements
- python 3.11 or higher

## How to run?
1. Create a virtual env
```bash
conda create --prefix .\bonney python=3.11 -y
```
2. Activate virtual env
```bash
conda activate .\bonney
```
3. Install required packages
```bash
pip install -r requirements.txt
```

### 🚩 License
This project is open-source and free to use for learning purposes.
