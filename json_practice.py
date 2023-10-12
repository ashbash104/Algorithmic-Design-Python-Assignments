# Practice with json files.

# Put "Hello World" on the screen.
print("Hello World!")

# Put "I was born in 1971" on the screen where 1971 is an integer.
birth_year = 1971
print("I was born in " + str(birth_year))

# Promt the user for his or her name and display it on the screen. 
name = input("What is your name? ")
print(f"Your name is: {name}")

# Prompt user for their birth year and display his or her age.
year = int(input("What is your birth year? "))
age = 2023 - year
print("You are " + str(age) + " years old this year.")

# Try the name.txt file. 
# This will write "Ashlee Hart" to the name.txt file.
try:
    file = open("name.txt", "w")
    file.write("Ashlee Hart")
    file.close()
except OSError:
    print("Unable to write to name.txt")

# Another option to write to text file, commented out for reference.
# with open("name.txt", "w") as file:
#    file.write("Ashlee")

# Read name from name.txt file and display it on the screen.
try:
    file = open("name.txt", "r")
    print(file.readline())
    file.close()
except FileNotFoundError:
    print("Check the file path.")

# Create a simple JSON construct with at least two attributes and a list.
dictionary = {
    "name" : "Ashlee",
    "age" : "23",
    "hobbies" : ["running", "crocheting", "hiking", "drawing"]
}
i_pivot = 3-1
i_largest = 0
i_check = 0
while i_pivot > 0:							    # D
    for each in dictionary[0, i_pivot]:
        if i_check > i_pivot:			   
            i_pivot == i_check and i_check == i_pivot # F


# Take the above JSON file, turn it into a string, and write it to a file using "dumps".
import json
text = json.dumps(dictionary)
with open("dictionary.json", "w") as file:
    file.write(text)

# Read the JSON file made above back into a dictionary using "loads" and display.
# This will be very helpful for the lab due Saturday. 
with open("dictionary.json", "r") as file:
    text2 = file.read()
    dictionary2 = json.loads(text2)
    print(text2)

# Put any 10 numbers in an array (list). 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number)

# Display the first 3 numbers in the list on the screen. 
print("The first 3: ", numbers[:3])

# Display the middle 3 numbers on the screen.
print("The middle 3 numbers: ", numbers[4:7])

# Display the last 3 numbers on the screen. 
print("The last 3 numbers: ", numbers[-3:])

# Create a tuple with the values 1, 1.1. Display each value independently. 
tuple = 1, 1.1
print("Tuple =", tuple)
print(tuple[0])
print(tuple[1])

# Create a tuple with values "two", "True", and "(2, 2+2j)". Display values independently.
tuple_one = "two", True, (2, 2+2j)
print(tuple_one[0])
print(tuple_one[1])
print(tuple_one[2])