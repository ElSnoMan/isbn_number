""" Ten and Thirteen Digit ISBN

Functions:
----------
* Verify the Check Digit of an ISBN-10
* Verify the Check Digit of an ISBN-13
* Convert an ISBN-10 to an ISBN-13
* Convert an ISBN-13 to an ISBN-10

Other Requirements:
--------------------
* Display functions as items in a menu
* Read ISBN numbers from a file
* Write converted ISBN numbers to a file
"""


def verify_ISBN_13_check_digit(isbn_13: str) -> bool:
    numbers = [int(n) for n in isbn_13]
    if len(numbers) != 13:
        return False

    # every other number, starting with the first number, is multiplied by 1
    # then get the sum of all those numbers
    sum_of_ones = sum(numbers[:-1:2])

    # every other number, starting with the second number
    # and excluding the last, is multiplied by 3
    # then get the sum of all those numbers
    sum_of_threes = sum(num*3 for num in numbers[1::2])

    modulo = (sum_of_ones + sum_of_threes) % 10
    check_digit = numbers[-1]

    if modulo == 0:
        return modulo == check_digit
    else:
        return 10 - modulo == check_digit


def verify_ISBN_10_check_digit(isbn_13: str) -> bool:
    pass


def convert_ISBN_10_to_13(isbn_10: str) -> str:
    pass


def convert_ISBN_13_to_10(isbn_13: str) -> str:
    pass


if __name__ == '__main__':
    # show menu and stuff
    pass
