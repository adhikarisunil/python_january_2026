contacts = {
    "Ram": {"phone": "9860841089",  "email": "ram@gmail.com"},
    "Shyam": {"phone": "9808416776", "email": "shyam@gmail.com"}
}


# contacts["Hari"] = {"phone": "9845407271", "email":"hari@gmail.com"}
# print(contacts)

#Show Menu

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


    # contacts[name] = {"phone": phone, "email": email}
    # print(contacts)
add_contact()



def view_contact():
    if not contacts:
        print("No contacts found.")

    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


view_contact()


def search_contact():
    pass

search_contact()


def update_contact():
    pass
update_contact()


def delete_contact():
    pass
delete_contact()


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