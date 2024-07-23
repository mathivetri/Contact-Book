class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, store_name, phone_number, email, address):
        new_contact = Contact(store_name, phone_number, email, address)
        self.contacts.append(new_contact)

    def view_contacts(self):
        return [(contact.store_name, contact.phone_number) for contact in self.contacts]

    def search_contact(self, query):
        result = []
        for contact in self.contacts:
            if query in contact.store_name or query in contact.phone_number:
                result.append(contact)
        return result

    def update_contact(self, phone_number, store_name=None, email=None, address=None):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                if store_name:
                    contact.store_name = store_name
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                return True
        return False

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                self.contacts.remove(contact)
                return True
        return False
def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(store_name, phone_number, email, address)
            print("Contact added successfully!")

        elif choice == '2':
            contacts = manager.view_contacts()
            print("\nContact List:")
            for contact in contacts:
                print(f"Store Name: {contact[0]}, Phone Number: {contact[1]}")

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = manager.search_contact(query)
            if results:
                for contact in results:
                    print(f"Store Name: {contact.store_name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No contact found!")

        elif choice == '4':
            phone_number = input("Enter the phone number of the contact to update: ")
            store_name = input("Enter new store name (or press enter to keep current): ")
            email = input("Enter new email (or press enter to keep current): ")
            address = input("Enter new address (or press enter to keep current): ")
            updated = manager.update_contact(phone_number, store_name, email, address)
            if updated:
                print("Contact updated successfully!")
            else:
                print("Contact not found!")

        elif choice == '5':
            phone_number = input("Enter the phone number of the contact to delete: ")
            confirm = input("Are you sure you want to delete this contact? (yes/no): ")
            if confirm.lower() == 'yes':
                deleted = manager.delete_contact(phone_number)
                if deleted:
                    print("Contact deleted successfully!")
                else:
                    print("Contact not found!")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
