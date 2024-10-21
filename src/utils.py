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
    sleep(0.1)
    input("Press any key to continue ...")


def clear_console():
    if current_os() == "Windows":
        system("cls")
    elif current_os() == "Linux":
        system("clear")


def colored_text(text, color=Colors.LIGHT_WHITE):
    return f"{color}{text}{Colors.LIGHT_WHITE}"


def open_file_dialog() -> str:
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
