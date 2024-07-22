import json, base64, hashlib, getpass

def encrypt(data):
    encoded = base64.b64encode(data.encode()).decode()
    hashed = hashlib.sha256(encoded.encode()).hexdigest()
    return hashed

def store_password():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    encrypted_password = encrypt(password)

    data = {
        "username": username,
        "password": encrypted_password
    }

    with open("passwords.bin", "wb") as file:
        file.write(json.dumps(data).encode())

    print("Password stored successfully!")

def update_password():
    with open("passwords.bin", "rb") as file:
        data = json.loads(file.read().decode())

    print("Current username:", data["username"])
    print("Current password:", data["password"])

    choice = input("Do you want to update the username (U), password (P), or exit (E)? ")

    if choice.upper() == "U":
        new_username = input("Enter new username: ")
        data["username"] = new_username
    elif choice.upper() == "P":
        new_password = getpass.getpass("Enter new password: ")
        encrypted_password = encrypt(new_password)
        data["password"] = encrypted_password
    elif choice.upper() == "E":
        return
    else:
        print("Invalid choice!")

    with open("passwords.bin", "wb") as file:
        file.write(json.dumps(data).encode())

    print("Password updated successfully!")

def view_password():
    with open("passwords.bin", "rb") as file:
        data = json.loads(file.read().decode())

    print("Username:", data["username"])
    print("Password:", data["password"])

def delete_password():
    choice = input("Are you sure you want to delete the password? (Y/N): ")

    if choice.upper() == "Y":
        with open("passwords.bin", "wb") as file:
            file.write(json.dumps({}).encode())

        print("Password deleted successfully!")
    elif choice.upper() == "N":
        return
    else:
        print("Invalid choice!")

def main():
    while True:
        print("1. Store Password")
        print("2. Update Password or Username")
        print("3. View Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            store_password()
        elif choice == "2":
            update_password()
        elif choice == "3":
            view_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()