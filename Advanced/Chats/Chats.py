# #Dictionaries:


# '''Q1:
# Write a Python program to sum all the items in a dictionary.
# '''
# my_dict = {'data1':100,'data2':-54,'data3':247}
# print(sum(my_dict.values()))


# '''Q2:
# Write a Python program to iterate over dictionaries using for loops.
# '''
# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for color_key, value in d.items():
#      print(color_key, 'corresponds to ', d[color_key]) 


# '''Q3:
# Write a Python program to sort a dictionary by key.
# '''
# color_dict = {'red':'#FF0000',
#             'green':'#008000',
#             'black':'#000000',
#             'white':'#FFFFFF'}

# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))


# '''Q4:
# Write a Python program to get the maximum and minimum value in a dictionary.
# '''
# my_dict = {'x':500, 'y':5874, 'z': 560}

# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])


# '''Q5:
# Write a Python program to remove duplicates from Dictionary.
# '''
# student_data = {'id1': 
#     {'name': ['Sara'], 
#         'class': ['V'], 
#         'subject_integration': ['english, math, science']
#     },
#     'id2': 
#     {'name': ['David'], 
#         'class': ['V'], 
#         'subject_integration': ['english, math, science']
#     },
#     'id3': 
#     {'name': ['Sara'], 
#         'class': ['V'], 
#         'subject_integration': ['english, math, science']
#     },
#     'id4': 
#     {'name': ['Surya'], 
#         'class': ['V'], 
#         'subject_integration': ['english, math, science']
#     },
# }

# result = {}

# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value

# print(result)