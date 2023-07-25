# Q1:

# s = input("Enter a string to check: ")
# if s == s[::-1]:
#     print("It is Palindrome")
# else:
#     print("Not palindrome")



# Q2:

# n = int(input("Enter a number: "))
# T = n**0.5

# if int(T + 0.5) ** 2 == n:
#     print(f"{n} is a perfect square")
# else:
#     print(f"{n} is not a perfect square")



# Q3:

# n = int(input("Enter a number to check whether it's Prime or not: "))

# if n > 1:  # primes are + integers greater than 1
#     for i in range(2, n):
#         if (n % i) == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not prime")



# Q4:

# import random

# choices = {0: 'rock', 1: 'paper', 2: 'scissors'}
# print("Enter your choice: 0 for rock, 1 for paper, 2 for scissors. ")
# user_choice = int(input("Enter your choice: "))
# computer_choice = random.randint(0, 2)

# if user_choice == computer_choice:
#     print('Draw, Try again')
# elif (user_choice - computer_choice) % 3 == 1:
#     print('Congrats! you won')
# else:
#     print('Computer wins')



# Q5:

# import cmath

# a = float(input("Enter The Value of a: "))
# b = float(input("Enter The Value of b: "))
# c = float(input("Enter The Value of c: "))

# D = cmath.sqrt(b**2 - 4*a*c)

# x = (-b + D) / (2*a)
# y = (-b - D) / (2*a)

# print(f"x = {x}")
# print(f"y ={y}")
