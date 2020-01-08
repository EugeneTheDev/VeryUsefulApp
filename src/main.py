import sys
import time
import platform
import keyboard
import speech_recognition as sr

is_mac = platform.system() == "Darwin"

recognizer = sr.Recognizer()
recognizer.phrase_threshold = 0.1
recognizer.pause_threshold = 0.3
recognizer.non_speaking_duration = 0.3
recognizer.energy_threshold = 700

commands = []

shortcuts = {
    "undo": "command+Z" if is_mac else "ctrl+Z",
    "redo": "command+shift+Z" if is_mac else "ctrl+shift+Z"
}


def recognize(audio, lang="en-US"):
    try:
        print("Capture audio")
        phrase = recognizer.recognize_google(audio, language=lang)
        print(f"Recognised phrase: {phrase}")
        if "f***" in phrase:  # fuck
            commands.append(shortcuts["undo"])
        elif "s***":  # shit
            commands.append(shortcuts["redo"])
    except sr.UnknownValueError:
        print("Not recognized :(")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        language = sys.argv[1]
    else:
        language = "en-US"

    recognizer.listen_in_background(sr.Microphone(), callback=lambda instance, audio: recognize(audio, language), phrase_time_limit=5)
    while True:
        if commands:
            keyboard.press_and_release(commands.pop())
        time.sleep(0.1)
