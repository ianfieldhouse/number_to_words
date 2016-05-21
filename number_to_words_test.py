import unittest
from number_to_words import NumberToWords


class TestNumberToWords(unittest.TestCase):
    def setUp(self):
        self.n2w = NumberToWords()

    def tearDown(self):
        self.n2w = None

    def test_zero_and_single_digits(self):
        NUMBERS = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
        }
        self.assert_numbers_equal_to_strings(NUMBERS)

    def assert_numbers_equal_to_strings(self, numbers):
        for number, string in numbers.iteritems():
            self.assertEqual(string, self.n2w.convert(number))

if __name__ == '__main__':
    unittest.main()
