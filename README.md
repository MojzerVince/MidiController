# MIDI Key Controller
This Python script lets you configure your MIDI **up** and **down** buttons to use as channel rack changer (especially) in FL Studio!

## Installation
***First of all you need to have Python downloaded and installed!***

 1. Download the script file from GitHub
 2. Open cmd (Windows button + R) and navigate to the folder location you downloaded the file (navigation: cd {foldername})
 3. To install the **mido** library: `pip install mido`
 4. Open `main.py`

## Usage

 1. After opening the file, select a MIDI port available
 2. Press the *up* and *down* controller buttons on your MIDI Device (if nothing happens, restart the program and use another available MIDI port!)
 3. If the above written was successful then it's working!

If you got an error saying: `error creating Windows MM MIDI input port.`

 - You probably already using that port in FL Studio
 - You probably already have a script running

To solve these, please open an unused MIDI port!

## What to expect in the future:

 - Better menu navigation
 - More key support
 - Easy port change

## Contact

 - Email: **mojzerka@gmail.com**
 - Discord: **mojzi1969**

Made by: **Vince Mojzer**
