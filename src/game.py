from enum import Enum
import globals
from colors import Colors
from random import randint
from filesHandler import add_games_played
from utils import clear_console, get_user_input, colored_text


class GameType(Enum):
    ADDITION = "a"
    SUBTRACTION = "s"
    MULTIPLICATION = "m"
    DIVISION = "d"
    RANDOM = "r"


class Game:
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

    def get_question(self, symbol):
        return f"{self.rand_x} {symbol} {self.rand_y} = ?"

    def get_result(self, symbol):
        return round(
            eval(f"{self.rand_x}{symbol}{self.rand_y}"),
            globals.division_round,
        )

    def get_symbol(self) -> str:
        symbols = {
            GameType.ADDITION.value: "+",
            GameType.SUBTRACTION.value: "-",
            GameType.MULTIPLICATION.value: "*",
            GameType.DIVISION.value: "/",
            GameType.RANDOM.value: ("+", "-", "*", "/")[randint(0, 3)],
        }
        return symbols.get(self.game_type, "+")

    def get_game_type_string(self) -> str:
        game_types = {
            GameType.ADDITION.value: "Addition",
            GameType.SUBTRACTION.value: "Subtraction",
            GameType.MULTIPLICATION.value: "Multiplication",
            GameType.DIVISION.value: "Division",
            GameType.RANDOM.value: "Random",
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
        correct_answers = 0
        while running:
            self.rand_x = randint(self.min_x, self.max_x)
            self.rand_y = randint(self.min_y, self.max_y)
            current_symbol = self.get_symbol()
            print(self.get_question(symbol=current_symbol))
            if globals.is_cheat_enabled:
                print(self.get_result(symbol=current_symbol))
            self.ui = get_user_input()

            if self.ui == self.get_result(symbol=current_symbol):
                print(colored_text("Correct !", Colors.LIGHT_GREEN))
                self.increase_difficulty_and_streak()
                correct_answers += 1
                if correct_answers >= globals.correct_answers_clear:
                    clear_console()
                    correct_answers = 0

            else:
                add_games_played(self.get_game_type_string(), self.streak)
                print(
                    colored_text(
                        f"Wrong !, correct answer is {self.get_result(symbol=current_symbol)}",
                        Colors.LIGHT_RED,
                    )
                )
                print(
                    colored_text(
                        f"\nYou had a great streak of {self.streak}", Colors.BLUE
                    )
                )
                self.reset_values()
                running = False
