# task 5 - main program
# kerr mcgettigan - b01746321 - lanarkshire campus
# uses the functions from security_tools.py to check a password and an ip address

import security_tools

# get the password and ip address from the user
password = input("Enter a password: ")
ip_address = input("Enter an IP address: ")
print()

# check the password using a function
if security_tools.validate_password(password):
    print("Password is strong")
else:
    print("Password is not strong")
    # suggest a strong password if their isnt good enough
    print("Suggested password:", security_tools.generate_password())

# check the ip address using the function
if security_tools.validate_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")