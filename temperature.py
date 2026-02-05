# Celsius to Fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32

# Fahrenheit to Celsius
def f_to_c(f):
    return (f - 32) * 5/9

# Celsius to Kelvin
def c_to_k(c):
    return c + 273.15

# Kelvin to Celsius
def k_to_c(k):
    return k - 273.15

# Fahrenheit to Kelvin
def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

# Kelvin to Fahrenheit
def k_to_f(k):
    return (k - 273.15) * 9/5 + 32




def show_menu():
    print("\n===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")


    


while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c} °C = {c_to_f(c)} °F")

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f} °F = {f_to_c(f)} °C")

    elif choice == "3":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c} °C = {c_to_k(c)} K")

    elif choice == "4":
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k} K = {k_to_c(k)} °C")

    elif choice == "5":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f} °F = {f_to_k(f)} K")

    elif choice == "6":
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k} K = {k_to_f(k)} °F")

    elif choice == "7":
        print("Exiting Temperature Converter. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")

