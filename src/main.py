import globals
import filesHandler
from game import Game
import utils
from utils import clear_console, colored_text
from colors import Colors

print(colored_text("", Colors.LIGHT_WHITE), end="")
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


def update_division_round():
    while True:
        division_round_input = utils.get_user_input(
            "Enter Division Round Amount (1-5): ", True
        )
        if 1 <= division_round_input < 5:
            globals.division_round = int(division_round_input)
            break
        else:
            print(
                f"{Colors.RED}Invalid value. Please enter a value between 1 and 5.{Colors.LIGHT_WHITE}"
            )


def settings():
    is_cheat_symbol = (
        colored_text("*", Colors.GREEN) if globals.is_cheat_enabled else "-"
    )

    print(f"[1] Cheat Mode ({is_cheat_symbol})")
    print(f"[2] Division Round ({globals.division_round})")
    print(f"[3] Change Username ({globals.username})")
    print("[0] Exit")

    settings_chose = utils.get_user_input("Choose : ")
    match settings_chose:
        case 1:
            globals.is_cheat_enabled = not globals.is_cheat_enabled
        case 2:
            update_division_round()
        case 3:
            globals.username = ""
            get_user_name()

    if settings_chose != 0:
        clear_console()
        settings()


def main_menu_text():
    print(colored_text("[1] Addition Game", Colors.CYAN))
    print(colored_text("[2] Subtraction Game", Colors.LIGHT_PURPLE))
    print(colored_text("[3] Multiplication Game", Colors.BROWN))
    print(colored_text("[4] Division Game", Colors.LIGHT_RED))
    print(colored_text("[5] Random Game", Colors.PURPLE))
    print(colored_text("[6] Settings", Colors.DARK_GRAY))
    print(colored_text("[7] History", Colors.LIGHT_GREEN))
    print(colored_text("[8] Credits", Colors.LIGHT_CYAN))
    print(colored_text("[0] Exit", Colors.LIGHT_WHITE))


running = True


def game_chooser():
    global running
    main_chose = int(utils.get_user_input("> ", True))
    clear_console()
    match main_chose:
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
            print(colored_text("Made with <3 by Hazem", Colors.LIGHT_RED))
        case 0:
            running = False
        case _:
            running = False


def main_menu():
    clear_console()
    print(colored_text("Welcome to math game, please choose a game", Colors.YELLOW))
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

print(colored_text("", Colors.LIGHT_WHITE), end="")
