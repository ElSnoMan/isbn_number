""" ISBN Tests

These links explained ISBN digits generation really well:
https://isbn-information.com/check-digit-for-the-13-digit-isbn.html
https://en.wikipedia.org/wiki/International_Standard_Book_Number
"""


import os, sys
sys.path.append(os.getcwd()) # solves Import Errors
from main import *


data = '9780306406157'
valid_isbn_13 = '9781861972712'
invalid_isbn_13 = '9781681972712'

valid_isbn_10 = '9992158107'
invalid_isbn_10 = '9992985107'


def test_verify_ISBN_13_with_valid():
    is_valid = verify_ISBN_13_check_digit(valid_isbn_13)
    assert is_valid


def test_verify_ISBN_13_with_invalid():
    is_valid = verify_ISBN_13_check_digit(invalid_isbn_13)
    assert is_valid is False
