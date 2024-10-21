# Cool-Math-Game π

A simple Math Game i made

## Features

- The game gets harder the more you play
- Saving system to store your streaks
- Multiple Modes
- Colorful Console Based 
- Very lightweight

## Requirements To Build

I didn't use any outside libraries

## How To Build

### Method 1 "auto-py-to-exe"

Install auto-py-to-exe `pip install auto-py-to-exe`

Clone the repo `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`

Open the cmd inside the "src" folder and type `auto-py-to-exe`

Expand the settings tab

![SCREENSHOT2](https://i.imgur.com/q81ORJO.png "s")

Click `Import Config From JSON File`

Then select the `build-config.json` file that's inside the repo

After that hit `CONVERT .PY TO .EXE`

### Method 2 "pyinstaller"

Install auto-py-to-exe `pip install pyinstaller`

Clone the repo `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`

Open the cmd inside the "src" folder and paste this long command

`pyinstaller --noconfirm --onefile --console --icon "ico.ico" --name "Cool Math Game" --upx-dir "upx" --clean --add-data "game.py;." --add-data "filesHandler.py;." --add-data "colors.py;." --add-data "globals.py;." --add-data "utils.py;."  "main.py"`

## Some screenshots

![SCREENSHOT1](https://i.imgur.com/a7iSmvW.png?raw=true "Screenshot")
![SCREENSHOT2](https://i.imgur.com/ZQvIrIh.png?raw=true "Screenshot2")
![SCREENSHOT2](https://i.imgur.com/Agr8bJ3.png?raw=true "Screenshot3")
