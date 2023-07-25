# Q1:

# n = int(input("How many numbers do you want to enter? "))
# print("Enter those numbers: ")
# sum = 0
# for i in range(1, n + 1):
#     x = int(input("-->"))
#     sum += x
# avrg = sum / n
# print("Their Average is: ", avrg)



# Q2:

# for i in range(1,11):
#     print("\n", "~~~~~~", i, "~~~~~~", "\n")
#     for j in range(1,11):
#         print(i, " X ", j, " = ", i * j)




# Q3:

# n = int(input("Enter a number for Fibonacci Series: "))
# a = 0
# b = 1
# if n < 0:
#     print("Enter a positive number.")

# else:
#     for i in range(0,n):
#         print(a)
#         fibo = a + b
#         a = b
#         b = fibo



# Q4:

# n = int(input("Enter a number to check wheter it's Prime or not: "))
# for i in range(2, n):
#     if n % i == 0:
#         print("Not Prime number")
#         break
#     else:
#         print("It is Prime")
#         break



# Q5:

# n = int(input("Enter a number for the list of primes: "))
# T = n
# def siP(n):
#     for i in range(1, n):
#         if n % i == 0:
#             a =  False
#             continue
#         else:
#             a = True
#             continue
#     return a
# b = siP(T)
# for j in range(1, T + 1):
#     if b == True:
#         print(j)
#     else:
#         continue