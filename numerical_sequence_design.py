# 1. Name:
#      Ashlee Hart
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program prompts the user for a number and calculates the given number in a sequnce created by the algorithm Fn = Fn-1 + Fn-2.
# 4. What was the hardest part? Be as specific as possible.
#      Unless I did it wrong, I don't think it was very difficult. It took me a while to think of which asserts to add and I feel like I 
#      missed some. The overall concept of the program was pretty easy and it didn't take me long to write. I did struggle to know where
#      to incude the cases for the first and second numbers in the equence. I just added an if/else statement before the while loop but 
#      I think there is a better way I could have done that. 
# 5. How long did it take for you to complete the assignment?
#      It tooke me about 4 hours to complete.

# Increase the number of digits allowed in the calculation and solution. 
import sys
sys.set_int_max_str_digits(0) 

if __debug__:

    # Make a loop so the user can try again if they enter a number <= 0. 
    done = False
    while done == False:

        # Prompt the user which Francois number in the sequence they would like to calculate.
        number = int(input("Which Francois number would you like to see? "))
        assert type(number) == int

        # Give the user an error message for numbers <= 0 and have them try again.
        if number <= 0:
            print("Please enter a valid number greater than 0.")

        # If the user enters a valid number exit the loop to calculate.
        else:
            done = True

    # Create a list with the first 2 numbers in the sequence.
    number_list = [2, 1]
    assert type(number_list) == list

    # Set iteration number to 1 and add one for each additional iteration.
    iteration_number = 1

    # Add cases for number = 1 and 2.
    if number == 1:
        sum = 2
    elif number == 2:
        sum = 1

    # Calculate the given number in the sequence.
    while iteration_number <= number - 2:
        assert type(iteration_number) == int, "Iteration number should be an integer."
        assert iteration_number >= 1, "Iteration number should be a positive integer."

        sum = number_list[0] + number_list[1]
        assert type(sum) == int, "Sum type must be an integer"
        assert type(number_list[0]) == int, "Items in numer_list must be positive integers."
        assert type(number_list[1]) == int, "Items in numer_list must be positive integers."

        number_list[0] = number_list[1]
        number_list[1] = sum
        assert sum > 0, "The sum should be a positive integer."
        assert len(number_list) == 2, "The length of number_list should never exceed 2 elements."

        iteration_number = iteration_number + 1

    # Return the calculated number to the user.
    print(f"Francois number {number} is {sum}.")