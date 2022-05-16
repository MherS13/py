#2)Write a program to display only those numbers from a list[12, 75, 150, 180, 145, 525, 50] 
#that satisfy the following conditions,
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop



# my_lst = [12, 75, 150, 180, 145, 525, 50]
# for i in my_lst:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)



# 3)Print First 10 natural numbers using while loop

# i = 1
# while i <= 10:
# 	print(i)
# 	i += 1



#8) Create a program that will display the numbers from 1 to 50 which is divisible by 7

# for i in range(1,50):
# 	if i % 7 == 0:
# 		print(i)


# 7)Write a program to keep asking for a number until you enter a negative number. 
# At the end, print the sum of all entered numbers.


# num_sum = 0
# while True:
#     x=int(input())
#     if x<0:
#         break
#     num_sum += x
# print(num_sum)


# 6)Count how many characters are in given sentence without spaces("Pyhton is awesome!.")


# my_str = "Pyhton is awesome!."

# number_of_characters = len(my_str) - my_str.count(" ")

# print(number_of_characters)









# 4)Write a Python program which have number (73421):
 # You should calculate (7 + 3 + 4 ….):


# num = (7,3,4,2,1)
# calc_num = 0
# for i in num:
#     calc_num += i
# print(calc_num)



# num = input()
# for i in num:
#     count += int(i)
# print(count)





# 1)Write a program to display the first 7 multiples of 7 using both(for, while) loops

# print("First seven multiples of 7")
# for i in range(1,8):
#     print(7*i)


# i = 1
# while i < 8:
#     n = i * 7
#     print(n)
#     i += 1

# i = 0
# mlt = 1
# while i < 7:
#     i += 1
#     mlt = i * 7
#     print(mlt)








# 5)Write a python program to compute the smallest
# number that is divisible by 2 inputed numbers


# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))
# i = 1
# while(i <= num1 and i <= num2):
#   if(num1 % i == 0 and num2 % i == 0):
#     smallest_divisibe = i
#   i = i + 1
# print("smallest_divisible is", smallest_divisibe)



# num_1= int(input())
# num_2 = int(input())
# i = 1
# while i > 0:
#     i += 1
#     if num_1 % i == 0 and num_2 % i == 0:
#         break
#         print(i)