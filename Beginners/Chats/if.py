
# # If Statements:


# '''Q1:
# Write a program that checks if a given number is positive, negative, or zero:
# python'''


# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# '''Q2:
# Create a program that determines whether a user's input is an even or odd number:
# python'''


# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# '''Q3:
# Write a program that checks if a year entered by the user is a leap year or not:
# python'''

# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 != 0 or year % 400 == 0:
#         print("Leap year")
#     else:
#         print("Not a leap year")
# else:
#     print("Not a leap year")


# '''Q4: 
# Create a program that checks if a given string is a palindrome:
# python
# Copy code'''


# word = input("Enter a word: ")
# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# '''Q5:
# Write a program that determines if a person is eligible to vote based on their age:
# python
# Copy code'''

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")