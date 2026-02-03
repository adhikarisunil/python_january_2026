# def greet():
#     global name   #don't practice this way
#     name = "Ram"
#     print(name)

# greet()

# print(name)







# name = "Ram"


# def greet():
#     print(name)


# greet()
# print(name)




# age = 30

# def increase_age():
#     global age
#     age +=5
#     print(age)


# increase_age()


# cube = lambda x : x **3

# print(cube(3))


# simple_interest = lambda p,t,r: p*t*r/100

# print(simple_interest(10000,3,10))



# def outer():
#     print("I am outer function.")
#     def inner():
#         print("I am inner function.")

#     inner()
# outer()



def greet():
    """
    This function greet users
    """
    print("Hello Ram")

print(greet.__doc__)
greet()