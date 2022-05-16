# # 1)Write a Python program to get a string from a given string where 
# # all occurrences of its "r" char have been changed to '$'.
# # example: 'restart'
# # Result : '$esta$t'



# txt = input("Print your text!  ")
# x = txt.replace("r", "$")
# print(x)



# # 2)Write a Python program to swap comma and dot in a string. 
# # Sample string: "32.054,23"
# # Expected Output: "32,054.23"


# my_num = "32.054,23"
# maketrans = my_num.maketrans
# my_num = my_num.translate(maketrans(".,", ",."))
# print(my_num)

# # kam


# txt = input()
# n = ""
# for i in txt:
#    if i == ",":
#       n = n + "."
#       continue
#    if i == ".":
#       n = n + ","
#       continue
#    else:
#       n = n + i
# print(n)






# # 3) Write a Python program to compute sum of digits of a given string


# givenstr = input("Write your string! ")
# sum_digits = 0
# for i in givenstr:
#     if i.isdigit():
#         sum_digits += int(i)

# print("Sum of digits is!", sum_digits)




# # 4)Write a Python program to remove spaces from a inputed sentence.

# inp_str = input("Enter your string! ")
# print(inp_str.replace(" ",""))



# # 5)Write python program to print even length words from inputed sentence.


# my_sentce_ = input("Enter your sentence! ")
# my_sentce_ = my_sentce_.split()
# for i in my_sentce_:
# 	if len(i) % 2 == 0:
# 		print(i)



# # 6)Write a program to count how many letters and numbers are in given word
# # Example: "2 + 2 is equal to 4"


# txt_ = "2 + 2 is equal to 4"
# numbers = 0
# letters = 0
 
# for i in txt_:
#    if i.isdigit():
#       numbers += 1
#    elif i.isalpha():
#       letters += 1

# print("There are", numbers, "numbers!")
# print("There are", letters, "letters!")


# # 7)Write a Python program to count the number of characters (character frequency) in a string.
# # example:"hello world"
# # output:
# # h 1
# # e 1
# # l 3


# given_str = "hello world"
# for i in given_str:
#    total = given_str.count(i)
#    print(str(i) + " " + str(total))



# #8) Write a Python script that takes input from the user and displays that input back in upper and lower cases. 

# user_input = input()
# print(user_input.upper())
# print(user_input.lower())


# # 9)Write a Python script that has a list and convert into comma separated string.
# # Sample list:['Geeks', 'for', 'Geeks']
# # output:Geeks-for-Geeks



# inp_list = ["Geeks", "for", "Geeks"]
# x = "-".join(inp_list)
# print(x)



# # 10)Python program to convert  starting letter of a word in upper case format or in the title format.
# # sample list: ["hello", "this", "is", "pythonlobby"]
# # output: Hello This Is Pythonlobby


# sample_lst = ["hello", "this", "is", "pythonlobby"]
# ch_str = ' '.join([str(i) for i in sample_lst])

# print(ch_str.title())


