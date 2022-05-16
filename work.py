# 1)Input a  number and check if it is even or odd number.
'''
number = int(input("Enter number to check it is even or odd"))
formula = number % 2
if (formula == 0):
   print(number,"is an even number")
else:
   print(number,"is an odd number")

# 2)input a string and check if there is 'a' character print appropriate 
# output(for example "there is 'a' character in inputed string"), else print opposite output.

my_str = input()
if "a" in my_str:
	print("there is 'a' character in inputed string")
else:
	print("there is not 'a' character in inputed string")


# 3)input 3 numbers and check which is the biggest and print appropriate output.


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_3 > num_2 and num_3 > num_1:
   print("num_3 is the greatest")
elif num_2 > num_1 and num_2 > num_3:
   print("num_2 is the greatest number")
else:
  print("num_1 is the greates number")


# 4)input a string and print out all characters  of  string using for loop.


_my_str = input()
for i in _my_str:
	print(i)


# 5)[1,2,3,4,5] sum all elements inside list using for loop and  assignment operator.


my_lst = [1,2,3,4,5]
ammount = 0
for i in my_lst:
	ammount += i
print(ammount)

'''

# 6)input 3 string and check which is the longest word and print appropriate output.

# str_1 = input()
# str_2 = input()
# str_3 = input()

# if len(str_1) > len(str_2) > len(str_3):
#    print("str_1 is the longest")
# elif len(str_3) > len(str_2) > len(str_1):
#    print("str_3 is the longest")
# else:
#    print("str_2 is the longest")






# 7)Input a string and count the length of the string, if length of string is less than 10,print ‘short word’, 
# elif  greater than 10, print ‘long word’, else ‘too long word’.

# the_str = input()
# if len(the_str) < 10:
# 	print("short word")
# elif len(the_str) > 10:
# 	print("long word")
# else:
# 	print("too long word")


# 8)Input a number and check, if the number divides by 5,print(“ﬁzz”),
# elif the number divides by 7,print(“buzz”),elif the number divides by 5 and 7 print(“ﬁzbuzz”).


# num = int(input())
# if (num) % 5 == 0 and (num) % 7 == 0:
#    print("fitbuzz")

# elif (num) % 7 == 0:
#    print("buzz")
# elif (num) % 5 == 0 :
#    print("fizz")


# # 9)check how many ‘a’ characters are in inputed string using for loop and assingment operator.

# x = 0
# my_str = input()
# for i in my_str:
#    if i == "a":
#       x += 1
# print(x)


# # 10)[1,2,3,4,5] multiply all elements inside list using for loop and  assignment operator.

# _my_lst = [1,2,3,4,5]
# ammount = 1
# for i in _my_lst:
# 	ammount *= i
# print(ammount)


# 11)[4, 50,37, 56, 71,14] print all numbers that are greater or equal 50.

# my_lst_ = [4, 50,37, 56, 71,14]
# for i in my_lst_:
#    if i >= 50:
#       print(i)
      

# # 12)input a string and check if a or b is in inputed string and print appropriate output.

# ch_str = input()
# if any(i in ch_str for i in ("a", "b")):
#    print (True)
# else:
#    print (False)