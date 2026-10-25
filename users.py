 #Student 5: User login and current-user management for MiniOS MTB.

USERS = {
    "admin": "admin123",
    "student": "student123",
}

current_user = None


def login():
    #Ask the user to log in, allowing up to three attempts.
    global current_user

    print("\n========== MINIOS MTB LOGIN ==========")
    attempts = 3

    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ")

        if username in USERS and USERS[username] == password:
            current_user = username
            print(f"\nLogin successful. Welcome, {username}!\n")
            return username

        attempts -= 1
        print("\nInvalid username or password.")
        print(f"Attempts remaining: {attempts}")

    print("\nToo many failed attempts.")
    return None


def whoami():
    #"""Display the username of the currently logged-in user."""
    if current_user is None:
        print("No user is currently logged in.")
    else:
        print(f"Current User: {current_user}")


def get_current_user():
    #"""Return the current username for system information."""
    return current_user


def check_login(username, password):
    #"""Return True if credentials match a configured demo account."""
    return username in USERS and USERS[username] == password