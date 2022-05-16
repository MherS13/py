# my_num = int(input())
# if (my_num) % 5 == 0 and (my_num) % 7 == 0:
# 	print("fizzbuz")

# elif(my_num) % 7 == 0:
# 	print("fizz")
# elif(my_num) % 5 == 0:
# 	print("buzz")


# my_word = input()


# if(my_word == my_word[::-1]):
#       print("The string is a palindrome")
# else:
#       print("the string is not a palindrome")




# for i in range(5):
# 	x = int(input())
# 	if x > 18:
# 		print("he can")
# 	else:
# 		print("he cant")






#import random




# x = random.randint(1,10)
# y = int(input())
# while x != y:
#     y = int(input())
# else:
# 	print("you win")



# import random

# number = random.randrange(0, 100)
# for_guess = int(input("Guess the given number"))

# while for_guess != number:
#     if for_guess < number:
#         print("It is too low!")
#         for_guess = int(input("Guess the given number"))
#     else:
#         print("It is too high")
#         for_guess = int(input("Guess the given number"))

# print("You guessed the number")




#ete ka password ev paswordum ka 10 kam avel nish u ka 1 gone tiv ev 1 mecatar tpi chishte

my_str = input()
nums = 0
uppers = 0
for i in my_str:
	if i.isdigit():
		nums += 1
	elif i.isupper():
		uppers += 1
if len(my_str) >= 10 and uppers >= 1 and nums >= 1:
	print("correct")