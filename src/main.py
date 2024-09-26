import globals
import filesHandler
from game import Game
import utils

addition_game = Game("a")
subtraction_game = Game("s")
multiplication_game = Game("m")
division_game = Game("d")


def get_user_name():
    while len(globals.username) < 1:
        globals.username = utils.get_user_input("Enter your name : ", False)


def show_high_scores():
    with open(globals.high_scores_path, "r") as f:
        data = f.readlines()
        for i in data:
            print(i)


def settings():
    is_cheat_symbol = "*" if globals.is_cheat_enabled else "-"

    print(f"[1] Cheat Mode ({is_cheat_symbol})")
    print(f"[2] Division Round ({globals.division_round})")
    print("[0] Exit")

    chose = utils.get_user_input("Choose : ")

    if chose == 1:
        globals.is_cheat_enabled = not globals.is_cheat_enabled

    elif chose == 2:
        division_round_input = utils.get_user_input("Enter Division Round Amount : ")
        if division_round_input > 0:
            if division_round_input < 5:
                globals.division_round = division_round_input
                print(globals.division_round)

        else:
            print("Enter a value bigger than 1")

    if chose != 0:
        settings()


running = True


def main_menu_text():
    print("[1] Addition Game")
    print("[2] Subtraction Game")
    print("[3] Multiplication Game")
    print("[4] Division Game")
    print("[5] Settings")
    print("[6] Highscore")
    print("[7] Credits")
    print("[0] Exit")


def game_chooser():
    global running
    chose = utils.get_user_input("> ")
    match chose:
        case 1:
            addition_game.start_game()
        case 2:
            subtraction_game.start_game()
        case 3:
            multiplication_game.start_game()
        case 4:
            division_game.start_game()
        case 5:
            settings()
        case 6:
            show_high_scores()
        case 7:
            print("Made with ♥ by Hazem")
        case 0:
            running = False
        case _:
            running = False


def main_menu():
    print("Welcome to math game, please choose a game")
    while running:
        main_menu_text()
        game_chooser()
        utils.get_user_input("Press Enter To Continue ...", False, True)


def main():
    get_user_name()
    filesHandler.init()
    main_menu()


if __name__ == "__main__":
    main()
