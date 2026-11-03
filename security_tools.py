# task 5  security tools module
# kerr mcgettigan  b01746321  lanarkshire campus
# this reusable security functions that get imported into main.py

import random

# characters used to make passwords
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SYMBOLS = "!@#$%"


def validate_password(password):
    # checks a password is at least 8 characters long
    # and has at least one letter, one digit and one symbol
    # returns True if it passes False if not
    iflen(password) <=8:
        return False

    has_Letter = False
    has_digit = False
    has_symbol = False

    # looks at each character and see what type it is
for char in password:
        if char.isalpha():
            has_letter = True
    elif char.isdigit():
            has_dgit = True
        elif char in SYMBOLS:
            has_symbol = True

    if has_letter and has_digit and has_symbol:
        return True
    else
        return False
