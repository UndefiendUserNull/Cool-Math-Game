import globals
import filesHandler
from game import Game
import utils
from utils import clear_console
from colors import Colors

print(f"{Colors.LIGHT_WHITE}", end="")
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
    is_cheat_symbol = (
        f"{Colors.GREEN}*{Colors.LIGHT_WHITE}" if globals.is_cheat_enabled else "-"
    )

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
            print(round(9.9999, globals.division_round))

            if division_round_input > 0:
                if division_round_input < 5:
                    globals.division_round = int(division_round_input)
                else:
                    print(
                        f"{Colors.RED}Divsion round can't be >= 5{Colors.LIGHT_WHITE}"
                    )

            else:
                print(f"{Colors.RED}Enter a value > 1{Colors.LIGHT_WHITE}")
        case 3:
            globals.username = ""
            get_user_name()

    if chose != 0:
        clear_console()
        settings()


running = True


def main_menu_text():
    print(f"{Colors.CYAN}[1] Addition Game{Colors.LIGHT_WHITE}")
    print(f"{Colors.LIGHT_PURPLE}[2] Subtraction Game{Colors.LIGHT_WHITE}")
    print(f"{Colors.BROWN}[3] Multiplication Game{Colors.LIGHT_WHITE}")
    print(f"{Colors.LIGHT_RED}[4] Division Game{Colors.LIGHT_WHITE}")
    print(f"{Colors.PURPLE}[5] Random Game{Colors.LIGHT_WHITE}")
    print(f"{Colors.DARK_GRAY}[6] Settings{Colors.LIGHT_WHITE}")
    print(f"{Colors.LIGHT_GREEN}[7] History{Colors.LIGHT_WHITE}")
    print(f"{Colors.LIGHT_CYAN}[8] Credits{Colors.LIGHT_WHITE}")
    print(f"{Colors.LIGHT_WHITE}[0] Exit{Colors.LIGHT_WHITE}")


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
            print(f"Made with {Colors.LIGHT_RED}<3{Colors.LIGHT_WHITE} by Hazem")
        case 0:
            running = False
        case _:
            running = False


def main_menu():
    clear_console()
    print(
        f"{Colors.YELLOW}Welcome to math game, please choose a game{Colors.LIGHT_WHITE}"
    )
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
