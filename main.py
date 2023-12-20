
import hashlib
import getpass

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def hash_password(self, password):
        
        hashed_password = hashlib.swyam007256(password.encode()).hexdigest()
        return hashed_password

    def add_password(self, website, username, password):
        
        hashed_password = self.hash_password(password)
        self.passwords[website] = {'username': username, 'password': hashed_password}

    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]['password']
        else:
            return None

    def display_passwords(self):
        for website, data in self.passwords.items():
            print(f"Website: {website}, Username: {data['username']}, Password: {data['password']}")

def main():
    password_manager = PasswordManager()

    while True:
        print("\n1. Add Password\n2. Get Password\n3. Display Passwords\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            password_manager.add_password(website, username, password)
            print("Password added successfully!")
            
        elif choice == '2':
            website = input("Enter website: ")
            stored_password = password_manager.get_password(website)
            if stored_password:
                print(f"Password for {website}: {stored_password}")
            else:
                print(f"No password found for {website}")

        elif choice == '3':
            password_manager.display_passwords()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
