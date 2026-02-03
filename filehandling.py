# file = open("ram.txt", "w")

# file.write("Hello world.\n")

# file.write("Welcome to our python class.")

# file.close()



# file = open("shyam.txt", "w")
# file .write("Hello group.\n")
# file .write("This is python group.\n")
# file .write("We are learning python.\n")
# file.close()


# file = open("ram.txt", "a")
# file.write("zoom online class.\n")
# file.close()


# file = open("ram.txt", "r")
# content = file.read()
# print(content)
# file.close()


# file = open("ram.txt", "r")
# line = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# print(line)
# print(line2)
# print(line3)
# file.close()



# file = open("ram.txt", "r")
# line = file.readline()


# while line:
#     print(line, end="")
#     line = file.readline()

# file.close()





# file = open("ram.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()



# file = open("ram.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print(lines, end = "")

# file.close()




# with open("ram.txt", "r") as file:
#     content = file.read()
#     print(content)



# with open("ram.txt", "w") as file:
#     file.write("I am Ram.")



# with open("ram.txt", "a") as file:
#     file.write("\n Hello world.\n")



name = input("Enter your name: ")


with open("ram.txt", "a") as file:
    file.write(name + "\n")

with open("ram.txt", "r") as file:
    content = file.read()
    print(content)

