contacts = {}

def add_contact(unique_id, name, phone, email, additional_info=None):
    contacts[unique_id] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info
    }

def edit_contact(unique_id, name=None, phone=None, email=None, additional_info=None):
    if unique_id in contacts:
        if name: contacts[unique_id]['Name'] = name
        if phone: contacts[unique_id]['Phone'] = phone
        if email: contacts[unique_id]['Email'] = email
        if additional_info: contacts[unique_id]['Additional Info'] = additional_info
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(unique_id):
    if unique_id in contacts:
        del contacts[unique_id]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact(unique_id):
    return contacts.get(unique_id, None)

def display_all_contacts():
    if contacts:
        for unique_id, info in contacts.items():
            print(f"ID: {unique_id}, Name: {info['Name']}, Phone: {info['Phone']}, Email: {info['Email']}, Additional Info: {info['Additional Info']}")
    else:
        print("No contacts found.")

def export_contacts(file_name):
    with open(file_name, 'w') as file:
        for unique_id, info in contacts.items():
            file.write(f"{unique_id},{info['Name']},{info['Phone']},{info['Email']},{info['Additional Info']}\n")

def import_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                unique_id, name, phone, email, additional_info = line.strip().split(',')
                contacts[unique_id] = {
                    'Name': name,
                    'Phone': phone,
                    'Email': email,
                    'Additional Info': additional_info
                }
    except FileNotFoundError:
        print(f"File {file_name} not found.")
