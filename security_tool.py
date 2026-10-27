# task 1 - security tool
#kerr nmcgettigan - b01746321 - lanarkshire campus
# a security tool you have to log in first to get the menu. with handful of security functions it keeps running until you pick exit

# correct login details 
USERNAME = "kerr"
PASSWORD = "Admin123!"

# password used for the brute force simulation
TARGET_PASSWORD = "bruteaccess"
MAX_GUESS = 5


def authenticate(username, password):
    #this checks the details against the stored ones
    #returns true if both match and false if not
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False


    def login():
    #gives the user 3 tries to log in
    #returns true if they get in, false if not
    attempts = 0
 
    while attempts < 3:
        user = input("Username: ").strip()
        pwd = input("Password: ")
 
        if authenticate(user, pwd):
            print("Login successful.\n")
            return True
 
        attempts += 1
        print("Login failed.", 3 - attempts, "attempt(s) left.\n")
 
    # only get here if all 3 tries were wrong
    print("Too many failed attempts. Account frozen for 24 hours.\n")
    return False



def event_counter():
    #asks for the password 10 times and counts the right and wrong ones

    correct = 0
    wrong = 0

    for i in range(10):
        entry = input(f"Enter password  ({i + 1}/10):")

if entry == PASSWORD:
    correct +=1
else:
    wrong += 1

    percent_wrong = (wrong / 10) * 100

    print("\nCorrect:", correct)
    print("Incorrect:", wrong)
    print(f"Percentage incorrect: {percent_wrong}%")

    #flag it if more than half of passwords entered were wrong
    if percent_wrong > 50:
        print("ALERT : more than 50% of the passwords entered were wrong")
        print()


        def brute_force():
            #user keeps guessing the password until they get it or run out of guesses

            guesses = 0 
            while guesses < MAX_GUESSES:
                guess = input(f"Guess {guesses + 1}/{MAX_GUESSES}: ")
        guesses += 1
 
        if guess == TARGET_PASSWORD:
            print("Password found after", guesses, "guess(es).\n")
            return
 
        print("Wrong guess.")
 
    print("Max attempts reached. Stopping the attack.\n")



    def menu():
        #shows the menu until user picks options

        while True:
            print("---Security Menu---")
            print("1. Security Event Counter")
            print("2. Brute force simulation")
            print("3. Login authentication")
            print("4. exit")

            #stops the program crashing if they type letters and not a number

            try:
                choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number.\n")
            continue
 
        print()
        if choice == 1:
            event_counter()
        elif choice == 2:
            brute_force()
        elif choice == 3:
            login()
        elif choice == 4:
            print("Thank you for using the security tool")
            break
        else:
            print("That's not an option, pick 1 to 4.\n")

            #program now starts here. user has to log in before they see the menu

            if login():
                menu()
                