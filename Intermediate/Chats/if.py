# If Statements:



# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# 
# print("Input lengths of the triangle sides: ")
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))

# if x == y == z:
#     print("Equilateral triangle")
# elif x==y or y==z or z==x:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")


# Write a Python program to check if a number is a multiple of another number.
# 
# def multiple(m, n):
#     return True if m % n == 0 else False
# print(multiple(20, 5))
# print(multiple(7, 2))

# Write a Python program to check a string represent an integer or not.
# 
# text = input("Input a string: ")
# text = text.strip()
# if len(text) < 1:
#     print("Input a valid text")
# else:
#     if all(text[i] in "0123456789" for i in range(len(text))):
#         print("The string is an integer.")
#     elif (text[0] in "+-" and 
#         all(text[i] in "0123456789" for i in range(1,len(text)))):
#         print("The string is an integer.")
#     else:
#         print("The string is not an integer.") 


# Write a Python program to check if an input is an integer or a string.
# 
# text = input("Input a string or an integer: ")
# if text.isdigit():
#     print(f"{text} is a integer.")
# else:
#     print(f"{text} is a string.")


# Write a Python program to check if a number is positive, negative or zero.
# 
# num = float(input("Input a number: "))
# if num > 0:
#     print("It is positive number")
# elif num == 0:
#     print("It is Zero")
# else:
#     print("It is a negative number")