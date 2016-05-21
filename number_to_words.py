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
