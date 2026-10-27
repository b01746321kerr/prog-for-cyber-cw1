# prog-for-cyber-cw1

# Task 1: Security Tool

**Name:** Kerr McGettigan
**Campus:** Lanarkshire
**Banner ID:** B01746321

## What the program does

A menu-driven security tool. The user has to log in before they can use the menu. The menu has,

1. Security Event Counter this asks for the password 10 times, counts the correct and incorrect ones,  and shows the percentage incorrect and gives an alert if it's over 50%.
2. Brute force Simulation the user guesses a set password. Stops when it's guessed or after 5 attempts.
3. Login Authentication  asks for a username and password. After 3 failed logins the account is frozen for 24 hours
4. Exit shows "Thank you for using the security tool" and closes the program.

Letters or wrong numbers more than 4 in the menu are delt with try/except so the program doesn't crash.

## Test details

- Username: `kerr`
- Password: `Admin123!`
- Brute-force password: `bruteaccess`

## How to run

Needs Python 3.

    python3 security_tool.py

## Testing

Screenshots of the tests are in the `Task1_securityTool_screenshots` folder.

## License

MIT - see `LICENSE`.