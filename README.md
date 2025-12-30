# REMC

Python script for quick restart of Windows Explorer (`explorer.exe`) by pressing the middle mouse button.

## Features
* **Smart verification:** The script will not work if games (Genshin Impact, Minecraft, PUBG, emulators, etc.) are running, so as not to interfere with the gameplay.
* **Performance:** Instantly kills the hung explorer process and restarts it.

## Requirements
Python and the following libraries are needed to work:
* `pynput` (mouse tracking)
* `psutil` (checking running games)

## Installation and launch
1. Clone the repository.
2. Install the dependencies:
   `pip install -r requirements.txt`
3. Run the script:
python restart_explorer.py

