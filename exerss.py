import random

def compare_numbers(number, user_guess):
    cowbull = [0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1] += 1
        else:
            cowbull[0] += 1
    return cowbull


playing = True
number = str(random.randint(1000, 9999))
guesses = 0



while playing:
    user_guess = input("")
    if user_guess == "exit":
        break
    cb_count = compare_numbers(number, user_guess)
    guesses += 1

    print("You have " + str(cb_count[0]) + " cows, and " + str(cb_count[1]) + " bulls.")

    if cb_count[1] == 4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break
    else:
        print("Your guess isn't quite right, try again.")
