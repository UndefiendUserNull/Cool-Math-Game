import globals
import os

def init():
    try:
        f = open(globals.high_scores_path, 'x')
        f.close()
    except FileExistsError:
        pass


def add_highscore(game_type: str, streak: int):
    a_or_an = 'a' if game_type[0].lower() != 'a' else 'an'
    if is_high_score_exist():
        with open(globals.high_scores_path, 'a') as f:
            if globals.is_cheat_enabled:
                f.write(f"{globals.username} Played {a_or_an} {game_type} Game WITH CHEATS Ended With {streak} Streak BY CHEATING\n")
            else:
                f.write(f"{globals.username} Played {a_or_an} {game_type} Game Ended With {streak} Streak\n")
    else:
        return

def is_high_score_exist():
    if os.path.isfile(globals.high_scores_path):
        return True
    else:
        init()
