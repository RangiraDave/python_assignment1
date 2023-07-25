# Q1:

# def common_data(list1, list2):
#     return any(i in list1 for i in list2)

# print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))



# Q2:

# def long_words(n, str):
#     return filter(lambda word: len(word) > n, str.split())
    
# print(list(long_words(3, "The quick brown fox jumps over the lazy dog")))



# Q3:

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for i, x in enumerate(color) if i not in (0, 4, 5)]

# print(color)



# Q4:

# import heapq

# def second_smallest(numbers):
#     return heapq.nsmallest(2, set(numbers))[-1]

# print(second_smallest([1, 2, -8, -2, 0]))

# Q5:

# def sort_by_last(tuples):
#     return sorted(tuples, key=lambda x: x[-1])

# print(sort_by_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
