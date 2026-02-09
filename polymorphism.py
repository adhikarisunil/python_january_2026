# class Dog:
#     def speak(self):
#         print("Bark.")


# class Cat:
#     def speak(self):
#         print("Mew.")



# def make_animal_speak(animal):
#     animal.speak()


# d1 = Dog()
# c1 = Cat()


# make_animal_speak(d1)
# make_animal_speak(c1)








# class Honda:
#     def color(self):
#         print("Black.")


# class Pulsar:
#     def color(self):
#         print("Blue.")



# def bike_color(bike):
#     bike.color()


# h1 = Honda()
# p1 = Pulsar()


# bike_color(h1)
# bike_color(p1)




# class Bird:
#     def fly(self):
#         print("Bird can fly.")


# class Penguin(Bird):
#     def fly(self):
#         print("Penguin cannot fly.")


# b = Bird()
# p = Penguin()


# b.fly()
# p.fly()







# class Fruit:
#     def taste(self):
#         print("Fruit are sweet in taste.")


# class Avogado(Fruit):
#     def taste(self):
#         print("Avogado is not sweet in taste.")


# b = Fruit()
# p = Avogado()


# b.taste()
# p.taste()




# print(2 + 3)
# print("Hello" + " World")



class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 22/7 * (self.radius**2)
    


r1 = Rectangle(8,5)
print(r1.area())


c1 = Circle(12)
print(c1.area())
