# #For Loops:


# '''Q1:
# Program to print a pattern of numbers using loops:
# '''
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


# '''Q3:
# Program to print the Fibonacci sequence up to a certain number:
# '''
# n = int(input("Enter a number: "))
# a, b = 0, 1

# while a < n:
#     print(a, end=' ')
#     a, b = b, a + b


# '''Q3:
# Program to find all factors of a number:
# '''
# num = int(input("Enter a number: "))

# print("Factors of", num, "are:")
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)


# '''Q4:
# Program to find the sum of all numbers in a list, excluding duplicates:
# '''
# lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# unique_lst = set(lst)
# sum_of_elements = sum(unique_lst)

# print(f"Sum of unique elements: {sum_of_elements}")


# '''Q5:
# Program to find the intersection of two lists:
# '''
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [4, 5, 6, 7, 8]
# intersection = list(set(lst1) & set(lst2))

# print(f"Intersection: {intersection}")