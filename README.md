# prog-for-cyber-cw1
# task 5 Cyber Security Utilities

- Name: Kerr McGettigan
- Campus lanarkshire
- Banner ID B01746321

## What the program does

A small set of reusable security function `security_tools.py`, which is imported into `main.py`.

`security_tools.py` has three functions;;

- `validate_password()` - checks the password is at least 8 characters and has at least one letter onee digit and one symbol (! @ # $ %) so example kerr2026? wouldnt work
- `validate_ip()` - checks the IP has 3 dots 4 numbers and each number is between 0 and 255
- `generate_password()` - makes a random strong password between 10 and 16 characters with uppercas lowercase, digits and symbols

`main.py` asks the user for a password and an Ip address checks both using the module, and suggests a strong password if theirs isnt strong enough..

# How to run

Needs Python 3. Both files must be in the same folder.

    python3 main.py

# Testing

Screenshots of the tests are in the `Task5_screenshots` folder.

# License

MIT - see `LICENSE`.