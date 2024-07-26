import os
from threading import Thread
import webbrowser
import pywhatkit
from datetime import datetime
import speak
import pygame
import pyautogui
import wikipedia ,window , music, weather, take_command, email, greeting , Gesture_Controller as gc, pdf_reader

def run_ai():
    try:
        greeting()
        while True:
            command = take_command()
            
            if "hello" in command:
                speak.speak("Hello boss, how are you?")
            
            elif 'exit' in command:
                speak.speak("Goodbye, sir.")
                break
        
            elif 'location' in command:
                speak.speak('Which place are you looking for ?')
                temp_audio = speak.record_audio()
                speak.speak(temp_audio)
                speak.speak('Locating...')
                url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
                try:
                    webbrowser.get().open(url)
                    speak.speak('This is what I found Sir')
                except:
                    speak.speak('Please check your Internet')
            
            elif 'open' in command and 'DISPLAY' in os.environ:
                app_name = command.replace('open', "").strip()
                speak.speak('Opening ' + app_name)
                pyautogui.press('super')
                pyautogui.typewrite(app_name)
                pyautogui.sleep(1)
                pyautogui.press('enter')
            
            elif 'launch gesture recognition' in command:
                if gc.Gesture_Controller.GestureController.gc_mode:
                    speak.speak('Gesture recognition is already active')
                else:
                    gc = gc.Gesture_Controller.GestureController()
                    t = Thread(target = gc.start)
                    t.start()
                    speak.speak('Launched Successfully')

            elif ('stop gesture recognition' in command) or ('top gesture recognition' in command):
                if gc.Gesture_Controller.GestureController.gc_mode:
                    gc.Gesture_Controller.GestureController.gc_mode = 0
                    speak.speak('Gesture recognition stopped')
                else:
                    speak.speak('Gesture recognition is already inactive')
              
            elif 'search' in command or 'search in wikipedia' in command:
                query = command.replace('search', '').strip()
                speak.speak(' searching for ' + query + ' on wekipedia ')
                wikipedia.search_wikipedia(query)
            
            elif 'minimise window' in command:
                speak.speak('minimizening window')
                window.minimize_window()

            elif 'maximize window' in command:
                speak.speak('maximizening window')
                window.maximize_window()

            elif 'show windows' in command:
                speak.speak('showing open windows')
                window.print_window_details()

            elif 'switch to window' in command:
                speak.speak('Switching windows')
                window_title = command.replace('switch to window', '').strip()
                window.switch_to_window(window_title)
            
            elif 'play' in command:
                song_name = command.replace('play', '').strip()
                speak.speak(f"Playing song {song_name}...")
                music.play_music(song_name)

            elif 'pause' in command:
                speak.speak("Pausing music...")
                music.pause_music()

            elif 'resume' in command:
                speak.speak("Resuming music...")
                music.resume_music()

            elif 'stop' in command:
                speak.speak("Stopping music...")
                music.stop_music()
            
            elif 'play next' in command:
                speak.speak("Playing next song...")
                music.play_next_song()

            elif 'play previous' in command:
                speak.speak("Playing previous song...")
                music.play_previous_song()

            elif 'play random' in command:
                speak.speak("Playing a random song...")
                music.play_random_song()
                
            elif 'close' in command and 'DISPLAY' in os.environ:
                pyautogui.hotkey('alt', 'f4')
                speak.speak('Done, sir.')
            
            elif 'time' in command:
                current_time = datetime.now().strftime('%I:%M %p')
                speak.speak('Current time is ' + current_time)
            
            elif 'sleep' in command:
                speak.speak('Okay sir, I am going to sleep. Wake me up by saying "wake up"!')
                while True:
                    wake_up_command = take_command()
                    if 'wake up' in wake_up_command:
                        speak.speak("I am awake now, sir!")
                        break
            
            elif 'read pdf ' in command or 'summarize the pdf ' in command or 'analyze the pdf ' in command:
                speak.speak('sir please provide the path of the book or pdf')
                file_path = input("Please enter the path to the PDF file: ")
                pdf_reader.pdf_reader(file_path)
            
            elif 'write an email' in command or 'compose an email' in command or 'send an email' in command:
                speak.speak('Sure sir, please provide the email address of the recipient.')
                receiver = input('Enter the email address: ')
                speak.speak('What should be the subject of the email?')
                subject = take_command()
                speak.speak('What should be the content of the email?')
                email_content = take_command()
                email.send_email(receiver, subject, email_content)
                speak.speak(f'Done, sir. Email sent successfully to {receiver}')
            
            elif 'todays weather' in command or 'weather' in command:
                weather.get_weather()
                
            elif " search on google " in command:
                query = command.replace('search on google', '').strip()
                speak.speak(' searching for ' + query + 'on wekipedia')
                url = 'https://google.com/search?q=' + command.split('search on google')[1]
                try:
                    webbrowser.get().open(url)
                    speak.speak('This is what I found Sir')
                except:
                    speak.speak('Please check your Internet')
                
                
                
    except KeyboardInterrupt:
        speak.speak("Goodbye, sir. It pleasure working with you.")

if __name__ == "__main__":
    speak.set_voice(12)
    run_ai()
