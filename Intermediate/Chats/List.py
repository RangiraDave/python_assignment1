# Lists:

# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# python
# Copy code

# def match_words(words):
#     ctr = 0

#     for word in words:
#         if len(word) > 1 and word[0] == word[-1]:
#             ctr += 1
#     return ctr
# print(match_words(['abc', 'xyz', 'aba', '1221']))
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# python
# Copy code
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)


# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# python
# Copy code
# def last(n): return n[-1]
# def sort_list_last(tuples):
#     return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# Write a Python program to remove duplicates from a list.
# python
# Copy code
# a = [10,20,30,20,10,50,60,40,80,50,40]

# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)


# Write a Python program to append a list to the second list.
# python
# Copy code
# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# final_list = list1 + list2
# print(final_list)