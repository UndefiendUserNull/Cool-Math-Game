import globals
import filesHandler
from game import Game
import utils
from utils import clear_console, print_colored_text
from colors import Colors

utils.reset_colors()
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
            "Enter Division Round Amount (1-4): ", int_it=True
        )
        if 1 <= division_round_input < 5:
            globals.division_round = division_round_input
            break
        else:
            print_colored_text(
                "Invalid value. Please enter a value between 1 and 4.", Colors.RED
            )


def update_clear_after_correct_ansewrs(new_value: int):
    globals.correct_answers_clear = new_value


def export_settings():
    filesHandler.export_settings()

    print_colored_text(
        f"Settings Exported ({globals.exported_settings_path})", Colors.GREEN
    )

    utils.press_to_continue()


def import_settings():
    try:
        filesHandler.import_settings()
    except IndexError:
        input(
            utils.colored_text(
                "Not A Settings File, Press Enter To Continue ...", Colors.RED
            )
        )
    except ValueError:
        input(
            utils.colored_text(
                "Broken Save File, Press Enter To Continue ...", Colors.RED
            )
        )


def settings():
    is_cheat_symbol = (
        utils.colored_text("*", Colors.GREEN)
        if globals.is_cheat_enabled
        else utils.colored_text("-", Colors.RED)
    )

    print(f"[1] Cheat Mode ({is_cheat_symbol})")
    print(f"[2] Division Round ({globals.division_round})")
    print(f"[3] Change Username ({globals.username})")
    print(f"[4] Clear Console After ({globals.correct_answers_clear}) Correct Answers")
    print("[5] Import Settings")
    print("[6] Export Settings")
    print("[7] Reset Settings")
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
        case 4:
            update_clear_after_correct_ansewrs(
                utils.get_user_input("Enter the new value : ", int_it=True)
            )
        case 5:
            import_settings()
        case 6:
            export_settings()
        case 7:
            filesHandler.import_default_settings()

    if settings_chose != 0:
        clear_console()
        settings()


def print_menu():
    print_colored_text("[1] Addition Game", Colors.CYAN)
    print_colored_text("[2] Subtraction Game", Colors.LIGHT_PURPLE)
    print_colored_text("[3] Multiplication Game", Colors.BROWN)
    print_colored_text("[4] Division Game", Colors.LIGHT_RED)
    print_colored_text("[5] Random Game", Colors.PURPLE)
    print_colored_text("[6] Settings", Colors.DARK_GRAY)
    print_colored_text("[7] History", Colors.LIGHT_GREEN)
    print_colored_text("[8] Credits", Colors.LIGHT_CYAN)
    print_colored_text("[0] Exit", Colors.LIGHT_WHITE)


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
            # print(utils.colored_text("Made with <3 ", Colors.LIGHT_RED + " by Hazem"))
            print(f"Made with {Colors.LIGHT_RED}<3{Colors.LIGHT_WHITE} by Hazem")
        case 0:
            running = False
        case _:
            running = False


def main_menu():
    clear_console()
    print_colored_text("Welcome to math game, please choose a game", Colors.YELLOW)

    while running:
        print_menu()
        game_chooser()
        utils.press_to_continue()
        clear_console()


def main():
    clear_console()
    filesHandler.init()
    if len(globals.username) < 1:
        get_user_name()
    main_menu()


if __name__ == "__main__":
    main()

utils.reset_colors()
