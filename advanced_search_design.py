# 1. Name:
#      Ashlee Hart
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program will get a file name from the user and load
#      it into a json file, then format it as a list. It will prompt
#      the user for an element and perform a binary search in the list and return found if
#      the element is in the list or return not found if not in the list. 
# 4. What was the hardest part? Be as specific as possible.
#      I've never done asserts before so it definitely wasn't intuitive
#      for me to know where to put them. I put them in the beggining, middle, and end to check
#      the file, index, and output but I spent a lot of time just thinking about it. It was also 
#      hard to implement the sort. I kept changing it and couldn't get it to work.
# 5. How long did it take for you to complete the assignment?
#      It took me around 3 hours to work on this assignment. 

# We will use JSON so import JSON
import json

valid = False
while valid == False:
# Display the filenames the user can choose from.
    options = ("""
        0. Empty file (Lab06.empty.json)  
        1. File with 1 entry (Lab06.trivial.json)   
        2. Small list (Lab06.languages.json)
        3. Medium list (Lab08.states.json)
        4. Large list (Lab08.cities.json)
        """)
    print(options)

    # Prompt the user for the file.
    option = int(input("Please choose a file name (0-4): "))

    # Define the options as the associated file name.
    if option == 0:
        fileName = "Lab06.empty.json"
        valid = True
    elif option == 1:
        fileName = "Lab06.trivial.json"
        valid = True
    elif option == 2:
        fileName = "Lab06.languages.json"
        valid = True
    elif option == 3:
        fileName = "Lab08.states.json"
        valid = True
    elif option == 4:
        fileName = "Lab08.cities.json"
        valid = True 
    else:
        print("Please choose a valid option.")
    assert type(option) == int

# Open the file, read it, and load it into a json file. 
names_list = []

with open(fileName, "r") as file:
    names_text = file.read()
    file.close()
    names_json = json.loads(names_text)
    if len(names_list) != 0: assert type(names_list) == []

    # Convert the json file into a list.
    names_list = names_json['array']

# Perform sort function to alphabetize the file.
def sort(names_list, word):
    i_pivot = len(names_list) - 1
    i_largest = 0
    while i_pivot > 0:
        # [0, len(names_list) - 1]
        for i_check in names_list[0, i_pivot]:
            if names_list[i_check] > names_list[i_largest]:
                names_list[i_largest] = names_list[i_check]
            if names_list[i_largest] > names_list[i_pivot]:
                names_list[i_pivot], names_list[i_largest] = names_list[i_largest], names_list[i_pivot]
                i_pivot = i_pivot - 1
    return names_list
print(f"The values in the file are: ")
for word in names_list:
    print(f"    {word}")
# Get an element from the user.
element = input("Please enter an element to search for: ")
assert type(element) == str, "Element can't compare to string"
sort(names_list, element)

print(f"The values in the file are: ")
for word in names_list:
    print(f"    {word}")


# First index = 0
i_first = 0

# End index is the length of the list.
i_end = len(names_list)
assert type(len(names_list)) == int, "Invalid length"

done = False
while done == False:

    # If the file is empty display message to user.
    if len(names_list) == 0:
        print("The file is empty.")
        done = True
        exit() # I know this is bad, I just can't figure out how to make it work another way.

    # While the end index (i_end) - first index (i_first) > 1, perform the search function.
    while i_end - i_first > 1:
        assert 0 <= i_first <= len(names_list), "Invalid index"
        assert 0 <= i_end <= len(names_list), "Invalid index"

        # Get middle index
        i_middle = (i_first + i_end) // 2 
        assert 0 <= i_middle <= len(names_list), "Invalid index"

        # Move the first or last index to the middle depending on the value.
        if names_list[i_middle] <= element:
            i_first = i_middle
            print("Working 1") #(This was a test).
        else: 
            i_end = i_middle
            print("Working 2") #(This was also a test).

    # If the element is in the list display "Found" to the user. 
    if names_list[i_first] == element:
        assert type(names_list[i_first]) == str
        assert type(element) == str
        print("Found")
        done = True

    # If the list is empty display message to user that it is empty and not found.
    #elif valid == False:
        #print("List is empty. Not found.")

        # If the element is not found, display "Not found" to the user. 
    else:
        print("Not found")
        done = True
# print("Goodbye :)") 
