# task 2 - security event logger
# kerr mcgettigan - b01746321 - lanarkshire campus
# program ask for a username and password until they are correct
# every attempt failed or successful is printed as a security event loger

import random
import socket
from datetime import datetime

# correct login details
USERNAME = "kerr"
PASSWORD = "Admin123!"

# get the ip address of this computer
# if there is no network it uses 127.0.0.1 so the program doesnt crash
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
except OSError:
    ip_address = "127.0.0.1"

print("SECURITY EVENT LOG")
print("==================")

logged_in = False

# keep asking until the correct username and password are entered
while not logged_in:
    username = input("Username: ").strip()
    password = input("Password: ")

    # check the details and decide what the event is
    if username == USERNAME and password == PASSWORD:
        event = "Successful login"
        logged_in = True
    else:
        event = "Failed login"

    # random 4 digit event id and current date and time
    event_id = random.randint(1000, 9999)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # print the log for this attempt
    print("\nEvent ID:", event_id)
    print("Username:", username)
    print("IP Address:", ip_address)
    print("Event:", event)
    print("Timestamp:", timestamp)
    print()