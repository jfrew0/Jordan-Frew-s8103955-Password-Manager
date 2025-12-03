# =========================================
# Password Manager - DigiCore / Apps2U
# ICTPRG302 Assessment Task 2
# =========================================

import os   # Library function #1

CREDENTIALS_FILE = "credentials.txt"   # Global variable

# ROT3 character set
charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;-!?@#$%^&*()_+=/"


def encrypt(text):
    """Encrypt text using ROT3."""
    result = ""
    for c in text:
        if c in charSet:
            new_pos = (charSet.index(c) + 3) % len(charSet)
            result += charSet[new_pos]
        else:
            result += c
    return result


def decrypt(text):
    """Decrypt ROT3 text."""
    result = ""
    for c in text:
        if c in charSet:
            new_pos = (charSet.index(c) - 3) % len(charSet)
            result += charSet[new_pos]
        else:
            result += c
    return result


def ensure_file_exists():
    """Create the credentials file if it does not exist."""
    if not os.path.exists(CREDENTIALS_FILE):
        open(CREDENTIALS_FILE, "w").close()     # Library function #2


def add_credentials():
    """Ask the user for credentials and save them encrypted."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    url = input("Enter URL or resource: ")

    record = f"{username}|{password}|{url}"
    encrypted = encrypt(record)

    with open(CREDENTIALS_FILE, "a") as f:
        f.write(encrypted + "\n")

    print("\n✔ Credentials saved!\n")


def view_credentials():
    """Read, decrypt and display all stored credentials."""
    ensure_file_exists()

    with open(CREDENTIALS_FILE, "r") as f:
        lines = f.readlines()

    if len(lines) == 0:
        print("\nNo stored credentials.\n")
        return

    print("\n==== Stored Credentials ====\n")
    for line in lines:
        decrypted = decrypt(line.strip())
        username, password, url = decrypted.split("|")
        print(f"Username: {username} | Password: {password} | URL: {url}")
    print()


# ========= Main Program Loop =========
if __name__ == "__main__":
    ensure_file_exists()
    choice = ""

    while choice.lower() != "q":
        print("------ Password Manager ------")
        print("[1] Add stored credentials")
        print("[2] View stored credentials")
        print("[q] Quit")
        choice = input("Select an option: ")

        if choice == "1":
            add_credentials()
        elif choice == "2":
            view_credentials()
        elif choice.lower() == "q":
            print("\nExiting program...\n")
        else:
            print("\nInvalid option — please try again.\n")

    print("Program exit.")
