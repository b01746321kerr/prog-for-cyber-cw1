# task 3 - ip address validator
# kerr mcgettigan - b01746321 - lanarkshire campus
# checks if an ip address entered by the user has a valid format


def validate_ip(ip):
    # takes an ip address as a string
    # returns tRue if it passes all the checks, False if not

    # remove spaces at the start and end
    ip = ip.strip()

    # must have dots in it
    if "." not in ip:
        return False

    # must have exactly 3 dots
    if ip.count(".") != 3:
        return False

    # split it into the 4 numbers
    parts = ip.split(".")

    # must be 4 parts
    if len(parts) != 4:
        return False

    # check each part
    for part in parts:
        # only digits allowed letters or empty parts fail
        if not part.isdigit():
            return False

        # each number must be between 0 and 255
        number = int(part)
        if number < 0 or number > 255:
            return False

    # passed every check
    return True


# get the ip address from user and show result
ip_address = input("Enter an IP address: ")

if validate_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")