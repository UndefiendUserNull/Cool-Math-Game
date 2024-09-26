import time
import platform
import os


def get_user_input(
    prompt: str = "", float_it: bool = True, zero_on_error: bool = False
) -> str | int:
    """_summary_

    Args:
        prompt (str, optional): The message. Defaults to ""
        float_it (bool, optional): Return the int value of the input. Defaults to True.
        zero_on_error (bool, optional): If there's an error return -1, use when the input is not stored. Defaults to False.

    Returns:
        _type_: String | Int
    """
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
                return -1
    return -1


def press_to_continue():
    time.sleep(0.5)
    input("Press any key to continue ...")


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("reset")
