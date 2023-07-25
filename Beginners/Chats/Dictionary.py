# #Dictionaries:


# '''Q1:
# Write a program that creates a dictionary of names and ages, and then prints the names of people who are above a certain age:
# '''
# dictionary = {"Alice": 25, "Bob": 18, "Charlie": 30}
# age = 20
# above_age = [name for name, person_age in dictionary.items() if person_age > age]
# print(f"People above {age} years old: {above_age}")


# '''Q2:
# Create a program that counts the frequency of words in a given sentence using a dictionary:
# '''
# sentence = "apple banana apple strawberry banana lemon"
# words = sentence.split()
# frequency = {}
# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1
# print(f"Word frequencies: {frequency}")


# '''Q3:
# Write a program that converts a dictionary into a list of tuples:
# '''
# dictionary = {"Alice": 25, "Bob": 18, "Charlie": 30}
# list_of_tuples = list(dictionary.items())
# print(f"List of tuples: {list_of_tuples}")


# '''Q4:
# Create a program that finds the average age from a dictionary of people's ages:
# '''

# dictionary = {"Alice": 25, "Bob": 18, "Charlie": 30}
# average_age = sum(dictionary.values()) / len(dictionary)
# print(f"Average age: {average_age}")


# '''Q5:
# Write a program that checks if a key exists in a dictionary and retrieves its value:
# '''
# dictionary = {"Alice": 25, "Bob": 18, "Charlie": 30}
# key = "Alice"
# value = dictionary.get(key, "Key not found")
# print(value)