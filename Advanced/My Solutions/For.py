# Q1:

# num = int(input("Enter a number: "))
# factors = set()

# for i in range(1, int(num**0.5) + 1):
#     if num % i == 0:
#         factors.add(i)
#         factors.add(num // i)

# print("Factors of", num, "are:")
# for factor in sorted(factors):
#     print(factor)



# Q2:

# n = int(input("Enter a number for Fibonacci Series: "))
# a = 0
# b = 1
# if n < 0:
#     print("Enter a positive number.")

# else:
#     for i in range(0,n):
#         print(a, end = ',')
#         fibo = a + b
#         a = b
#         b = fibo
# print(".")



# Q3:

# lst1 = [1, 2, 3, 4, 5,4,4,3,6,3]
# lst2 = [4, 5, 6, 7, 8,4,5,6,7,7]
# inter= [value for value in lst1 if value in lst2]

# print(f"Intersection: {inter}")



# Q4:

# n = int(input("Enter the number of rows for the triangle: "))

# count = 1
# for i in range(n):
#     output = ' ' * (n - i - 1)
#     for _ in range(2 * i + 1):
#         output += str(count) + " "
#         count += 1
#     print(output.center(n*4))




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