# Q1:

# class Coordinate:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if isinstance(other, Coordinate):
#             return Coordinate(self.x + other.x, self.y + other.y)
#         else:
#             return Coordinate(self.x + other, self.y + other)

# c1 = Coordinate(1, 2)
# c2 = Coordinate(3, 4)
# c3 = c1 + c2
# c4 = c1 + 5
# print(f"c3: x = {c3.x}, y = {c3.y}")
# print(f"c4: x = {c4.x}, y = {c4.y}")



# Q2:

# class Person:
#     def __init__(self, name, age):
#         if not isinstance(name, str):
#             raise ValueError('Name must be a string.')
#         elif not isinstance(age, int):
#             raise ValueError('Age must be an integer.')
#         self.name = name
#         self.age = age

# try:
#     p = Person(42, "Twenty")
# except ValueError as e:
#     print(e)



# Q3:

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
#         return 2 * self._radius

#     @property
#     def circumference(self):
#         return 2 * 3.1416 * self._radius

# c = Circle(5)
# print(f"Radius: {c.radius}, Diameter: {c.diameter}, Circumference: {c.circumference}")



# Q4:

# import time

# class TimeIt:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         result = self.func(*args, **kwargs)
#         end = time.time()
#         print(f"Time taken by {self.func.__name__}: {end - start}")
#         return result

# @TimeIt
# def add(a, b):
#     return a + b

# add(1, b=2)



# Q5:

# from collections import namedtuple, defaultdict

# Animal = namedtuple('Animal', ['type', 'name'])
# default_animal = Animal('Dog', 'Tommy')

# animal_dict = defaultdict(lambda: default_animal)

# animal_dict['my_pet'] = Animal('Cat', 'Kitty')
# animal_dict['my_second_pet'] = Animal('Bird', 'Tweety')

# print(animal_dict['my_pet'])
# print(animal_dict['my_second_pet'])
# print(animal_dict['any_other_pet'])
