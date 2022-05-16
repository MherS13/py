# # 1)Write a Python program to match key values in two dictionaries.
# # Sample dictionary:dict_1= {'key1': 1, 'key2': 3, 'key3': 2},dict2 = {'key1': 1, 'key2': 2}
# # Expected output: key1: 1 is present in both dict_1 and dict_2

# dict_1 = {"key1": 1, "key2": 3, "key3": 2}
# dict_2 = {"key1": 1, "key2": 2}

# for i in dict_1:
#  	if i in dict_2:
#  		if dict_1[i] == dict_2[i]:
# 		    print("key1: 1 is present in both dict_1 and dict_2")





# # 2) Write a Python program to drop empty Items from a given Dictionary.
# # Original Dictionary:
# # {'c1': 'Red', 'c2': 'Green', 'c3': None}
# # New Dictionary after dropping empty items:
# # {'c1': 'Red', 'c2': 'Green'}


# original_dict = {"c1": "Red", "c2": "Green", "c3": None}

# original_dict = {i:j for i, j in original_dict.items() if j is not None}
# print(original_dict)



# # 2.2
# original_dict.popitem()
# print(original_dict)

# #2.3

# # original_dict.pop("c3")
# # print(original_dict)



# # 3)A Python Dictionary contains List as value. Write a Python program to update the list values 
# #in the said dictionary.
# # Original Dictionary:
# # {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# # Update the list values of the said dictionary:
# # {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}

# given_dict = {"Math": [88, 89, 90], "Physics": [92, 94, 89], "Chemistry": [90, 87, 93]}

# given_dict["Math"][0] += 1
# given_dict["Math"][1] += 1
# given_dict["Math"][2] += 1

# given_dict["Physics"][0] -= 2
# given_dict["Physics"][1] -= 2
# given_dict["Physics"][2] -= 2

# print(given_dict)

#given_dict["Math"] = [i + 1 for i in given_dict["Math"]]
#given_dict["Physics"] = [i - 2 for i in given_dict["Physics"]]

# # 4)Get a dictionary from 2 lists

# key = ["name", "age", "city"]
# value = ["Mher", 29, "Yerevan"]
# get_dictionary = dict(zip(key, value))
# print(get_dictionary)


# # 4.2 


# keys = ["name", "age", "city"]
# values = ["Mher", 29, "Yerevan"]
# get_dictionary = {}
# for i in keys:
#     for j in values:
#         get_dictionary[i] = j
#         values.remove(j)
#         break
# print(get_dictionary)  



# # 5) Write a Python script to generate and print a dictionary that contains a 
# # number (between 1 and n) in the form (x, x*x).
# # Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



# inputed_number = 5
# result = dict()

# for i in range(1, 6):
#     result[i]=i*i
# print(result) 


# # 5.2

# inputted_number = 5
# result={i:i*i for i in range(1, 6)}
# print(result)






# # 6)Write a Python program to get the top three items in a shop.
# # Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# # Expected Output:
# # item4 55
# # item1 45.5
# # item3 41.3



# dicts_items = {"item1": 45.50, "item2":35, "item3": 41.30, "item4":55, "item5": 24}
# for i,j in sorted(dicts_items.items(),key=lambda x:x[1],reverse=True)[:3]:
#     print(i,j)


# #6.2

# dict_items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# big_values = sorted(dict_items.values(),reverse=True)[:3]
# for i,j in dict_items.items():
#     if dict_items[i] in big_values:
#         result = {i:j}
#         print(result)

# dict_items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# big_values = sorted(dict_items.values(),reverse=True)[:3]
# for i in big_values:
#     for k,v in dict_items.items():
#         if i == v:
#             print(k,v)

















