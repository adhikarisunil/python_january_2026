# import random

# number = random.randint(1, 10)
# guess = None

# print("Guess the number between 1 and 10")

# while guess != number:
#     guess = int(input("Enter your guess: "))

#     if guess < number:
#         print("Too low!")
#     elif guess > number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed the correct number 🎉")






# import random


 # random_number = random.randint(1,6)
 # print(random_number)

# random_number = random.randrange(1,7)
# print(random_number)









import random


secrete = random.randint(1,10)

print("Guess a number between 1 to 10:")

while True:
    guess = int(input("Enter a number."))

    if guess == secrete:
        print("You have won.")
        break

    elif guess < secrete:
        print("You are too low. Try Again.")

    else:
        print("You are high. Try Again.")