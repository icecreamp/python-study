# Simple quiz game.py
# Date: 2/17/2023
# Author: Hyunjin Kim
# Reference: https://youtu.be/DLn3jOsNRVE

# print a message
print("Welcome to my computer quiz!")

# Get user input to start the game
playing = input("Do you want to play? enter yes if you want: ")

# Stop running the program if user does not want to play
if playing.lower() != "yes":
    quit()

# Display the message that the game has started
print("Okay! Let's play: ")
# A variable for tracking user's score
score = 0

# Get user input for the first question
answer = input("What does CPU stand for?: ").lower()

# Inform user if their answer is right or wrong
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("incorrect :( ")

# Get user input for the second question
answer = input("What does GPU stand for: ").lower()

# Inform user if their answer is right or wrong
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("incorrect :( ")

# Get user input for the thrid question
answer = input("What does RAM stand for: ").lower()

# Inform user if their answer is right or wrong
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("incorrect :( ")

# Get user input for the fourth question
answer = input("What does PSU stand for?: ").lower()

# Inform user if their answer is right or wrong
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("incorrect :( ")

# Display a message how many questions the user got
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%!")

