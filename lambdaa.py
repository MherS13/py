# 1) Use the sorted() function to sort the list in ascending order with lambda.

my_list = ['5', '4', '3', '1', '6', '7']
sorted_list = sorted(my_list, key=lambda x: int(x[0:]))
print(sorted_list)

# 2) Write a Python program to sort each sublist of strings in a given list of lists using lambda.
# Original list using lambda:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

given_list = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
print((sorted(given_list, key=lambda x: x[0])))


# 3)Write a Python program to count float number in a given mixed list using lambda.
# Original list:
# [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]


def count_integer(list1):
    f_list = list(map(lambda i: isinstance(i, float), list1))
    result = len([i for i in f_list if i])
    return result


mixed_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(count_integer(mixed_list))


# 4)Write a Python program to count the occurrences of the items in a given list using lambda. Go to the editor
# Original list:
# [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}


def count_occurrences(numbers):
    count_occ_list = dict(map(lambda x: (x, list(numbers).count(x)), numbers))
    return count_occ_list


original_list = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
print(count_occurrences(original_list))

# 5)Write a Python program to remove None values from a given list using lambda function. Go to the editor
# Original list:
# [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None values from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]


original_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
result_list = list(filter(lambda x: x is not None, original_list))

print(result_list)

# 6)  Write a Python program to check whether a given string is number or not using Lambda.


my_Num = lambda x: x.isdigit()
print(my_Num("1"))
print(my_Num("2"))
print(my_Num("a"))
print(my_Num("3"))

# # 7)Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
# # Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]

Arrays = [-1, 2, -3, 5, 7, 8, 9, -10]
result = sorted(Arrays, key=lambda x: 0 if x == 0 else -1 / x)
print(result)



