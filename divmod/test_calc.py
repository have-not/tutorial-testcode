import unittest
from  calc import mydivmod

class TestCalc(unittest.TestCase):

    def test_第1引数を第2引数で割り算する(self):
        self.assertEqual(mydivmod(3, 2), (1, 1))

    def test_ゼロ除算する(self):
        self.assertEqual(mydivmod(3, 0), (0, 0))

    def test_負数の剰余を計算するな(self):
        self.assertEqual(mydivmod(1, -2), (-1, -1))

if __name__ == '__main__':
    unittest.main()
