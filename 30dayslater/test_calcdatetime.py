import unittest
from calcdatetime import thirtyDaysLater
from datetime import datetime

class TestCalcdatetime(unittest.TestCase):

    def test_30日後の日数(self):
        testdate = datetime.strptime('2019/09/11', '%Y/%m/%d')
        self.assertIn(thirtyDaysLater(testdate), r"2019/10/11")

if __name__ == '__main__':
    unittest.main()
