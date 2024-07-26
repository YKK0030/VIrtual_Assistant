import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def set_voice(voice_id):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)


