# Q1:

# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
# print('Dictionary in ascending order by value : ',sorted_d)
# sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)



# Q2:

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#     if x in d:
#         print('Key is present in the dictionary')
#     else:
#         print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)



# Q3:

# d = {'x': 10, 'y': 20, 'z': 30} 
# for dict_key, dict_value in d.items():
#     print(dict_key,'->',dict_value)




# Q4:

# n=int(input("Input a number "))
# d = dict()

# for x in range(1,n+1):
#     d[x]=x*x

# print(d) 




# Q5:

# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d)  
