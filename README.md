<!-- Language: en -->

[عربي](https://github.com/UndefiendUserNull/Cool-Math-Game/tree/main/docs/ar)

# Cool Math Game π

Cool Math Game is an engaging math-based game designed to challenge your arithmetic skills while providing fun and excitement.

## Features

- **Dynamic Difficulty**: The game increases in difficulty the more you play it
- **Saving System**: Your progress and streaks are saved
- **Modes**: Addition, Subtraction, Multiplication, Division, Random and Pythagorean
- **Colorful Console**: Not a boring console.
- **Lightweight**: The game uses Maximum 12.2MB of ram.

## Requirements To Build

- Python 3.x (no external libraries used)
- Pyinstaller

## How To Build

### Method 1: ".bat/.sh"

1. Clone the repo: `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`
2. Install pyinstaller `pip install pyinstaller`
3. For **Windows**, run the `build.bat`.
4. For **Linux**, run the `build-linux.sh`.

### Method 2: "auto-py-to-exe"

1. Install auto-py-to-exe: `pip install auto-py-to-exe`.
2. Clone the repo: `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`.
3. Open a terminal inside the "src" folder and type `auto-py-to-exe`.
4. Expand the settings tab.
5. Click `Import Config From JSON File` and select the `build-config.json` file inside the repo.
6. Hit `CONVERT .PY TO .EXE`.

### Method 3: "pyinstaller"

1. Install pyinstaller: `pip install pyinstaller`.
2. Clone the repo: `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`.
3. Open a terminal inside the "src" folder and paste the following command:

   **Windows**:

   ```bash
   pyinstaller --noconfirm --onefile --console --name "Cool Math Game" --add-data "colors.py;." --add-data "filesHandler.py;." --add-data "game.py;." --add-data "geometryGame.py;." --add-data "globals.py;." --add-data "main.py;." --add-data "utils.py;."  "src\main.py"
   ```

   **Linux**:

   ```bash
   pyinstaller --noconfirm --onefile --console --icon "./ico.ico" --name "Cool Math Game" --add-data "colors.py:." --add-data "filesHandler.py:." --add-data "game.py:." --add-data "geometryGame.py:." --add-data "globals.py:." --add-data "main.py:." --add-data "utils.py:." "main.py"
   ```

## Screenshots

![SCREENSHOT1](https://i.imgur.com/a7iSmvW.png?raw=true "Screenshot")
![SCREENSHOT2](https://i.imgur.com/ZQvIrIh.png?raw=true "Screenshot2")
![SCREENSHOT2](https://i.imgur.com/Agr8bJ3.png?raw=true "Screenshot3")
