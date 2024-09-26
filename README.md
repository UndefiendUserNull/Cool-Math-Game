# Cool-Math-Game

A simple Math Game i made

## Features

- The game gets harder the more you play
- Saving system to store your streaks
- Multiple modes

## Requirements To Build

I didn't use any outside libraries, only Pyinstaller (You could use auto-py-to-exe)

## Building Command

pyinstaller --noconfirm --onedir --console --name "Cool Math Game" --add-data "globals.py;." --add-data "game.py;." --add-data "filesHandler.py;." --add-data "utils.py;." "main.py"
