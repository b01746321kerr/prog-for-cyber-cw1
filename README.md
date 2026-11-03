# prog-for-cyber-cw1
## Task 2: Security Event Logger

Name kerr McGettigan
Campus Lanarkshire
Banner ID B01746321

# What the program does

Asks user for a username and password until the correct ones are entered. Every attempt is printed as a security event log with:

- Event ID 
- Username
- IP Address of the computer running the program
- Event if it was failed login or Successful login
- Timestamp

If the IP address can't be found it uses 127.0.0.1 so the program does not crash.

# Test details

- Username: `kerr`
- Password: `Admin123!`

# How to run

Needs Python 3.

    python3 security_event_logger.py

# Testing

Screenshots of the tests are in the `Task2_screenshots` folder.

# License

MIT - see `LICENSE`.