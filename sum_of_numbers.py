# numbers = [1, 2, 3, 4, 5]
# total = 0


# for num in numbers:
#     total+= num

# print("Sum=", total)






total = 0

while True:
    num = float(input("Enter number to add(0 to stop): "))

    if num == 0:
        print("Exiting sum.")
        break

    total += num
print(total)