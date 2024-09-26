# TODO: FIX THE FUCKING KEYBOARD MODULE DOESN'T WORK
import globals
import filesHandler
from game import Game
import utils
from utils import clear_console

addition_game = Game("a")
subtraction_game = Game("s")
multiplication_game = Game("m")
division_game = Game("d")
random_game = Game("r")


def get_user_name():
    clear_console()
    while len(globals.username) < 1:
        globals.username = utils.get_user_input("Enter your name : ", False)


def show_games_played():
    with open(globals.GAMES_PLAYED_PATH, "r") as f:
        data = f.readlines()
        for i in data:
            print(i)


def settings():
    is_cheat_symbol = "*" if globals.is_cheat_enabled else "-"

    print(f"[1] Cheat Mode ({is_cheat_symbol})")
    print(f"[2] Division Round ({globals.division_round})")
    print(f"[3] Change Username ({globals.username})")
    print("[0] Exit")

    chose = utils.get_user_input("Choose : ")

    match chose:
        case 1:
            globals.is_cheat_enabled = not globals.is_cheat_enabled
        case 2:
            division_round_input = utils.get_user_input(
                "Enter Division Round Amount : "
            )
            if division_round_input > 0:
                if division_round_input < 5:
                    globals.division_round = division_round_input
                    print(globals.division_round)
                else:
                    print("Divsion round can't be >= 5")

            else:
                print("Enter a value > 1")
        case 3:
            globals.username = ""
            get_user_name()

    if chose != 0:
        settings()


running = True


def main_menu_text():
    print("[1] Addition Game")
    print("[2] Subtraction Game")
    print("[3] Multiplication Game")
    print("[4] Division Game")
    print("[5] Random Game")
    print("[6] Settings")
    print("[7] History")
    print("[8] Credits")
    print("[0] Exit")


def game_chooser():
    global running
    chose = int(utils.get_user_input("> ", True))
    clear_console()
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
            random_game.start_game()
        case 6:
            settings()
        case 7:
            show_games_played()
        case 8:
            print("Made with <3 by Hazem")
        case 0:
            running = False
        case _:
            running = False


def main_menu():
    clear_console()
    print("Welcome to math game, please choose a game")
    while running:
        main_menu_text()
        game_chooser()
        utils.press_to_continue()
        clear_console()


def main():
    get_user_name()
    filesHandler.init()
    main_menu()


if __name__ == "__main__":
    main()
