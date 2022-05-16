# 1)Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


def reverse_a_string(string):
    reversed_string = ""
    for i in string[::-1]:
        reversed_string += i
    return reversed_string


string = "1234abcd"
print(reverse_a_string(string))


# 2) Write a Python program that accepts a hyphen-separated sequence of words as input
# and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow


def hyphen_separated_sequence(word):
  ch_str = word.split('-')
  ch_str.sort()
  sort_str = '-'.join(ch_str)
  return sort_str


print("green-red-yellow-black-white")

sample_items = "green-red-yellow-black-white"
print(hyphen_separated_sequence(sample_items))


# 3)Write a Python program to print the floating numbers up to 2 decimal places

def floating_number(number):
    format_float = "{:.2f}".format(number)
    return format_float

given_num = float(input("Enter your floating number! "))
print(floating_number(given_num))


# 4)Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

from random import randint

def generate_number():
	random_number = randint(0, 9)
	return random_number

def main():
	the_number = generate_number()
	while True:
		print("Guess the number")
		number = int(input())

		if number == the_number:
			print("you guessed the number")
			print("The correct number is " + str(number))
			break
		elif number > the_number:
			print("Try lower")
		elif number < the_number:
			print("Go higher")

main()


# 5)Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def list_divisors(number) :
    i = 1
    while i <= number :
        if (number % i == 0) :
            print (i,end =" ")
        i += 1
        
print ("Enter the number to find the divisor! ")
list_divisors(int(input()))

