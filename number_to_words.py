class NumberToWords(object):
    """
    Class for converting positive integer values to a textual representation
    of the submitted number for value of 0 up to 999999999.
    """

    MAX = 999999999
    SMALL_NUMBERS = ['', 'one', 'two', 'three', 'four', 'five', 'six',
                     'seven', 'eight', 'nine', 'ten', 'eleven',
                     'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                     'seventeen', 'eighteen', 'nineteen']
    TENS = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy',
            'eighty', 'ninety']
    LARGE_NUMBERS = ['', 'thousand', 'million']
    EXCEPTION_STRING = "This method expects positive integer values between " \
        + "0 and {0}".format(MAX)

    def convert(self, number):
        """
        Take an integer and return it converted to a textual representation.

        Args:
            number (int): The number to be converted.

        Returns:
            sentence (string): The textual representation of `number`.

        Raises:
            ValueError: If `number` is not a positive integer or is greater
                        than `MAX`.
        """

        if not isinstance(number, (int, long)):
            raise ValueError(self.EXCEPTION_STRING)
        sentence = ""
        if number is 0:
            sentence = "zero"
        else:
            # split number into a list of strings where each list item is
            # at most 3 character in length.
            groups = format(number, ',').split(',')

            # make sure each list item is exactly 3 characters long by
            # zero filling
            zero_filled_groups = []
            for group in groups:
                zero_filled_groups.append(group.zfill(3))

            # reverse the list of strings so that the list indexes of the
            # string representation of hundreds, thousands and million
            # match those of `LARGE_NUMBERS`
            zero_filled_groups.reverse()
        return sentence.rstrip()

    def _number_to_word_list(self, number_string, suffix=None):
        """
        Take a 3 digit string representation of an integer and convert it to a
        textual representation with an optional suffix.
        """

        words = []
        hundreds, tens, units = [int(n) for n in list(number_string)]

        if hundreds is not 0:
            string = self.SMALL_NUMBERS[hundreds]
            words.append("{0} hundred".format(string))
            if tens is not 0 or units is not 0:
                words.append("and")
        return words
