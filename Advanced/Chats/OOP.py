# Advanced:


# Implement operator overloading in Python. Create a Vector class, and implement the + operator to add two vectors.

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3.x, v3.y)


# Implement exception handling in Python. Create a Person class, and raise an exception if a name is not a string.

# class Person:
#     def __init__(self, name):
#         if not isinstance(name, str):
#             raise ValueError('Name must be a string.')
#         self.name = name
# try:
#     p = Person(42)
# except ValueError as e:
#     print(e)


# Implement property decorators in Python. Create a Circle class, with a radius property and a diameter property. If the radius is updated, the diameter should also change.

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#     @property
#     def radius(self):
#         return self._radius
#     @radius.setter
#     def radius(self, radius):
#         self._radius = radius
#     @property
#     def diameter(self):
#         return 2 *


# Implement a decorator in Python. Write a decorator log which wraps functions to log function arguments and the return value on each call. Provide support for both positional and named arguments (your wrapper function should take both *args and **kwargs and print them both):

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Called with args: {args} and kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function returned: {result}")
#         return result
#     return wrapper
# @log
# def add(a, b):
#     return a + b
# add(1, b=2)


# Implement Python's namedtuple and defaultdict. Create a namedtuple 'Animal' with types 'type' and 'name'. Then, create a defaultdict which will return a default Animal namedtuple ('Dog', 'Tommy') when the key does not exist in the dictionary:

# from collections import namedtuple, defaultdict
# Animal = namedtuple('Animal', ['type', 'name'])
# default_animal = Animal('Dog', 'Tommy')
# animal_dict = defaultdict(lambda: default_animal)
# animal_dict['my_pet'] = Animal('Cat', 'Kitty')
# print(animal_dict['my_pet'])
# print(animal_dict['any_other_pet'])