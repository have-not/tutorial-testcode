import unittest
from greeting import get_greet_msg

class TestGreeting(unittest.TestCase):
    def test_helloという文字列を返す(self):
        self.assertEqual(get_greet_msg(), "hello!")

    def test_6の場合(self):
        self.assertEqual(get_greet_msg(6), "hello!")
        
    def test_7の場合(self):
        self.assertEqual(get_greet_msg(7), "good morning!")
        
    def test_9の場合(self):
        self.assertEqual(get_greet_msg(9), "good morning!")
        
    def test_10の場合(self):
        self.assertEqual(get_greet_msg(10), "hello!")

if __name__ == '__main__':
    unittest.main()
