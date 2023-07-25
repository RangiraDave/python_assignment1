# Q1:

# Stud = {
#     "Nkuru": {"Age": 25},
#     "Habyara": {"Age": 28},
#     "Habibi": {"Age": 26}
# }
# for key, values in Stud.items():
#     if Stud.Age() > 25:
#         print(key, values)




# Q2:

# def char_frequency(s):
#     frequency = {}
#     for char in s:
#         frequency[char] = frequency.get(char, 0) + 1
#     return frequency



# Q3:

# def tuples_to_dict(tuples_list):
#     return dict(tuples_list)



# Q5:

# def inventory_system(inventory=None):
#     if inventory is None:
#         inventory = {}

#     def create(item, quantity):
#         inventory[item] = quantity

#     def read(item):
#         return inventory.get(item, 'Item not found')

#     def update(item, quantity):
#         if item in inventory:
#             inventory[item] = quantity

#     def delete(item):
#         if item in inventory:
#             del inventory[item]

#     return create, read, update, delete