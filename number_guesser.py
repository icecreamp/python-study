# Numer guesser game
# Date: 2/17/2023
# Author: Hyunjin Kim
# Reference: https://youtu.be/DLn3jOsNRVE

# import the moduel random
import random

# encourage users to enter a number
top_of_range = input("Type a number: ")

# if user enter a number, convert it into int
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

# if user enters a negative number, display an error message and quit the program
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()

# if user didn't enter a number, display an error message and quit the program
else:
    print("Please type a number next time.")
    quit()

# generate random number
# Method 1: print(random.randrange(startnumber, stopnumber)) (doesn't include stopnumber)
# Method 2: random,randrange(11) (Start from 0)
# Method 3: print(random.randrange(startnumber, stopnumber)) (include stopnumber)
random_number = random.randint(0, top_of_range)

# A variable for counting how many time the user tried to guess
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    # if all the characters are digits, convert the string to int
    if user_guess.isdigit():
        user_guess = int(user_guess)

    # if user enters a string, display an error message and continue
    else:
        print("Please type a number next time.")
        continue
    
    # when the user got the answer, stop the loop
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("Yout were below the number!")

print("You got it in ", guesses, " guesses")
