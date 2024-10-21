"""The place where user settings are stored"""

username: str = ""
is_cheat_enabled: bool = False
# round(0.999, division_round)
division_round: int = 1
GAMES_PLAYED_PATH: str = "History.pi"
exported_settings_path: str = f"{username}'s Settings.pi"
correct_answers_clear: int = 5


# Default Settings DON'T TOUCH

D_USERNAME: str = ""
D_IS_CHEAT_ENABLED: bool = False
D_DIVISION_ROUND: int = 1
D_GAMES_PLAYED_PATH: str = "History.pi"
D_EXPORTED_SETTINGS_PATH: str = f"{username}'s Settings.pi"
D_CORRECT_ANSWERS_CLEAR: int = 5
