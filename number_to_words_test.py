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

    def test_eleven_to_nineteen(self):
        NUMBERS = {
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen'
        }
        self.assert_numbers_equal_to_strings(NUMBERS)

    def test_factors_of_ten(self):
        NUMBERS = {
            10: 'ten', 100: 'one hundred', 1000: 'one thousand',
            10000: 'ten thousand', 100000: 'one hundred thousand',
            1000000: 'one million', 10000000: 'ten million',
            100000000: 'one hundred million'
        }
        self.assert_numbers_equal_to_strings(NUMBERS)

    def test_tens(self):
        NUMBERS = {
            20: 'twenty', 29: 'twenty nine', 30: 'thirty', 38: 'thirty eight',
            40: 'fourty', 47: 'fourty seven', 50: 'fifty', 56: 'fifty six',
            60: 'sixty', 65: 'sixty five', 70: 'seventy', 74: 'seventy four',
            80: 'eighty', 83: 'eighty three', 90: 'ninety', 92: 'ninety two'
        }
        self.assert_numbers_equal_to_strings(NUMBERS)

    def test_zero_hundreds(self):
        NUMBERS = {
            12000: 'twelve thousand',
            123000: 'one hundred and twenty three thousand',
            1234000: 'one million two hundred and thirty four thousand',
            12345000: 'twelve million three hundred and fourty five ' +
                      'thousand',
            123456000: 'one hundred and twenty three million four hundred ' +
                       'and fifty six thousand'
        }
        self.assert_numbers_equal_to_strings(NUMBERS)

    def assert_numbers_equal_to_strings(self, numbers):
        for number, string in numbers.iteritems():
            self.assertEqual(string, self.n2w.convert(number))

if __name__ == '__main__':
    unittest.main()
