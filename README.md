# Contact Management System
## Project Overview
Welcome to the Contact Management System! This is a command-line-based Python application that allows you to manage your contacts easily. You can add, edit, delete, and search for contacts, as well as export and import them from a text file.

The project is structured into multiple Python files to ensure clean code organization and maintainability. It utilizes Python dictionaries to store contact information and includes features such as input validation and error handling.

## Features
* Add, Edit, Delete Contacts: Manage your contacts by adding, editing, and deleting entries. Each contact is stored with a name, phone number, email, and additional information.
* Search Contacts: Look up contact information by their name or unique identifier.
* Display All Contacts: View a list of all saved contacts.
* Export Contacts to File: Save your contacts to a text file for backup or sharing.
* Import Contacts from File: Load contacts from a text file into the system (Bonus Feature).
* User-Friendly CLI: Simple and intuitive menu-driven interface.
* Input Validation: Ensures that the contact information (e.g., email and phone number) is in the correct format using regular expressions.
* Error Handling: Graceful handling of invalid input and file-related errors.

## File Structure
This project is organized across multiple files to improve readability and code management. Here’s a breakdown of the key files:

1. contact_manager.py - The main file responsible for running the application and managing the command-line interface. It handles user interaction and delegates tasks to helper modules.

2. contacts_storage.py - Contains the functions responsible for managing the contact data (e.g., adding, editing, deleting contacts). The contact list is stored in a dictionary, and operations on the data are performed here.

3. helpers.py - Contains utility functions such as input validation (e.g., email and phone number regex checks) and file handling functions (e.g., exporting and importing contacts).

4. README.md - This file, providing an overview of the project.

## How to Run the Application
1. Clone the Repository:

```
git clone https://github.com/MatthewGUser/CT-MP_Contact_Management_System
cd CT-MP_Contact_Management_System
```

2. Run the Application: In your terminal, run the contact_manager.py file to start the program:
```
python contact_manager.py
```

3. Menu Options: Once the program is running, you’ll be greeted with the following menu:
```
Welcome to the Contact Management System!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit
```
4. Follow the Instructions: Choose the number corresponding to the action you want to take and follow the prompts to manage your contacts.

## Example Usage
Here’s a sample interaction with the Contact Management System:

```
Welcome to the Contact Management System!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit

Select an option (1-8): 1
Enter contact name: John Doe
Enter phone number: 123-456-7890
Enter email address: john@example.com
Enter additional information: Friend from work
Contact added successfully!
```

## Input Validation
* Email Validation: Ensures the email follows a standard email format using regex.
* Phone Number Validation: Ensures the phone number follows a proper format.
* Error Handling: The program gracefully handles incorrect inputs and invalid file paths.

## Project Structure
```
contact-management-system/
├── contact_manager.py    # Main entry point for the application (UI and menu).
├── contacts_storage.py   # Functions for adding, editing, deleting contacts.
├── helpers.py            # Input validation and file handling functions.
└── README.md             # Project overview and instructions.
```

## Conclusion
This Contact Management System allows you to manage your contacts with ease, featuring a modular code structure for better organization and maintainability. Feel free to explore the code and extend its functionalities!
