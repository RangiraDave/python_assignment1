# #Lists:


# '''Q1:
# Write a Python program to find the list of words that are longer than n from a given list of words.
# '''
# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len	
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# '''Q2:
# Write a Python function that takes two lists and returns True if they have at least one common member.
# '''
# def common_data(list1, list2):
#     result = False
#     for x in list1:
#         for y in list2:
#             if x == y:
#                 result = True
#                 return result
#     return result
# print(common_data([1,2,3,4,5], [5,6,7,8,9]))


# '''Q3:
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# '''
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)


# '''Q4:
# Write a Python program to find the second smallest number in a list.
# '''
# def second_smallest(numbers):
#     if (len(numbers)<2):
#         return
#     if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#         return
#     dup_items = set()
#     uniq_items = []
#     for x in numbers:
#         if x not in dup_items:
#             uniq_items.append(x)
#             dup_items.add(x)
#     uniq_items.sort()    
#     return  uniq_items[1]   

# print(second_smallest([1, 2, -8, -2, 0]))


# '''Q5:
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# '''
# def last(n): return n[-1]

# def sort_list_last(tuples):
#     return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2