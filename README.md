<!-- Language: en -->

# Cool Math Game π

Cool Math Game is an engaging math-based game designed to challenge your arithmetic skills while providing fun and excitement.

## Features

- **Dynamic Difficulty**: The game increases in difficulty the more you play it
- **Saving System**: Your progress and streaks are saved
- **Modes**: Addition, Subtraction, Multiplication, Division and Random
- **Colorful Console**: Not a boring console.
- **Lightweight**: The game uses Maximum 12.2MB of ram.

## Requirements To Build

- Python 3.x (no external libraries used)

## How To Build

### Method 1: ".bat/.sh"

1. Clone the repo: `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`
2. Navigate to the repository folder.
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
   pyinstaller --noconfirm --onefile --console --icon "..\ico.ico" --name "Cool Math Game" --clean --add-data "game.py;." --add-data "filesHandler.py;." --add-data "colors.py;." --add-data "globals.py;." --add-data "utils.py;." "main.py"
   ```

   **Linux**:

   ```bash
   pyinstaller --noconfirm --onefile --console --icon="ico.ico" --name="Cool Math Game" --clean --add-data="src/game.py:." --add-data="src/filesHandler.py:." --add-data="src/colors.py:." --add-data="src/globals.py:." --add-data="src/utils.py:." src/main.py
   ```
