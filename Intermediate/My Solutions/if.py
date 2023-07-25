# Q1:

# marks = int(input("Enter Your marks: "))
# if marks <= 100 and marks >= 95:
#     print("You got an A+")
# elif marks >= 85:
#       print("You got A")
# elif marks >= 70:
#     print("You got B")
# elif marks >= 60:
#     print("You got C")
# elif marks >= 50:
#    print("You got D")
# elif marks >=30:
#     print("You got E")
# elif marks >= 10:
#     print("You got s")
# elif marks < 10:
#     print("You got F")
# elif not int:
#     print("INVALID INPUT!")



# Q2:

# n = int(input("Enter a Year that you were bone in: "))
# i = int(input("Enter a month you were bone in: "))
# if n % 4 == 0 and n % 100 == 0 or n % 400 == 0:
#     print("You entered a Leap year")
# else:
#     print("You entered a Non-Leap year")
# if i == 2:
#         print("The month you entered is Feb.")
# elif i % 2 == 0:
#     print("You entered a 30-Days-month")
# else:
#     print("You entered a 31-days-month")



# Q3:

# s = input("Enter a string to check: ")
# if s == s[::-1]:
#     print("It is Palindrome")
# else:
#     print("Not palindrome")



# Q4:

# p = input("Enter Your password: ")
# crit = '''aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ,./;[]<>?:"{}!@#$%^&*()1234567890-=+_'''
# for i in range(0, len(p) - 1):
#     if p[i] in crit and p[i] != p[i + 1]:
#         t = "Your password is Valid"
#     else:
#         t = "Your password is Invalid."
# print(t)




# Q5:

# n = int(input("Enter a number to check whether it's Prime or not: "))

# if n > 1:
#     for i in range(2, n):
#         if (n % i) == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not prime")
