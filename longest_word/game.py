import string
import random

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""

        for input_char in word:
            input_char_in_grid = False
            for grid_char in self.grid:
                if input_char == grid_char:
                    input_char_in_grid = True
            if input_char_in_grid == False:
                return False
        return True

    # just adding a comment
