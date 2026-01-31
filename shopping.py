

def add_item():
    item = input("Enter item name: ").lower()
    qty = int(input("Enter quantity: "))

    if item in shopping_list:
        shopping_list[item] += qty
        print(f"{qty} added to existing {item}. Total:{shopping_list[item]}")

    else:
        shopping_list[item] = qty
        print(f"{item} added with quantity {qty}.")




def view_items():
    if not shopping_list:
        print("Shopping list is empty!")

    else:
        print("\n Your Shopping List: ")
        for item, qty in shopping_list.items():
            print(f"{item}: {qty}")



def update_item():
    item = input("Enter item name to update: ").lower()

    if item in shopping_list:
        qty = int(input(f"Enter new quantity for {item}: "))
        shopping_list[item] = qty
        print(f"{item} quantity updated to {qty}.")
    else:
        print(f"{item} not found in the list!")


def delete_item():
    item = input("Enter item name to delete: ").lower()

    if item in shopping_list:
        del shopping_list[item]
        print(f"{item} removed from shopping list.")
    else:
        print(f"{item} not found!")




def show_menu():
    print("\n===== SHOPPING LIST MANAGER =====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")



shopping_list = {}  # start empty

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        print("Exiting Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
