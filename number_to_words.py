class NumberToWords(object):
    """
    Class for converting positive integer values to a textual representation
    of the submitted number for value of 0 up to 999999999.

    Example:
        >>> from number_to_words import NumberToWords
        >>> n2w = NumberToWords()
        >>> n2w.convert(123)
        'one hundred and twenty three'
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
        try:
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
                for group in zero_filled_groups:
                    index = zero_filled_groups.index(group)
                    suffix = self.LARGE_NUMBERS[index]
                    is_and_required = False
                    if index is 0 and len(zero_filled_groups) > 1:
                        is_and_required = True
                    number_as_words = " ".join(
                        self._number_to_word_list(group, is_and_required,
                                                  suffix))
                    if len(number_as_words) > 0:
                        sentence = "{0} {1}".format(number_as_words, sentence)
                    # set this group to None so as to not set a false `index`
                    # for subsequent groups where `number` has multiple
                    # identical groups
                    zero_filled_groups[index] = None
            return sentence.rstrip()
        except (IndexError, ValueError):
            raise ValueError(self.EXCEPTION_STRING)

    def _number_to_word_list(self, number_string, is_and_required,
                             suffix=None):
        """
        Take a 3 digit string representation of an integer and convert it to a
        textual representation with an optional suffix.
        """

        words = []
        hundreds, tens, units = [int(n) for n in list(number_string)]
        total = sum([hundreds, tens, units])
        if hundreds is not 0:
            string = self.SMALL_NUMBERS[hundreds]
            words.append("{0} hundred".format(string))
            if tens is not 0 or units is not 0:
                words.append("and")
        elif hundreds is 0 and is_and_required and total is not 0:
            words.append("and")
        if tens is 1:
            string = self.SMALL_NUMBERS[int("{0}{1}".format(tens, units))]
            words.append("{0}".format(string))
        else:
            if tens is not 0:
                string = self.TENS[tens]
                words.append("{0}".format(string))
            if units is not 0:
                string = self.SMALL_NUMBERS[units]
                words.append("{0}".format(string))

        if suffix and total is not 0:
            words.append(suffix)

        return words

if __name__ == "__main__":
    n2w = NumberToWords()
    unique = set()

    def fib():
        x, y = 0, 1
        yield x
        yield y

        while True:
            x, y = y, x + y
            yield y

    for num in fib():
        if num > n2w.MAX:
            break
        unique.add(num)

    print n2w.__doc__
    print """
Some example conversions from number to words
=============================================\n"""

    for num in sorted(list(unique)):
        print "{0} : {1}".format(format(num, ','), n2w.convert(num))
    print "{0} : {1}".format(format(n2w.MAX, ','), n2w.convert(n2w.MAX))
