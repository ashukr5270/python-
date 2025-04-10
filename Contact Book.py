import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

# Search contact by name
def search_contacts(contacts):
    query = input("Enter name to search: ").strip().lower()
    found = [c for c in contacts if query in c['name'].lower()]
    if found:
        for c in found:
            print(f"- {c['name']} | {c['phone']} | {c['email']}")
    else:
        print("No contact found.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        deleted = contacts.pop(index)
        print(f"Deleted contact: {deleted['name']}")
    except (ValueError, IndexError):
        print("Invalid number.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
