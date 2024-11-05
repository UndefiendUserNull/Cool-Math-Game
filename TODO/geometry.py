# This for other things that may be added
# TODO: Pythagorean


import math
import random
import os


def clear_console():
    os.system("cls")


clear_console()
min_x = 4
max_x = 1000


# region Sqrt
def get_random(range_x, range_y):
    number = 0.1
    while True:
        sqrted_number = math.sqrt(number)
        if not sqrted_number.is_integer():
            number = random.randint(range_x, range_y)
        else:
            break
    return number


def get_answer(random_given):
    random_num = math.sqrt(random_given)
    return random_num


def get_sqrt_question(random_number):
    return f"√{random_number} = ?"


# endregion


def get_answer_rounded(leg1, leg2):
    return round(math.sqrt(leg1**2 + leg2**2), 2)


def print_question(leg1, leg2):
    print(
        f"""
        \\
      x |\\
        | \\
        |  \\
        |   \\
        |    \\
        |     \\
      y |______\\ z
      
    xy = {leg1}cm
    yz = {leg2}cm
    xy = ?
      """
    )


leg1 = random.randint(1, 25)
leg2 = random.randint(1, 25)
hypotenuse = get_answer_rounded(leg1, leg2)

print_question(leg1, leg2)
print(hypotenuse)
