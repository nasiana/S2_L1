"""
Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity()
a default value of 50.
Use the following code for your parent Vehicle class:
"""

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

'''
Testing to see if the above worked
'''

bus_1 = Bus('TFL', 50, 500)
print(bus_1.seating_capacity(30))

# ex1 = Bus("bus", 15, 60)
# print(super.ex1.seating_capacity)

'''
TASK: Create a new class called Dog that overwrites the 2 methods of the below class Cat to match the animal. 
Create an instance for each class. 
'''

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class Dog(Cat):

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

dog = Dog("Sniffles", 5)
(dog.info())
(dog.make_sound())

'''
 Write a Python program to create a Vehicle class with colour and max_speed instance attributes.

 Create an instance of the class and print the following: "My car is red and has a maximum speed of 240."
'''

class Vehicle:

     def __init__(self, colour, max_speed):
         self.colour = colour
         self.max_speed = max_speed
         print("My car is {} and has a maximum speed of {}.".format(self.colour, self.max_speed))

car_1 = Vehicle('red', 240)

'''
ASSIGN NEW VALUE TO THE ATTRIBUTE IN CLASS
'''

class Cat:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('Mrr meow meow!')

    def get_info(self):
        print(self.name + " is " + str(self.age) + " years old " + self.breed + " cat.")

    def birthday(self):
        self.age +=1

cat_1 = Cat("Buttons", 3, 'Saber')
print(cat_1.age)
cat_1.birthday()
print(cat_1.age)