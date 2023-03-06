import unittest
import Game


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        print('Starting a Test')

    def test_input (self):
        answer = 5
        guess = 5
        result = Game.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_wrong(self):
        result = Game.run_guess(5, 6)
        self.assertFalse(result)

    def test_input_out_of_range(self):
        result = Game.run_guess(11, 6)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = Game.run_guess('1', 6)
        self.assertIsInstance(result, TypeError)


if __name__ == '__main__':
    unittest.main()
