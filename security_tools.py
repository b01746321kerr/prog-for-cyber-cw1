# task 5 - security tools module
# kerr mcgettigan - b01746321 - lanarkshire campus
# reusable security functions that get imported into main.py

import random

# characters used to make passwords
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SYMBOLS = "!@#$%"


def validate_password(password):
    # checks the password is at least 8 characters long
    # and has at least one letter, one digit and one symbol
    # returns True if it passes False if not
    if len(password) < 8:
        return False

    has_letter = False
    has_digit = False
    has_symbol = False

    # look at each character and see what type it is
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif char in SYMBOLS:
            has_symbol = True

    if has_letter and has_digit and has_symbol:
        return True
    else:
        return False


def validate_ip(ip):
    # basic ip check - 3 dots, 4 numbers, each between 0 and 255
    # returns True if valid, False if not
    ip = ip.strip()

    if ip.count(".") != 3:
        return False

    parts = ip.split(".")

    for part in parts:
        # only digits allowed, so letters or empty parts fail
        if not part.isdigit():
            return False

        number = int(part)
        if number < 0 or number > 255:
            return False

    return True


def generate_password():
    # makes a random strong password between 10 and 16 characters long
    # with uppercase, lowercase, digits and symbols
    # returns the password
    all_chars = UPPERCASE + LOWERCASE + DIGITS + SYMBOLS
    length = random.randint(10, 16)

    # keep making passwords until one has all 4 types of character
    while True:
        password = ""
        for i in range(length):
            password += random.choice(all_chars)

        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in SYMBOLS:
                has_symbol = True

        if has_upper and has_lower and has_digit and has_symbol:
            return password