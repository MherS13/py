# # 1)Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# # print out a message of congratulations to the winner,
# #  and ask if the players want to start a new game)
# # Remember the rules:
# # Rock beats scissors
# # Scissors beats paper
# # Paper beats rock
#
# p1_ch = input("P1 choose your game item ")
# p2_ch = input("P2 choose your game item ")
#
#
# def game(player_1, player_2):
#     game_list = ["rock", "paper", "scissors", "Rock", "Scissors", "Paper"]
#
#     while player_1 not in game_list or player_2 not in game_list:
#         print("Please give a correct game item.")
#         player_1 = input("Player 1 Enter rock, paper, scissors: ")
#         player_2 = input("Player 2 Enter rock, paper, scissors: ")
#
#     while player_1 == player_2:
#         print("Nobody wins. Try again")
#         player_1 = input("Player 1, Enter rock, paper,scissors: ")
#         player_2 = input("Player 2, Enter rock, paper, scissors: ")
#
#     if player_1 == "rock" and player_2 == "paper":
#         print("Congratulations Player 2 wins!")
#
#     elif player_1 == "paper" and player_2 == "rock":
#         print("Congratulations Player 1 wins!")
#
#     elif player_1 == "rock" and player_2 == "scissors":
#         print("Player 1 wins!")
#
#     elif player_1 == "scissors" and player_2 == "rock":
#         print("Congratulations Player 2 wins")
#
#     elif player_1 == "paper" and player_2 == "scissors":
#         print("Congratulations Player 2 wins!")
#
#     elif player_1 == "scissors" and player_2 == "paper":
#         print("Congratulations Player 1 wins!")
#
#
# game(p1_ch, p2_ch)
#
# # 2)A year is called a leap year if it contains an additional day which makes the number of the days in that year is 366.
# # This additional day is added in February which makes it 29 days long.
# # A leap year occurred once every 4 years.
# # How to determine if a year is a leap year?
#
#
# def leap_year(year):
#   if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
#     print("Given Year is a leap Year")
#   else:
#     print("Given Year is not a leap Year")
#
#
# check_year = int(input("Enter the number: "))
# leap_year(check_year)
#
# # 4)Get the factorial of number 6 using recursion.
#
#
# def factorial_recursive(n):
#    if n == 1:
#        return 1
#    else:
#        return n * factorial_recursive(n-1)
#
#
# print(factorial_recursive(6))
#
# # 5)Write a Python program to calculate the sum of the positive and negative numbers of a
# # given list of numbers using lambda function.
# # Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# # Sum of the positive numbers: -32
# # Sum of the negative numbers: 48
#
# original_list = [2, 4, -6, -9, 11, -12, 14, -5, 17]
#
# calculate_negative = list(filter(lambda x: x < 0, original_list))
# calculate_positive = list(filter(lambda x: x > 0, original_list))
#
# print("sum of negative numbers is", sum(calculate_negative))
# print("sum of positive numbers is", sum(calculate_positive))

# 3)Use a dictionary comprehension to count the length of each word in inputted sentence.


my_dic = input()
dic_result = {my_dic: len(my_dic) for my_dic in my_dic.split()}
print(dic_result)
