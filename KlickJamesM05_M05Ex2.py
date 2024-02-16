#Random Number Guessing Game
#Version 1.0 - 2/16/2024
#This program will generate a random number. It will then allow the user to guess the number, telling them high or low until the guess correctly.

import random

def random_number():
    random_goal = random.randint(1,100)
    return random_goal


def random_guess(random_goal):
    guess = int(input("Guess the number between 1 and 100: "))
    guess_value = 0
    if guess == random_goal:
        guess_value = 1
    elif guess < random_goal:
        guess_value = 2
    else :
        guess_value = 3
    return guess_value
 

random_goal = random_number()
guess_value = 0
guess_count = 0


while guess_value != 1:
    guess_value = random_guess(random_goal)
    guess_count = guess_count + 1
    if guess_value == 2:
        print("Your guess is too low, try again")
    elif guess_value == 3:
        print("Your guess is too high, try again")
else:
    print("You got it! The number was " + str(random_goal))
    print("Number of guess needed: " + str(guess_count))
