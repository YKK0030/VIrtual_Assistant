import subprocess
import pyautogui
import speak

def get_window_titles_wmctrl():
    try:
        result = subprocess.run(['wmctrl', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise Exception(result.stderr.decode('utf-8'))
        
        output = result.stdout.decode('utf-8').strip()
        windows = output.splitlines()
        
        titles = {}
        for window in windows:
            parts = window.split(None, 3)
            if len(parts) == 4:
                titles[parts[0]] = parts[3] 
        return titles
    except FileNotFoundError:
        print("wmctrl is not installed or not found in PATH.")
        return {}
    except Exception as e:
        print(f"An error occurred while fetching window titles with wmctrl: {e}")
        return {}

def get_window_titles_xdotool():
    try:
        result = subprocess.run(['xdotool', 'search', '--onlyvisible', '--name', '.*'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise Exception(result.stderr.decode('utf-8'))
        
        window_ids = result.stdout.decode('utf-8').splitlines()
        
        titles = {}
        for wid in window_ids:
            result = subprocess.run(['xdotool', 'getwindowname', wid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                title = result.stdout.decode('utf-8').strip()
                titles[wid] = title  # Use window ID as key and title as value
        
        return titles
    except FileNotFoundError:
        print("xdotool is not installed or not found in PATH.")
        return {}
    except Exception as e:
        print(f"An error occurred while fetching window titles with xdotool: {e}")
        return {}

def get_all_window_titles():
    wmctrl_titles = get_window_titles_wmctrl()
    xdotool_titles = get_window_titles_xdotool()
    
    all_titles = {**wmctrl_titles, **xdotool_titles}
    return all_titles

def print_window_details():
    windows = get_all_window_titles()
    if not windows:
        print("No windows found.")
    else:
        for i, (wid, title) in enumerate(windows.items()):
            print(f"{i + 1}: {title}")
    return windows

def switch_to_window_by_number(window_number):
    windows = get_all_window_titles()
    if 0 < window_number <= len(windows):
        window_id = list(windows.keys())[window_number - 1]
        try:
            subprocess.run(['wmctrl', '-ia', window_id], check=True)
        except Exception as e:
            speak.speak(f"An error occurred while switching window: {str(e)}")
    else:
        speak.speak(f"Invalid window number: {window_number}")

if __name__ == '__main__':
    windows = print_window_details()

