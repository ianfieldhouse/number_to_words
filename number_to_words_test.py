import unittest
from number_to_words import NumberToWords


class TestNumberToWords(unittest.TestCase):
    def setUp(self):
        self.n2w = NumberToWords()

    def tearDown(self):
        self.n2w = None

if __name__ == '__main__':
    unittest.main()
