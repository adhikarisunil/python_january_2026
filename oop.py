# class Car:
#     #attributes
#     wheels = 4
#     engine = 1

#     #methods
#     def drive(self):
#         print("I drive very fast.")

#     def condition(self):
#         print("My condition is good.")



# car1 = Car() # object create

# print(car1.wheels)
# print(car1.engine)
# car1.condition()
# car1.drive()






# class School:
#     room = 12
#     canteen = 1



#     def quality(self):
#         return("The quality of education is good.")

    
#     def area(self):
#         return("The area of school is 200 square metre.")
    

# my_school = School()
# print(my_school.room)
# print(my_school.canteen)
# print(my_school.quality())
# print(my_school.area())




# class Person:
#     # self ----->object created
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age



# person1 = Person("Ram", 20)   #object creation
# person2 = Person("Shyam", 15)
# person3 = Person("Hari", 10)





# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)
# print(person3.name)
# print(person3.age)






# class Person:
#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location



#     def greet(self):
#         print(f"Person's name is {self.name} and his age is {self.age} and his location is {self.location}.")


# person1 = Person("Ram", 20, "Kathmandu")
# person1.greet()





# class Car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color


#     def details(self):
#         print(f"The name of car is {self.name} and color is {self.color}")

        

# car1 = Car("Suzuki", "Red")
# car1.details()



# class Father:
#     age = 25
#     def skill(self):
#         print("I do farming.")

# class Son(Father):
#     pass


# s1 = Son() #object creation
# s1.skill()
# print(s1.age)





# class Animal:
#     def skill1(self):
#         print("I have 4 legs.")


# class Dog(Animal):
#     def skill2(self):
#         print("Dog Bark.")



# d1 = Dog()
# d1.skill1()
# d1.skill2()




# class Father:
#     def skill_father(self):
#         print("I do farming.")


# class Mother:
#     def skill_mother(self):
#         print("I do cooking.")


# class Uncle:
#     def skill_uncle(self):
#         print("I do driving.")


# class Son(Father, Mother, Uncle):
#     pass
# s1 = Son()
# s1.skill_father()
# s1.skill_mother()
# s1.skill_uncle()






# class Grandfather:
#     def skill_grandfather(self):
#         print("I do farming.")



# class Father(Grandfather):
#     def skill_father(self):
#         print("I am Teacher.")


# class Son(Father):
#     def skill_son(self):
#         print("I am a content creator.")


# s1 = Son()

# s1.skill_son()
# s1.skill_father()
# s1.skill_grandfather()




# class Country:
#     def location1(self):
#         print("I live in Nepal.")
    
# class Province(Country):
#     def location2(self):
#         print("I live in Bagmati.")


# class District(Province):
#     def location3(self):
#         print("I live Kathmandu.")

# l1 = District()
# l1.location3()
# l1.location2()
# l1.location1()





# class Vehicle:
#     def skill(self):
#         print("I drive.")


# class Car(Vehicle):
#     def skill_car(self):
#         print("4 people can sit.")

# class Bike(Vehicle):
#     def skill_bike(self):
#         print("2 people can sit.")

# class Truck(Vehicle):
#     def skill_truck(self):
#         print("I carry heavy loads.")



# c1 = Car()
# c1.skill()
# c1.skill_car()


# b1 =Bike()
# b1.skill()
# b1.skill_bike()


# t1 = Truck()
# t1.skill()
# t1.skill_truck()





# class Vehicle:
#     def skill(self):
#         print("I can drive.")


# class Truck(Vehicle):
#     def skill_Truck(self):
#         print("I lift heavy loads.")

# class Bus(Vehicle):
#     def skill_Bus(self):
#         print("I can carry many people.")

# class Trus(Truck, Bus):
#     def skill_Trus(self):
#         print("I can carry heavy loads and many persons at once.")




# t1 = Trus()
# t1.skill()
# t1.skill_Bus()
# t1.skill_Truck()
# t1.skill_Trus()



class Parent:
    def skill(self):
        print("I do farming.")


class Son(Parent):
    def skill(self):
        print("I am a teacher.")
        super().skill()

s1 =Son()
s1.skill()