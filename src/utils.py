from time import sleep
from platform import system as current_os
from os import system
from colors import Colors


def get_user_input(
    prompt: str = "", float_it: bool = True, zero_on_error: bool = False
) -> str | int:
    stuck = True
    while stuck:
        try:
            if float_it:
                return float(input(prompt))
            else:
                return input(prompt)
        except ValueError:
            if not zero_on_error:
                print("Enter a valid input")
            else:
                return 0
    return 0


def press_to_continue():
    sleep(0.3)
    input("Press any key to continue ...")


def clear_console():
    if current_os() == "Windows":
        system("cls")
    elif current_os() == "Linux":
        system("clear")


def colored_text(text, color):
    return f"{color}{text}{Colors.LIGHT_WHITE}"
