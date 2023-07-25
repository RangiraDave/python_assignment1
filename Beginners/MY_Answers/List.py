# Q1:

# L = [2, 3, 34, 54, 5, 5, 75, 643, 23, 23, 32, 43, 3, 5, 4, 564, 34, 34, 4, 43, 43, 43, 43, 4, 34, 3, 3, 32, 3, 5, 3]
# q = int(input("Whats the spesfic element? "))
# j = 0
# for i in range(0, len(L) - 1):
#     if q == L[i]:
#         j += 1
# print(j)



# Q2:

# Alch_Drinks = ['Gatanu', 'Mutsig', 'Skol', 'Primus']
# Non_Alch_Drinks = ['Milk', 'Water', 'Juice', 'Soda']
# print("The combined List Is:  ", Alch_Drinks + Non_Alch_Drinks)



# Q3:

# L = [2, 6, 7, 12, 24, 34, 1, 9]
# mx = mn = 0
# m = len(L)
# for i in range(0, m - 1):
#     for j in range(m - 1, 0):
#         if L[j] >= L[i]:
#             mx = L[j]
#             mn = L[i]
#         elif L[i] == L[j]:
#             continue
# print("Maximum: ", mx)
# print("Minimum: ", mn)




# Q4:

# New = list(set(input("Enter elements in your list:")))
# print("Here is your entered elements without duplicates: ",New)



# Q5:

# lst1 = ['Bannanas', 'Rice', 'Flour', 'Meat', 'Beans']
# print(lst1[::-1])