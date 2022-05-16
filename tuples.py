# # 1)Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to222
# # example:tuple1 = (11, [22, 33], 44, 55)
# # output:tuple1 = (11, [222, 33], 44, 55)


# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0] = 222
# print(tuple1)


# # 2)Write a Python program convert a given string list to a tuple.
# # Original string: python 3.0
# # <class 'str'>
# # Convert the said string to a tuple:
# # ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')


# given_string = "python 3.0"
# print("Original string is", given_string)
# print(type(given_string))
# converted_string_list = tuple(given_string)
# print(f"The converted string is! {converted_string_list}")



# # 3)Check if all items in the tuple are the same


# tuple_items = ("Hallo", "Hallo", "Hallo", "Hallo")
# if(len(set(tuple_items)) == 1):
# 	print("All items in the tuple are the same")
# else:
# 	print("All items in the tuple are not the same")

# 3.2

# tuple_items = ("Hallo", "Hallo", "Hallo", "Hallo")
# if tuple_items.count(tuple_items[0]) == len(tuple_items):
# 	print("All items in the tuple are the same")
# else:
#  	print("All items in the tuple are not the same")



# # 5)Write a Python program to check if two given sets have no elements in common.

# given_set1 = {1, 2, 3, 4, 5, 7}
# given_set2 = {55, 12, 9, 3, 7, 1}


# if given_set1.isdisjoint(given_set2):
#   print("There are no common elements in set")
# else:
#   print("The sets have elements in common")
#   print(given_set1.intersection(given_set2))


# 5.2

# given_set3 = given_set1.isdisjoint(given_set2)
# print(given_set3)



# # 6)Write a Python program to convert a tuple to a string

# my_tuple = ("hello", "world")
# my_string = ' '.join(my_tuple)
# print(my_string)


# #7)Write a Python program to convert a tuple of string values to a tuple of integer values.
# # Original tuple values:
# # (('333', '33'), ('1416', '55'))
# # New tuple values:
# # ((333, 33), (1416, 55))


# original_tuple = (("333", "33"), ("1416", "55"))
# print(tuple((int(i),int(j)) for i , j in original_tuple))





# 4)Get the maximum and minimum values for set without max() and min() and without cast to list


# nums_for_set = {9,7,3,5,10,13}
# min_value = 13
# max_value = 0
# for i in nums_for_set:
#     if i > max_value:
#         max_value = i
# for i in nums_for_set:
#     if i < min_value:
#         min_value = i
# print(f"The max value in set is {max_value}")
# print(f"The min value in set is {min_value}")



# set_1 = {9, 7, 3, 10, 13, -13, -3}
# max_value = set_1.pop()
# min_value = max_value

# for i in set_1:
#     if i > max_value:
#         max_value = i
# for j in set_1:
#     if i < min_value:
#         min_value = j
# print(f"the maximum value of the det is {max_value} and the minimum value of the set is {min_value}")




# list_1 = [9, 7, 3, 10, 13, -13, -3]
# # max_value = list_1[0]
# # for i in list_1:
# #     if i > max_value:
# #         max_value = i
# # print(max_value)


# min_value = list_1[-1]
# for i in list_1:
#     if i < min_value:
#         min_value = i
# print(min_value)        

