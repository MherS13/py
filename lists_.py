#3)Write a Python program to get the difference between the two lists

# inpList_1 = [1,2,3,4,5]
# inpList_2 = [3,4,5,6,7]

# list_difference = set(inpList_1).symmetric_difference(set(inpList_2))
# inp_difference = list(list_difference)
# print(inp_difference)

# #tarberak 2

# inpList_1 = [1,2,3,4,5]
# inpList_2 = [3,4,5,6,7]
# for i in inp_list_1:
# 	for j in inp_list_2:
# 		if i != j:
# 			print(i)




# # 4) Write a Python program to find the second smallest number in a list.


# check_list = [10, 20, 30, 40, 50]
# check_list=[i for i in check_list if i != min(check_list)]  
# print(min(check_list))


# inpList_1 = [1,5,2,7,9]
# print(sorted(inpList_1)[1])



# # 5)Getting the first three items of a list

# list_for_check = ["python", "is", "awesome","and", "the", "best"]
# print(list_for_check[0:3])




# # 6)Write a Python program to remove duplicates from a list.



# given_lst = [100, 100, 200, 200, 300, 400, 500]
# given_lst = list(dict.fromkeys(given_lst))
# print(given_lst)


# #tarberak 2

# given_lst = [100, 100, 200, 200, 300, 400, 500]
# removed_duplicates = []
# for i in given_lst:
#     if i not in removed_duplicates:
#         removed_duplicates.append(i)
# given_lst = removed_duplicates
# print(given_lst)



# # 2)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

# sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(sample_list[1:-2])



# sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(sample_list[1:4])


# #1) Write a Python program that takes two lists and returns True if they have at least one common member.

# inp_list_1 = [1, 2, 3, 4, 5]
# inp_list_2 = [5, 6, 7, 8, 9]
# for i in inp_list_1:
# 	for j in inp_list_2:
# 		if i == j:
# 			print(True)
            
