@staticmethod
def get_user_input(
    prompt: str = "", is_int: bool = True, zero_on_error: bool = False
) -> str | int:
    """_summary_

    Args:
        prompt (str, optional): The message. Defaults to ""
        is_int (bool, optional): Return the int value of the input. Defaults to True.
        zero_on_error (bool, optional): If there's an error return -1, use when the input is not stored. Defaults to False.

    Returns:
        _type_: String | Int
    """
    stuck = True
    while stuck:
        try:
            if is_int:
                return int(input(prompt))
            else:
                return input(prompt)
        except ValueError:
            if not zero_on_error:
                print("Enter a valid input")
            else:
                return -1
    return -1
