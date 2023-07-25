# OOP

# Define a class named Circle which can be constructed by a radius. The Circle class has a method that can compute the area.

# class Circle():
#     def __init__(self, r):
#         self.radius = r
#     def area(self):
#         return 3.1416 * (self.radius ** 2)
# circle = Circle(5)
# print(circle.area())


# Define a class named Rectangle which can be constructed by length and width. The Rectangle class has a method which can compute the area.

# class Rectangle():
#     def __init__(self, l, w):
#         self.length = l
#         self.width  = w

#     def area(self):
#         return self.length * self.width
# rect = Rectangle(5,4)
# print(rect.area())


# Create a Student class and initialize it with name and roll number. Make methods to display all information about the student.

# class Student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number

#     def display(self):
#         print("Name: ", self.name)
#         print("Roll Number: ", self.roll_number)
# stu = Student("John", "42")
# stu.display()


# Create a Temperature class. Make two methods: one method to convert Fahrenheit to Celsius and another method to convert Celsius to Fahrenheit.

# class Temperature:
#     def to_celsius(self, fahrenheit):
#         return (fahrenheit - 32) * 5/9

#     def to_fahrenheit(self, celsius):
#         return celsius * 9/5 + 32
# temp = Temperature()
# print(temp.to_celsius(100))
# print(temp.to_fahrenheit(0))


# Create a Time class and initialize it with hours and minutes. Make a method addTime which should take two times as parameters and return a new Time object, and another method displayTime which should print the time.

# class Time:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
#     def add_time(self, t1, t2):
#         t3 = Time(0, 0) # creating new object
#         t3.hours = t1.hours + t2.hours # sum of hours
#         t3.minutes = t1.minutes + t2.minutes # sum of minutes
#         while t3.minutes >= 60:
#             t3.hours += 1
#             t3.minutes -= 60
#         return t3
#     def display_time(self):
#         print(f"Time is {self.hours} hours and {self.minutes} minutes")
# t1 = Time(2, 50)
# t2 = Time(1, 20)
# t3 = t1.add_time(t1, t2)
# t3.display_time()
