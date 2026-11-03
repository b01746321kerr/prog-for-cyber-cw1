# prog-for-cyber-cw1
# Task 3: IP Address Validator

- Name: Kerr McGettigan
- Campus: Lanarkshire
- Banner ID: B01746321

# What the program does

asks user for an IP address and checks if it has a valid format using a function called `validate_ip()`. this function:

- Removes spaces at the start and end
- checks the IP has dots in it
- checks thereis 3 dots in ip
- checks there are 4 numbers
- checks each number only contains digits and is between 0 and 255

It returns True if all checks pass and False if not the program then shows "Valid IP address" or "Invalid IP address".

# Example

    enter an ip address: 192.168.1.10
    Valid IP address

    Enter an IP address: 192.168.1.300
    Invalid IP address

# How to run

Needs Python 3.

    python3 ip_address_validator.py

# Testing

Screenshots of the tests are in the `Task3_screenshots` folder.

# License

MIT - see `LICENSE`.