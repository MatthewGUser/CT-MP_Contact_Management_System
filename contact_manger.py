import helpers
import contacts_storage

def main_menu():
    while True:
        print("Welcome to the Contact Management System! ")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            unique_id = input("Enter a unique ID: ")
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            if not helpers.validate_phone(phone):
                print("Invalid phone number.")
                continue
            email = input("Enter email: ")
            if not helpers.validate_email(email):
                print("Invalid email.")
                continue
            additional_info = input("Enter additional info (optional): ")
            contacts_storage.add_contact(unique_id, name, phone, email, additional_info)
            print("Contact added successfully!")
        
        elif choice == "8":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main_menu()
