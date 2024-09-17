import helpers
import contacts_storage

def main_menu():
    while True:
        print("\nWelcome to the Contact Management System! ")
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
        
        elif choice == "2":
            unique_id = input("Enter the unique ID of the contact to edit: ")
            name = input("Enter new name (or press Enter to keep unchanged): ")
            phone = input("Enter new phone (or press Enter to keep unchanged): ")
            if phone and not helpers.validate_phone(phone):
                print("Invalid phone number.")
                continue
            email = input("Enter new email (or press Enter to keep unchanged): ")
            if email and not helpers.validate_email(email):
                print("Invalid email.")
                continue
            additional_info = input("Enter new additional info (optional): ")
            contacts_storage.edit_contact(unique_id, name, phone, email, additional_info)
        
        elif choice == "3":
            unique_id = input("Enter the unique ID of the contact to delete: ")
            contacts_storage.delete_contact(unique_id)
        
        elif choice == "4":
            unique_id = input("Enter the unique ID of the contact to search: ")
            contact = contacts_storage.search_contact(unique_id)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print("Contact not found.")
        
        elif choice == "5":
            contacts_storage.display_all_contacts()
        
        elif choice == "6":
            file_name = input("Enter the file name to export contacts to: ")
            contacts_storage.export_contacts(file_name)
            print(f"Contacts exported to {file_name}")
        
        elif choice == "7":
            file_name = input("Enter the file name to import contacts from: ")
            contacts_storage.import_contacts(file_name)
            print(f"Contacts imported from {file_name}")
        
        elif choice == "8":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main_menu()
