import speak
import datetime
from weather import get_weather

def greeting():
    speak.speak(get_weather())
    current_time = datetime.now().hour
    if 3 <= current_time < 12:
        speak.speak("Good morning, sir!")
    elif 12 <= current_time < 18:
        speak.speak("Good afternoon, sir!")
    elif 18 <= current_time < 19:
        speak.speak("Good evening, sir!")
    else:
        speak.speak("Sir! It's past 9 o'clock. Are we working on something?")

if __name__ == "__main__":
    greeting()