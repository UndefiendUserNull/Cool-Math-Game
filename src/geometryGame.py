from enum import Enum
import globals
from colors import Colors
from random import randint
from filesHandler import add_games_played
from utils import clear_console, get_user_input, print_colored_text
import math


class GGameType(Enum):
    PYTHAGOREAN = "p"


class GGame:
    min_x = 0
    max_x = 10

    min_y = 1
    max_y = 10

    rand_x = 0
    rand_y = 1

    streak = 0

    ui = 0

    def __init__(self, game_type):
        self.game_type = game_type

    def print_question(self):
        clear_console()
        print(
            f"""
      X |\\
        | \\
        |  \\
        |   \\
        |    \\
        |     \\
        |      \\
      Y |_______\\ Z
    
    
        XY = {self.rand_x}cm
        YZ = {self.rand_y}cm
        XY = ?
        """
        )

    def get_answer_rounded(self) -> float:
        return round(math.sqrt(self.rand_x**2 + self.rand_y**2), globals.division_round)

    def get_game_type_string(self) -> str:
        game_types = {
            GGameType.PYTHAGOREAN.value: "Pythagorean",
        }
        return game_types.get(self.game_type, "Not Found")

    def reset_values(self):
        self.min_x = 0
        self.max_x = 10
        self.min_y = 1
        self.max_y = 10
        self.rand_x = 0
        self.rand_y = 1
        self.streak = 0
        self.ui = 0

    def increase_difficulty_and_streak(self):
        self.min_x += 1
        self.max_x += 1

        self.min_y += 1
        self.max_y += 1

        self.streak += 1

    def start_game(self):
        running = True
        while running:
            self.rand_x = randint(self.min_x, self.max_x)
            self.rand_y = randint(self.min_y, self.max_y)
            self.print_question()
            if globals.is_cheat_enabled:
                print(self.get_answer_rounded())
            self.ui = get_user_input()

            if self.ui == self.get_answer_rounded():
                print_colored_text("Correct !", Colors.LIGHT_GREEN)
                self.increase_difficulty_and_streak()
                clear_console()

            else:
                add_games_played(self.get_game_type_string(), self.streak)

                print_colored_text(
                    f"Wrong !, correct answer is {self.get_answer_rounded()}",
                    Colors.LIGHT_RED,
                )

                print_colored_text(
                    f"\nYou had a great streak of {self.streak}", Colors.BLUE
                )

                self.reset_values()
                running = False
