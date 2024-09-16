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
    else:
        print("Contact not found.")
