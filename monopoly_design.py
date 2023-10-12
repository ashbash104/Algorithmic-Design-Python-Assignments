# 1. Name:
#      Ashlee Hart
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program determines the cheapest way you can place a hotel on Pennsylvania street 
#      and determines if you are able to, following the rules of Monopoly.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was keeping the if else statements ligned up well and not getting lost when I was 
#        changing the code.
# 5. How long did it take for you to complete the assignment?
#      About 2.5 hours.

# Create a while loop so the user will be brought back to the prompt if they enter an invalid response.
key = True
while key == True:

    # Prompt the user to see if they own all of placed the green properties.
    color_group = input("Do you own all the green properties? (y/n) ")

    # User cannot buy hotel if they don't own all of the green properties. 
    if color_group.lower() == "n":
        print("You cannot purchase a hotel until you own all the properties of a given color group.")
        key = False

    # Prompt user to see what is on Pennsylvania Avenue
    elif color_group.lower() == "y":
        pa = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, 5:a hotel) "))
        if pa == 0 or pa == 1 or pa == 2 or pa == 3 or pa == 4:

            # If user has a house on Pennsylvania Avenue prompt them for the number of houses on North Carolina Avenue.
            nc = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, 5:a hotel) "))

            # If user has a house on North Carolina Avenue prompt them for the number of houses on Pacific Avenue.
            if nc == 0 or nc == 1 or nc == 2 or nc == 3 or nc == 4:
                pc = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, 5:a hotel) "))

                # If user has a house on Pacific Avenue prompt them to see how mmany hotels are for sale.
                if pc == 0 or pc == 1 or pc == 2 or pc == 3 or pc == 4:
                    hotels_for_sale = int(input("How many hotels are there to purchase? "))

                    # Calculate the number of houses needed and the total cost to place a hotel.
                    # Also see if there are enough hotels and houses for sale.
                    if hotels_for_sale >= 1:
                        num_houses = pa + nc + pc
                        houses_needed = 12 - num_houses
                        total_cost = houses_needed * 200

                        # Ask user how much money they have to spend.
                        money = int(input("How much cash do you have to spend? "))
                        if money >= total_cost and money >= 200:
                            houses = int(input("How many houses are there to purchase? "))
                            if houses >= houses_needed:
                                pa_houses_needed = 4 - pa
                                nc_houses_needed = 4 - nc
                                pc_houses_needed = 4 - pc

                                # If the bank has enough hotels and houses for sale
                                # And the user has enough cast, display the total cost
                                # And instructions for placing the hotel and houses.
                                if nc_houses_needed > 0 and pc_houses_needed > 0:
                                    print(f"""This will cost ${total_cost}.
                                                        Purchase 1 hotel and {houses_needed} house(s).
                                                        Put 1 hotel on Pennsylvania and return any houses to the bank.
                                                        Put {nc_houses_needed} house(s) on North Carolina.
                                                        Put {pc_houses_needed} house(s) on Pacific.""")
                                elif nc_houses_needed == houses_needed:
                                    print(f"""This will cost ${total_cost}.
                                                        Purchase 1 hotel and {houses_needed} house(s).
                                                        Put 1 hotel on Pennsylvania and return any houses to the bank.
                                                        Put {nc_houses_needed} house(s) on North Carolina.""")
                                elif pc_houses_needed == houses_needed:
                                    print(f"""This will cost ${total_cost}.
                                                        Purchase 1 hotel and {houses_needed} house(s).
                                                        Put 1 hotel on Pennsylvania and return any houses to the bank.
                                                        Put {nc_houses_needed} house(s) on Pacific.""")
                                else:
                                    print(f"""This will cost ${total_cost}.
                                                        Purchase 1 hotel and {houses_needed} house(s).
                                                        Put 1 hotel on Pennsylvania and return any houses to the bank.""")

                            # Display message to user that there are not enough houses for sale by the bank.            
                            else:
                                print("There are not enough houses available for purchase at this time. ")
                                exit()

                        # Display message to user that they do not have anough cash.
                        else:
                            print("You do not have sufficient funds to purchase a hotel at this time.")
                        
                    # Display message to user that there are no hotels for sale.
                    else: 
                        print("There are not enough hotels available for purchase at this time.")
                        exit()

                    # If user has a hotel on Pacific and 4 houses on Pennsylvania prompt them to swap them.
                else:
                    print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
                    exit()

                # If user has a hotel on North Carolina and 4 houses on Pennsylvania prompt them to swap them.
            elif nc == 5: 
                print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
                exit() # I know I can't use "break" so is this the better alternative?
            else: 
                print("Please enter a valid response")

        # Display that user can't purchase a hotel if the property already has one.
        elif pa == 5:
            print("You cannot purchase a  hotel if the property already has one.")
            exit()

        # Prompt the user to enter a valid response
        else:
            print("Please enter a valid response" )

    # Prompt the user to enter a valid response (y or n).
    else:
        print("Please enter a valid response. ")
        key = True
