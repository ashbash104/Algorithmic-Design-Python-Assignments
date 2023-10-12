# Week 01 Guessing Game Lab
# 1. Name:
#      Ashlee Hart
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      This program has the user input a random positive integer, generates a random number
#      in that range, and has the user guess it in the lest number of guesses. It then
#      displays the number of guesses it took to get the right number.
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out how to combine the while loop with the if statements and track the guesses.
# 5. How long did it take for you to complete the assignment?
#      It took me about 2 hours because I am really rusty in Python.
# Display the program name
print('This is the "Guess a Number" game.')
# Display the game description
print('Try to guess a random number in the smallest number of attempts')
print()
# Have the user input a random positive integer
# I still need to make the number bold and underlined

integer = int(input("Pick a positive integer: "))
# Import random library
import random
# Generate a random number between 0 and the integer chosen by the user
secret_number = random.randint(0,integer)
# Dispay message with game instructions
print(f"Guess a number between 0 and {integer}")
# Create a new list where guesses can be stored
guesses_list = []
guess = int(input("> "))
guesses_list.append(guess)
while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
        # Get new guess
        guess = int(input("> "))
        # Add the guess to list of guesses
        guesses_list.append(guess)
    elif guess > secret_number:
        print("Too high!")
        # Get new guess
        guess = int(input("> "))
        # Add the guess to list of guesses
        guesses_list.append(guess)
    elif guess == secret_number:
        print(secret_number)
        print(guesses_list)
        
    else:
        quit()
# Display the ending statment with number of guesses it took user to get the right number.
guesses = len(guesses_list) # +1
print(f"You were able to find the number in {guesses} guesses!")
print(f"The numbers you guessed were: {guesses_list}")
