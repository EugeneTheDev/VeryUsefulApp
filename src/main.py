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
    "undo": "command+z" if is_mac else "ctrl+z",
    "redo": "command+shift+z" if is_mac else "ctrl+shift+z"
}

languages = {
    "en": {
        "undo": "f***",  # fuck
        "redo": "s***"  # shit
    },
    "ru": {
        "undo":  "блять",
        "redo": "п*****"  # пиздец
    }
}


def recognize(audio, lang="en"):
    try:
        print("Capture audio")
        phrase = recognizer.recognize_google(audio, language=lang)
        print(f"Recognised phrase: {phrase}")
        if languages[lang]["undo"] in phrase:
            commands.append(shortcuts["undo"])
        elif languages[lang]["redo"] in phrase:
            commands.append(shortcuts["redo"])
    except sr.UnknownValueError:
        print("Not recognized :(")
    except KeyError:
        print("Unsupported language")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        language = sys.argv[1]
    else:
        language = "en"

    recognizer.listen_in_background(sr.Microphone(), callback=lambda instance, audio: recognize(audio, language), phrase_time_limit=5)
    while True:
        if commands:
            keyboard.press_and_release(commands.pop())
        time.sleep(0.1)
