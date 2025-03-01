class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        """Add a new contact to the contact book."""
        name = input("Enter contact name: ")
        phone_number = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")

        if name not in self.contacts:
            self.contacts[name] = {
                "phone_number": phone_number,
                "email": email,
                "address": address
            }
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists.")

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Your Contacts:")
            for index, (name, details) in enumerate(self.contacts.items(), start=1):
                print(f"{index}. Name: {name}")
                print(f"   Phone Number: {details['phone_number']}")
                print(f"   Email: {details['email']}")
                print(f"   Address: {details['address']}\n")

    def search_contact(self):
        """Search for a contact by name."""
        name = input("Enter contact name to search: ")
        if name in self.contacts:
            print(f"Contact '{name}' found:")
            print(f"Phone Number: {self.contacts[name]['phone_number']}")
            print(f"Email: {self.contacts[name]['email']}")
            print(f"Address: {self.contacts[name]['address']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self):
        """Update a contact's details."""
        name = input("Enter contact name to update: ")
        if name in self.contacts:
            print("Enter new details (press Enter to keep current value):")
            phone_number = input(f"Phone Number ({self.contacts[name]['phone_number']}): ")
            email = input(f"Email ({self.contacts[name]['email']}): ")
            address = input(f"Address ({self.contacts[name]['address']}): ")

            if phone_number:
                self.contacts[name]["phone_number"] = phone_number
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address

            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' does not exist.")

    def delete_contact(self):
        """Delete a contact from the contact book."""
        name = input("Enter contact name to delete: ")
        if name in self.contacts:
            confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").lower()
            if confirm == "yes":
                del self.contacts[name]
                print(f"Contact '{name}' deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Contact '{name}' does not exist.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
