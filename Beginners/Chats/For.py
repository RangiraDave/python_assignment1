# #For Loops:

# '''Q1:
# Write a program that prints all the numbers from 1 to 10:
# python'''


# for i in range(1, 11):
#     print(i)


# '''Q2:
# Create a program that calculates the sum of all the numbers in a given list:
# python'''


# lst = [1, 2, 3, 4, 5]
# total = 0
# for num in lst:
#     total += num
# print(total)


# '''Q3:
# Write a program that prints the factorial of a given number:
# python'''


# num = int(input("Enter a number: "))
# result = 1
# for i in range(2, num+1):
#     result *= i
# print(f"The factorial of {num} is {result}")


# '''Q4:
# Create a program that generates a multiplication table for a given number:
# python'''

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")


# '''Q5:
# Write a program that counts the number of vowels in a given string:
# python'''


# s = input("Enter a string: ")
# count = 0
# for char in s:
#     if char.lower() in 'aeiou':
#         count += 1
# print(f"Number of vowels: {count}")