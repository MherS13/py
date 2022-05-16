# 1)Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.



def reverse_word(string):
    return ' '.join(string.split(' ')[::-1])



print(reverse_word(input('Please input a sentence:')))


1.2

given_string = input("Please enter your name!  ")
words = given_string.split()
words = list(reversed(words))
print(" ".join(words))


# 2) You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.



low_num = 0
high_num = 100
print("Please guess the number between 0 and 100!")
while True:
    guess = (high_num + low_num)//2
    print("Is your secret number " + str(guess) + " ?")
    guessed_num = input("Enter 'high' to check the guess is too high. Enter" 'low' "to check the guess is too low. Enter 'correct' to check I guessed correctly.")
    if guessed_num == 'correct':
        print("You win.Your secret number was:", str(guess))
        break
    elif guessed_num == "low":
        low_num = guess
    elif guessed_num == "high":
        high_num = guess
    else:
        print( "I did not understand your number.")





# 3)Take two lists, say for example these two:



#     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
# and write a program that returns a list that without duplicates. 
# Use list comprehension!


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 3, 13, 25, 12, 33, 27, 13, 55, 89]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)





#4) Write a Python program to return a new set with unique items from both sets by removing duplicates.

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {70, 40, 10, 50, 20, 60, 30}


set_1 = {10, 20, 30, 40, 50}
set_2 = {30, 40, 50, 60, 70}

set_2.update(set_1)

print(set_2)

#4.2

set_1 = {10, 20, 30, 40, 50}
set_2 = {30, 40, 50, 60, 70}

print(set_1.union(set_2))



#5) Remove items from set1 that are not common to both set1 and set2
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))



# 6)input a text and add vowels in set 


vowels =["a","e","i","o","u", "A", "E", "I", "O", "U",]
my_text = input("Enter your text! ")
add_vowels = set(my_text)
result = add_vowels.intersection(vowels)
print(result)



