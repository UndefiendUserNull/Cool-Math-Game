#!/bin/bash
pyinstaller --noconfirm \
    --onefile \
    --console \
    --icon="ico.ico" \
    --name="Cool Math Game" \
    --clean \
    --add-data="src/game.py:." \
    --add-data="src/filesHandler.py:." \
    --add-data="src/colors.py:." \
    --add-data="src/globals.py:." \
    --add-data="src/utils.py:." \
    src/main.py
