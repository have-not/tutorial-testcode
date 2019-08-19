import unittest
import programming as pg


class TestHelloWorld(unittest.TestCase):

    def test_helloworld(self):
        self.assertEqual('HelloWorld!', pg.helloworld())


if __name__ == '__main__':
    unittest.main()
