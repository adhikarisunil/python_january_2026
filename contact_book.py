

contacts ={}

def show_menu():
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View All contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
show_menu()


#Add contact
def add_contact():
    name = input("Enter a name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")



    if name in contacts:
        print(f"{name} already exists.")

    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"{name} added successfully.")


# View Contacts
def view_contact():
    if not contacts:
       print("Contacts not found.")

    else: 
       for name, info in contacts.items():
           print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


# Search Contact
def search_contact():
    name = input("Enter a name: ")

    if name in contacts:
        info  = contacts[name]
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    
    else: print(f"{name} not found.")



def update_contact():
    name = input("Enter a name to update: ")

    if name in contacts:
        phone = input("Enter phone number(Leave empty for not changing.): ")
        email = input("Enter email(Leave empty for not changing): ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email


        print(f"{name}'s contact updated.")

    else:
        print(f"{name} not found.")



def delete_contact():
    name = input("Enter a name to delete: ")

    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully. ")

    else:
        print(f"{name} not found.")


while True:
    show_menu()
    choice = input("Enter a number(1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Exiting program. Goodbye.")
        break

    else:
        print("Invalid choice.")