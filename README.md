#number_to_words.py

Class for converting positive integer values to a textual representation of the submitted number for value of 0 up to 999999999.

##Example usage
```
>>> from number_to_words import NumberToWords
>>> n2w = NumberToWords()
>>> n2w.convert(123)
'one hundred and twenty three'
```

##Examples
```
python number_to_words.py
```

##Tests
```
python -m unittest -v number_to_words_test
```
[![Build Status](https://travis-ci.org/ianfieldhouse/number_to_words.svg?branch=master)](https://travis-ci.org/ianfieldhouse/number_to_words)
