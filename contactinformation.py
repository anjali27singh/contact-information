import os
import json

class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists('contacts.json'):
            with open('contacts.json', 'r') as file:
                self.contacts = json.load(file)

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self):
        name = input("Enter the name of the contact: ")
        phone_number = input("Enter the phone number of the contact: ")
        email_address = input("Enter the email address of the contact: ")
        self.contacts[name] = {'phone_number': phone_number, 'email_address': email_address}
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        for name, contact in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {contact['phone_number']}")
            print(f"Email Address: {contact['email_address']}")
            print("----------------------------------------")

    def edit_contact(self):
        name = input("Enter the name of the contact you want to edit: ")
        if name in self.contacts:
            phone_number = input("Enter the new phone number of the contact: ")
            email_address = input("Enter the new email address of the contact: ")
            self.contacts[name]['phone_number'] = phone_number
            self.contacts[name]['email_address'] = email_address
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact you want to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def run(self):
        while True:
            print("\n1. Add a new contact")
            print("2. View all contacts")
            print("3. Edit an existing contact")
            print("4. Delete a contact")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_contact()
            elif choice == 2:
                self.view_contacts()
            elif choice == 3:
                self.edit_contact()
            elif choice == 4:
                self.delete_contact()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.run()