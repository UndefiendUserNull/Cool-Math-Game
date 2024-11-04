import utils
import globals
import os


def init():
    """
    tries to load the settings in the dir and creates a History.py if it doesn't exist
    """
    # To make sure old "highscores" from previos versions work
    settings_found = []
    for i in os.listdir(os.getcwd()):
        if i.endswith(".pi") and str(i) != "History.pi":
            settings_found.append(i)
    settings_found_count = len(settings_found)

    if settings_found_count > 1:
        for i in range(settings_found_count):
            print(f"[{i}] : {settings_found[i]}")
        ui = utils.get_user_input(
            "Multiple Saves Found Select One : ", False, int_it=True
        )
        if ui >= 0 and ui <= settings_found_count:
            try:
                import_settings(settings_found[int(ui)])
            except:  # noqa
                import_default_settings()
    elif settings_found_count > 0:
        import_settings(settings_found[0])
    if os.path.exists("highscores.txt"):
        os.rename("highscores.txt", globals.GAMES_PLAYED_PATH)
    else:
        try:
            f = open(globals.GAMES_PLAYED_PATH, "x")
            f.close()
        except FileExistsError:
            pass


def update_globals_username():
    globals.exported_settings_path = f"{globals.username}'s Settings.pi"


def export_settings():
    update_globals_username()
    with open(globals.exported_settings_path, "w") as f:
        f.write("")

    with open(globals.exported_settings_path, "a") as f:
        f.write(
            "# DON'T CHANGE THE ORDER OF THE SETTINGS OR REMOVE SPACES\\NEW LINES\n"
        )
        f.write(str(globals.username) + "\n")
        f.write(str(globals.is_cheat_enabled) + "\n")
        f.write(str(globals.division_round) + "\n")
        f.write(str(globals.correct_answers_clear) + "\n")


def read_settings(path="NONE") -> list:
    data = []
    if path == "NONE":
        try:
            with open(utils.get_settings_with_file_dialog(), "r") as f:
                for i in f.readlines():
                    if i.startswith("#"):
                        continue
                    data.append(i[: i.find("\\")])
        except FileNotFoundError:
            ...
    else:
        with open(path, "r") as f:
            for i in f.readlines():
                if i.startswith("#"):
                    continue
                data.append(i[: i.find("\\")])
    return data


def import_settings(path="NONE"):
    update_globals_username()
    read_data = read_settings() if path == "NONE" else read_settings(path)
    if int(read_data[2]) < 5:
        globals.division_round = int(read_data[2])
    else:
        raise ValueError("Division Round Is Bigger Than 4")
    globals.username = read_data[0]
    globals.is_cheat_enabled = bool(read_data[1])
    globals.correct_answers_clear = int(read_data[3])


def import_default_settings():
    globals.division_round = globals.D_DIVISION_ROUND
    globals.is_cheat_enabled = globals.D_IS_CHEAT_ENABLED
    globals.correct_answers_clear = globals.D_CORRECT_ANSWERS_CLEAR


def add_games_played(game_type: str, streak: int):
    """May Change When Adding geometry"""
    a_or_an = "a" if game_type[0].lower() != "a" else "an"
    if is_games_played_exist():
        with open(globals.GAMES_PLAYED_PATH, "a") as f:
            if globals.is_cheat_enabled:
                (
                    f.write(
                        f"{globals.username} Played {a_or_an} {game_type} Game WITH CHEATS Ended With {streak} Streak BY CHEATING\n"
                    )
                )
            else:
                (
                    f.write(
                        f"{globals.username} Played {a_or_an} {game_type} Game Ended With {streak} Streak\n"
                    )
                )


def is_games_played_exist():
    if os.path.isfile(globals.GAMES_PLAYED_PATH):
        return True
    else:
        init()
