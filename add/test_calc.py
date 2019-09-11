import unittest
import calc
from calc import MyException

class TestCalc(unittest.TestCase):

    def test_2つの整数の合計値を出す(self):
        self.assertEqual(calc.add(1, -2), -1)

    def test_整数と小数の合計値を出す(self):
        with self.assertRaises(MyException):
            calc.add(1, 0.1)

if __name__ == '__main__':
    unittest.main()
