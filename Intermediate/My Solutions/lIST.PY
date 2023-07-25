# Q1:

# def match_words(words):
#     ctr = 0

#     for word in words:
#         if len(word) > 1 and word[0] == word[-1]:
#             ctr += 1
#     return ctr

# print(match_words(['abc', 'xyz', 'aba', '1221']))




# Q2:

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)




# Q3:

# def last(n): return n[-1]

# def sort_list_last(tuples):
#     return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))




# Q4:

# a = [10,20,30,20,10,50,60,40,80,50,40]

# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)





# Q5:

# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# final_list = list1 + list2
# print(final_list)
