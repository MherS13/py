# 2)By using list comprehension, please write a program to print the list after removing the value
# 24 in [12,24,35,24,88,120,155]


# my_list = [12, 24, 35, 24, 88, 120, 155]
# try:
#     my_list = [i for i in my_list if i != 24]
#     print(my_list)
# except NameError as name_error:
#     print(name_error, "use the correct name")

# 4) Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


# try:
#     num = [1, 2, 3, 4]
#     print(["emp{0}".format(i) for i in num])
# except NameError as name_error:
#     print(name_error, "use defined name")
# except TypeError as type_error:
#     print(type_error, "use correct type")

#3)Write a program in Python that asks the user to input ten integers of their choice and return them a dictionary
# whose keys are the integers entered and whose values are the lists of divisors of the numbers entered.
# Example if the user enters the numbers: 2, 7,14, 9, 1, 4, the program returns the dictionary:
# d = {2: [1,2], 7: [1,7], 14: [1,2,7,14],1: [1], 4: [1,2,4]}.
# (try to use 'try except' if inputted value is not proper type)

# def list_divisor(number):
#     my_list = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             my_list.append(i)
#     return my_list
#
#
# my_number = []
# for i in range(0, 10):
#     try:
#       number = int(input("Please enter you number! "))
#       my_number.append(number)
#     except ValueError as value_error:
#         print(value_error, "Please print proper type of value!")
#
# my_dict = dict({})
# for number in my_number:
#     my_dict[number] = list_divisor(number)
# print(my_dict)


# 1) Ask the user for scientist’s name and birthday to add to the dictionary,
#  and update the JSON file you have on disk with the scientist’s name.
#  If you run the program multiple times and keep adding new names,
#  your JSON file should keep getting bigger and bigger.


# import json
#
# filename = "text.json"
#
# user = [
#     {"name": "scientist1", "birthday": 1950},
#     {"name": "scientist2", "birthday": 1960},
#     {"name": "scientist3", "birthday": 1970}
# ]
# try:
#    with open(filename, "w") as file:
#       json.dump(user, file)
# except FileExistsError as file_exists_error:
#     print(file_exists_error, "file exists")


