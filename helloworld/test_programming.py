import unittest
import programming as pg

class TestHelloWorld(unittest.TestCase):

    def test_helloworld(self):
        self.assertEqual(pg.helloworld(), 'HelloWorld!')

if __name__ == '__main__':
    unittest.main()
