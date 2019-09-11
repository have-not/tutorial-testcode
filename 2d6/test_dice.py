import unittest
from dice import d6, roll_2d

class TestDice(unittest.TestCase):

    def test_6面ダイスを振る(self):
        self.assertIn(d6(), [1, 2, 3, 4, 5, 6])

    def test_ダイスを2つの合計値を出す(self):
        self.assertEqual(roll_2d(1, 6), 7)

if __name__ == '__main__':
    unittest.main()
