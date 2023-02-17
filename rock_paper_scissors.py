# Rock paper scissors
# Date: 2/17/2023
# Author: Hyunjin Kim
# Reference: https://youtu.be/DLn3jOsNRVE

# import the module random
import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options: 
        continue

    # rock: 0, paper: 1, scissors: 2
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("The computer picked: ", computer_pick)
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("The computer picked: ", computer_pick)
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("The computer picked: ", computer_pick)
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, " times.")
print("The computer", computer_wins, " times.")
print("Goodbye!")