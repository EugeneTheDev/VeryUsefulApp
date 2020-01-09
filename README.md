# VeryUsefulApp

Utility which "simplifies" undo and redo operations. Just say some "keywords"<br> 
instead of pressing usual boring shortcuts :)

## Usage
Clone this repo and install dependencies from [requirements.txt](https://github.com/EugeneTheDev/VeryUsefulApp/blob/master/requirements.txt). 
Then just run it:
```
$ (sudo, if you are using Linux) python src/main.py <lang code to recognize (optional, default en)>
```
**IMPORTANT: When you run it, your keyboard layout must be English (for proper shortcuts work).**<br>
When app is running, you could switch your layout and work as usual.<br>
Also you may face some problems with PyAudio installation, so just follow these steps:

### macOS
Run this in terminal:
```
$ brew install portaudio
$ pip install pyaudio
```

### Linux
Run this:
```
$ sudo apt-get install python-pyaudio python3-pyaudio
$ pip install pyaudio
```

### Windows
Just install it!
```
$ pip install pyaudio
```
