# 1. Name:
#      Ashlee Hart 
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program authenticates the user if a corresponding username and password
#      are entered. If something else is entered then the user is not authorized.
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out how to split the JSON object into 2 different lists was the hardest.
#      I am still kinda rusty with my Python so Ireferred to Stack Overflow for ideas. 
#      https://stackoverflow.com/questions/12988351/split-a-dictionary-in-half
# 5. How long did it take for you to complete the assignment?
#      It took me about 3 hours because I got lost on a couple parts. 

# Import JSON.
import json
5
# Read the contents of Lab02.json into a single string.
with open("Lab02.json", "r") as file:
    text = file.read()

# Convert the string into a JSON object using .loads().
    dictionary = json.loads(text)

# Convert the username and password components of the JSON object into two lists.
usernames = list(dictionary.values())[0]
passwords = list(dictionary.values())[1]

# Prompt the user for a username and a password. 
username = input("Username: ")
password = input("Password: ")

# Search to see if the username and password are on the lists. 
for index, user in enumerate(usernames):
    # If both are present at the same location on the lists then the user is authenticated.
    if username == user and passwords[index] == password:
        print("You are authenticated!")
        break
    # If the username and password are not in the lists and don't match, the user is not authorized.
    else: 
        print("You are not authorized to use the system.")
        break