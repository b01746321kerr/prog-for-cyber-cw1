# prog-for-cyber-cw1
# Task 4 Security Incident Manager

 Name Kerr McGettigan
 Campus Lanarkshire
 Banner ID B01746321

# What the program does

stores details about a security incident in a dictionary and updates them
 The program:

1 Creates a dictionary with a username, ip address, event type and risk level
2 Shows the username and IP address
3 Adds a new field called status
4 Updates the risk level
5 Removes a field chosen by the user
6 Shows all the keys and values left
7 Shows the total number of key value pairs

If the user enters a field that doesnt exist, try except stops the program crashing and nothing is removed

# How to run

Needs Python 3.

    python3 security_incident_manager.py

when asked type one of the field names shown for example i used `event_type`.

# Testing

screenshots of the tests are in the `Task4_screenshots` folder.

# License

MIT - see `LICENSE`.