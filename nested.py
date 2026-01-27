# student = [
#     ["Ram", 17, "Kathmandu"],
#     ["Shyam", 16, "Kathmandu"],
#     ["Shyam", 15, "Pokhara"]
# ]



# print(student[1][2])
# print(student[2][1])



# student[2][0] = "Krishna"
# print(student)


# student[1][1] = 14
# print(student)



# products = [
#     {"name": "laptop", "price": 1000},
#     {"name": "mobile", "price": 2000},
#     {"name": "watch", "price": 3000},
#     {"name": "earphone", "price": 4000}

# ]

# print(products[0]["name"])
# print(products[2]["price"])


# products[0]["price"] = 5000
# print(products)


# products[3]["name"] = "earbuds"
# print(products)





# student = {
#     "name" : "Ram",
#     "age": [40,50,60,70],
#     "hobbies": ["running", "hiking", "swimming", "painting"]
# }



# print(student["age"][3])
# print(student["hobbies"][3])


# student["hobbies"][1] = "gym"
# print(student)


# student["hobbies"].append("gym")
# print(student)





users = {
    "user1" : {"name" : "Ram", "age": 20},
    "user2" : {"name" : "Shyam", "age": 15}
}


print(users["user2"]["name"])
print(users["user1"]["age"])

users["user1"]["name"] = "krishna"
print(users)

users["user2"]["age"] = 10



users["user3"] = {"name": "Hari", "age": 25}
print(users)