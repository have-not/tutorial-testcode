import unittest
from greeting import getGreetMsg

class TestGreeting(unittest.TestCase):
    def test_helloという文字列を返す(self):
        self.assertEqual(getGreetMsg(), "hello!")

    def test_6の場合(self):
        self.assertEqual(getGreetMsg(6), "hello!")
        
    def test_7の場合(self):
        self.assertEqual(getGreetMsg(7), "good morning!")
        
    def test_9の場合(self):
        self.assertEqual(getGreetMsg(9), "good morning!")
        
    def test_10の場合(self):
        self.assertEqual(getGreetMsg(10), "hello!")

if __name__ == '__main__':
    unittest.main()
