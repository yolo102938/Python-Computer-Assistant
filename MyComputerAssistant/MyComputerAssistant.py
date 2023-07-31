import os
import time
from winsound import PlaySound
import speech_recognition as sr
import pyautogui
import requests
import g4f
import pyttsx3
import ctypes, sys
import sqlite3
from BluetoothConnect import BluetoothConnect
from handleDatabase import DatabaseHandler
import pygame
pygame.init()


def find_current_largest_serial_number():
    current_largest_serial_number = 0
    for file_name in os.listdir("screenshots"):
        if file_name.startswith("screenshot") and file_name.endswith(".png"):
            try:
                serial_number = int(file_name.split("screenshot")[1].split(".png")[0])
                current_largest_serial_number = max(current_largest_serial_number, serial_number)
            except ValueError:
                pass
    return current_largest_serial_number

screenshot_serial_number = find_current_largest_serial_number() + 1

def play_screenshot_sound():
    # Change the sound_file_path to the actual path of your screenshot sound file
    my_sound = pygame.mixer.Sound("Screenshot.mp3")
    my_sound.play()

def get_code_from_chatgpt(audio_input):
    # Replace the next line with your preferred prompt for ChatGPT
    prompt = audio_input

    # Call the OpenAI API to get the code
    response = g4f.ChatCompletion.create(
        model=g4f.Model.gpt_4,  # You can also try "text-davinci-003" for GPT-3
        provider=g4f.Provider.ChatgptAi,
        prompt=prompt,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )

    # Find the index of the first occurrence of triple backticks
    start_index = response.find('```')

    # Find the index of the first '\n' after the first occurrence of triple backticks
    start_index = response.find('\n', start_index + 3)

    # Find the index of the second occurrence of triple backticks
    end_index = response.find('```', start_index + 1)

    # Extract the desired substring
    code = response[start_index + 1:end_index]

    return code

def get_command_from_chatgpt(audio_input):
    prompt = f"""
    I am a chatbot acting as a Windows terminal assistant. Execute a command that will: {str(audio_input)}. 
    Please start the command with '~' and end it with '~'. Do not write '~' anywhere else besides at the start and end of the code. 
    If the command I requested does not exist, write a correct command to perform the task I requested, 
    and do not assume I have any executables added to my PATH environment variable; write the whole path if necessary; if you cant write the requested command, replay "cant"."""

    # Call the OpenAI API to get the command
    response = g4f.ChatCompletion.create(
        model=g4f.Model.gpt_4,
        provider=g4f.Provider.ChatgptAi,
        prompt=prompt,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    print(response)
    start_index = response.find('~')
    end_index = response.find('~', start_index + 1)

    if start_index != -1 and end_index != -1:
        command = response[start_index + 1:end_index].strip()
    else:
        print("Failed to extract command from GPT response")
        command = ""

    return command

def get_answer_from_chatgpt(audio_input):
    prompt = audio_input

    # Call the OpenAI API to get the command
    response = g4f.ChatCompletion.create(
        model=g4f.Model.gpt_4,
        provider=g4f.Provider.ChatgptAi,
        prompt=prompt,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    os.system("start notepad")
    time.sleep(1)
    pyautogui.typewrite(response)
    text_to_speech(response)

def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate", 160)  # Adjust the speech rate (words per minute)
    engine.say(text)
    engine.runAndWait()

def set_default_voice_on_windows(voice_registry_key):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Find the voice with the matching registry key
    for voice in voices:
        if voice_registry_key.lower() in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break


def listen_and_execute_command():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            execute_command(command)

            if "exit" in command or "quit" in command:
                break

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error occurred; {e}")


def execute_command(command):
    global screenshot_serial_number
    if "take a screenshot" in command:
        take_screenshot()
    elif "live write a code" in command:
        command = command[5:]
        write_code_from_chatgpt_live(command)
    elif "write a code" in command:
        write_code_from_chatgpt_notepad(command)
    elif "tell me a joke" in command:
        tell_joke()
    elif command.startswith("search"):
        site_search(command)
    elif command.startswith("google search"):
        google_search(command)
    elif command.startswith("chat"):
        command = command[5:]
        get_answer_from_chatgpt(command)
    elif command.startswith("close"):
        close_tab()
    elif "connect bluetooth" in command:
        BluetoothConnect.main_action()
        pyautogui.hotkey("alt", "f4")
    elif "netflix search" in command:
        netflix_search(command)
    elif "netflix login" in command or "netflix log in" in command:
        netflix_tap()
    elif "netflix first" in command:
        netflix_first()
    else:
        write_command_from_chatgpt_notepad(command)

def close_tab():
    pyautogui.hotkey("ctrl", "w")

def google_search(command):
    search_query = """start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.google.com/search?q=""" + command[len("google search "):] + '"'
    os.system(search_query)

def site_search(command):
    search_query = command[len("search "):].strip()
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)
    pyautogui.typewrite(search_query, interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")
    print(f"Terminal: Searching for '{search_query}'.")

def netflix_search(command):
    search_query = command[len("netflix search "):].strip()
    pyautogui.moveTo(1650, 200)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite(search_query, interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")
    print(f"Terminal: Searching for '{search_query}'.")

def netflix_tap():
    pyautogui.moveTo(550, 600)
    pyautogui.click()

def netflix_first():
    pyautogui.moveTo(300, 550)
    pyautogui.click()
    pyautogui.moveTo(500, 800)
    pyautogui.click()

def take_screenshot():
    global screenshot_serial_number
    file_name = f"screenshots/screenshot{str(screenshot_serial_number)}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)
    print(f"Screenshot saved as '{file_name}'.")
    screenshot_serial_number += 1
    play_screenshot_sound()

def tell_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke_data = response.json()
        setup = joke_data["setup"]
        punchline = joke_data["punchline"]
        os.system("start notepad")
        time.sleep(1)
        pyautogui.typewrite(setup + "\n" + punchline)
    else:
        print("Failed to fetch a joke. Please try again later.")

def write_code_from_chatgpt_notepad(audio_input):
    # Get code from ChatGPT API based on the audio input
    code = get_code_from_chatgpt(audio_input)

    # Open Notepad and type the code
    os.system("start notepad")
    time.sleep(1)
    pyautogui.typewrite(code)

def write_code_from_chatgpt_live(audio_input):
    # Get code from ChatGPT API based on the audio input
    code = get_code_from_chatgpt(audio_input)
    pyautogui.typewrite(code)

def write_command_from_chatgpt_notepad(audio_input):
    command = DatabaseHandler.find_command_by_input(audio_input)
    if command:
        print("Found command in the database:")
        os.system(command)
    else:
        # Get code from ChatGPT API based on the audio input
        code = get_command_from_chatgpt(audio_input)
        if code:
            # Execute the code
            res = os.system(code)
            # Ask for audio input
            
            if res == 0:
                DatabaseHandler.insert_command(code, audio_input)
                return
            else:
                audio_input = "google search " + audio_input
                google_search(audio_input)
                return

        else:
            print("No valid command received from GPT.")

if __name__ == "__main__":
    print("Voice commands are listening. Say commands like 'open file explorer', 'open browser', 'search something', 'open notepad', 'shut down', 'open calculator', 'take a screenshot', 'tell me a joke', 'open netflix', 'write a code that does ...', or say 'exit' to quit.")
    DatabaseHandler.create_table_if_not_exists()
    listen_and_execute_command()
