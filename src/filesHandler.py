import globals
import os


def init():
    # To make sure old "highscores" from previos versions work
    if os.path.exists("highscores.txt"):
        os.rename("highscores.txt", globals.GAMES_PLAYED_PATH)
    else:
        try:
            f = open(globals.GAMES_PLAYED_PATH, "x")
            f.close()
        except FileExistsError:
            pass


def add_games_played(game_type: str, streak: int):
    a_or_an = "a" if game_type[0].lower() != "a" else "an"
    if is_games_played_exist():
        with open(globals.GAMES_PLAYED_PATH, "a") as f:
            if globals.is_cheat_enabled:
                f.write(
                    f"{globals.username} Played {a_or_an} {game_type} Game WITH CHEATS Ended With {streak} Streak BY CHEATING\n"
                )
            else:
                f.write(
                    f"{globals.username} Played {a_or_an} {game_type} Game Ended With {streak} Streak\n"
                )


def is_games_played_exist():
    if os.path.isfile(globals.GAMES_PLAYED_PATH):
        return True
    else:
        init()
