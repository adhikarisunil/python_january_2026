# def greet():
#     print("Good morning.")

# greet()



# def hello():
#     print("Hello world.")

# hello()


# def greet(name):
#     print(f"Good morning {name}.")

# greet("Ram")



# def add(a,b):
#     print(a+b)

# add(2,3)


# def ram_age():
#     return 34
# print(ram_age())


# def sum(a,b):
#     return a + b

# print(sum(2,3))


# def mul(a,b):
#     return a * b

# print(mul(2,3))


# def info(name, age):
#     return(f"{name} and {age}")

# print(info(age=20, name="Ram"))



# def greet(name="Ram"):
#     return f"Good morning, {name}."

# print(greet())





# def numbers(*nums):
#     print(nums)

# numbers(2,3,4,5,6)



def numbers(*nums):
    total = 0
    for num in nums:
        total += num

    return total
print(numbers(1,2,3,4,5,6))