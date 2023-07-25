# For Loops:


# Write a Python program to construct the following pattern, using a nested for loop.
# 
# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')


# Write a Python program that accepts a string and calculate the number of digits and letters.
# 
# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)


# Write a Python program to check the validity of a password (input from users).
# 
# import re
# p = input("Input your password")
# x = True
# while x:  
#     if (len(p)<6 or len(p)>12):
#         break
#     elif not re.search("[a-z]",p):
#         break
#     elif not re.search("[0-9]",p):
#         break
#     elif not re.search("[A-Z]",p):
#         break
#     elif not re.search("[$#@]",p):
#         break
#     elif re.search("\s",p):
#         break
#     else:
#         print("Valid Password")
#         x = False
#         break
# if x:
#     print("Not a Valid Password")


# Write a Python program to calculate a dog's age in dog's years.
# 
# human_age = int(input("Input a dog's age in human years: "))

# if human_age < 0:
#     print("Age must be positive number.")
#     exit()
# elif human_age <= 2:
#     dog_age = human_age * 10.5
# else:
#     dog_age = 21 + (human_age - 2)*4

# print("The dog's age in dog's years is", dog_age)


# Write a Python program to check a triangle is valid or not.
# 
# def triangle_check(l1,l2,l3):
#     if (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
#         print('No, the lengths wont form a triangle')
#     elif (l1==l2+l3) or (l2==l1+l3) or (l3==l1+l2):
#         print('yes, it can form a degenerated triangle')
#     else:
#         print('Yes, a triangle can be formed out of it')

# length1 = int(input("Enter side 1\n"))
# length2 = int(input("Enter side 2\n"))
# length3 = int(input("Enter side 3\n"))
# triangle_check(length1,length2,length3)
