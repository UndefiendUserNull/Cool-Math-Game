# This for other things that may be added
# TODO: Pythagorean

import math
import random

min_x = 4
max_x = 1000


def get_random():
    number = 0.1
    while True:
        sqrted_number = math.sqrt(number)
        if not sqrted_number.is_integer():
            number = random.randint(min_x, max_x)
        else:
            break
    return number


random_number = get_random()


def get_answer(random_given):
    random_num = math.sqrt(random_given)
    return random_num


def get_sqrt_question():
    return f"√{random_number} = ?"


print(f"{get_sqrt_question()} {get_answer(random_number)}")
