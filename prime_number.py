# 1. Name:
#      Ashlee Hart
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This program calculates all of the prime numbers below a given number.
# 4. What was the hardest part? Be as specific as possible.
#      I had to change the design from the psuedocode I made so it took me a while to 
#      realize that I would have to use the index for certain things since the list
#      is just a bunch of boolean values.
# 5. How long did it take for you to complete the assignment?
#      The assignment took me about 4 hours.

# Create a while loop so the user can enter a valid number greater than 1.
done = False
while done == False:
    assert type(done) == bool
    number = int(input("This program will find all the prime numbers at or below N. Select that N: "))
    if number < 2:
        assert type(number) == int
        print("Enter an integer greater than 1.")
    else:
        done = True
# Create a list with values of True for each number.
numbers = [True] * (number + 1)
assert len(numbers) >= number
assert len(numbers) > 0
assert type(numbers) == list
# This is for a test.
#print(numbers)

# Set 0 and 1 to False because they will never be prime numbers.
numbers[0] = False
numbers[1] = False
# This is for a test.
#print(numbers)

# Set each multiple of prime numbers above that number to False.
for index in range(2, number + 1):
    assert type(index) == int
    assert (number + 1) > 2
    # This is for a test.
    #print(f"Index: {index}")
    if numbers[index] != False:
            for i_numbers in range(index * 2, number + 1, index):
                numbers[i_numbers] = False
                # This is for a test.
                #print(f"Number array: {numbers}")

# Filter out False to return only prime numbers.
print(f"The prime numbers at or below {number} are:", end=" ")
for i, prime in enumerate(numbers):
    assert type(i) == int
    if prime:
        # Print the prime numbers on the same line. 
        print(i, end=", ")

