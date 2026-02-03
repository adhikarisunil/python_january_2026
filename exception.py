# try:
#     print(10/0)

# except ZeroDivisionError:
#     print("Error: You cannot divide by zero.")



# try:
#     int("Ram")

# except ValueError:
#     print("Error: Cannot convert string to integer.")


# try:
#     num = int(input("Enter a number: "))
#     print(12/num)
# except ZeroDivisionError:
#     print("Error occurred")

# except ValueError:
#     print("Error occurred")


# try:
#     num = int(input("Enter a number: "))
#     print(12/num)
# except (ZeroDivisionError, ValueError):
#     print("Error occurred")




# try:
#     print(10/0)

# except Exception as e:
#     print(e)



#try ------> possible
#except------->if error, print
#finally------> either error or not--->run



# try: 
#     print(10/0)

# except ZeroDivisionError:
#     print("Error: You cannot divide by zero.")

# finally:
#     print("I always run.")


# try:
#     file = open("shyam.txt", "r")
#     content = file.read()
#     print(content)

# except FileNotFoundError:
#     print("Error: File not found.")


# finally:
#     print("This block always run.")

#     try:
#         file.close()

#     except:
#         print("File cannot be closed.")




# age = int(input("Enter your age: "))


# if age < 0:
#     raise ValueError("Age cannot be zero.")



def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except TypeError:
        print("Error: You cannot divide by string.")
    finally:
        print("print always")
print(safe_divide(10,5))