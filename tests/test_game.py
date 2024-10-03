from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            new_game = Game()

            grid = new_game.grid

            assert len(grid) == 9
            assert type(grid) == list
            for letter in grid:
                assert letter in string.ascii_uppercase
            # teardown
            pass

    def test_is_valid(self):

        new_game = Game()
        test_grid = "ABEIOVET"
        test_word_one = "BET"
        test_word_two = "BEET"

        new_game.grid = list(test_grid)

        assert new_game.is_valid(test_word_one) == True
        assert new_game.is_valid(test_word_two) == True


    def test_is_invalid(self):

        new_game = Game()
        test_grid = "ABEIOVET"
        test_word_three = "BATTER"

        new_game.grid = list(test_grid)

        assert new_game.is_valid(test_word_three) == False

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
