# Q1:

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Car(Vehicle):
#     pass

# class Bike(Vehicle):
#     pass

# car = Car(220, 12)
# print(car.max_speed, car.mileage)

# bike = Bike(120, 18)
# print(bike.max_speed, bike.mileage)



# Q2:

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no

# stu = Student("John", "42")
# print(stu.name, stu.roll_no)





# Q3:

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     @classmethod
#     def from_string(cls, date_string):
#         day, month, year = map(int, date_string.split('-'))
#         return cls(day, month, year)

# date = Date.from_string('29-02-2020')
# print(date.day, date.month, date.year)




# Q4:

# class Math:
#     @staticmethod
#     def factorial(n):
#         if n == 0:
#             return 1
#         else:
#             return n * Math.factorial(n-1)

# print(Math.factorial(5))




# Q5:

# class Animal:
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return 'Woof!'

# class Cat(Animal):
#     def sound(self):
#         return 'Meow!'

# dog = Dog()
# cat = Cat()

# print(dog.sound())
# print(cat.sound())
