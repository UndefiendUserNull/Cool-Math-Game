from time import sleep
from platform import system as current_os
from os import system, getcwd
from colors import Colors
import tkinter as tk
from tkinter import filedialog


def get_user_input(
    prompt: str = "",
    float_it: bool = True,
    zero_on_error: bool = False,
    int_it: bool = False,
) -> str | int:
    """Gets the user input with error handling

    Args:
        prompt (str, optional): _description_. The text that will appear when getting the input. Defaults to "".
        float_it (bool, optional): _description_. Converts the user input to a float. Defaults to True.
        zero_on_error (bool, optional): _description_. instead of trying to get the input again when an error happens it returns 0. Defaults to False.
        int_it (bool, optional): _description_. Converts the user input to an int. Defaults to False.

    Returns:
        str | int
    """
    stuck = True
    while stuck:
        try:
            if float_it and not int_it:
                return float(input(prompt))
            elif int_it:
                float_it = False
                return int(input(prompt))
            else:
                return input(prompt)
        except ValueError:
            if not zero_on_error:
                print("Enter a valid input")
            else:
                return 0
    return 0


def press_to_continue():
    # To prevent enter spamming, maybe removed
    sleep(0.1)
    input("Press any key to continue ...")


def clear_console():
    """Clears the console based on the OS"""
    if current_os() == "Windows":
        system("cls")
    elif current_os() == "Linux":
        system("clear")


def colored_text(text: str, color: Colors) -> str:
    """Returns a colored text, doesn't print

    Args:
        text (str): The text it self
        color (Colors): The color from the Colors

    Returns:
        str
    """
    return f"{color}{text}{Colors.LIGHT_WHITE}"


def print_colored_text(text: str, color: Colors):
    """Prints a colored text with the given text and color

    Args:
        text (str): The text it self
        color (Colors): The color from the Colors
    """
    print(f"{color}{text}{Colors.LIGHT_WHITE}")


def reset_colors():
    print(f"{Colors.LIGHT_WHITE}", end="")


def get_settings_with_file_dialog() -> str:
    """Opens a tkinter file dialog to get the .pi settings

    Returns:
        str
    """
    root = tk.Tk()
    root.withdraw()

    try:
        root.iconbitmap("ico.ico")
    except:  # noqa
        pass

    pickedfiletypes = (("pi files", "*.pi"), ("pi files", "*.pi"))

    file_path = filedialog.askopenfilename(
        initialdir=getcwd(), title="Pick Save File", filetypes=pickedfiletypes
    )
    return file_path


def open_custom_file_dialog() -> str:
    """Custom file dialog that can be used with anything

    Returns:
        str
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=getcwd(), title="Pick")
    return file_path
