# num = int(input("Enter a number:"))


# if num % 2 == 0:
#     print("The number is Even")

# else:
#     print("The number is Odd.")





# num  = int(input("Enter a number: "))


# if num %2 == 0:
#     print("Even")
# else:
#     print("Odd")





while True:

    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("Even")

    else: 
        print("Odd")


    

    choice = input("Do you want to check another number ? (yes/no)")


    if choice == "no":
        print("Exiting loop.")
        break