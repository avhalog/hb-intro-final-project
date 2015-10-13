"""
-----
TO DO LIST: Correctly parse the text file by splitting it up by paragraph
-----
"""

import adventuretext.txt
my_file = open(adventuretext.txt)

def title():
    print
    print "*"*80
    print "Alone in the Woods"
    print "*"*80
    print

def intro():
    print "You wake up alone in a dense forest in the middle of the night armed with only a flashlight.\n"
    "You have no recollection of what has happen. You immediately become scared. You hear a noise."
    print "You sense that something or someone is close. It could be one of your friends."
    print "What do you want to do?"
    print "1) Examine the noise"
    print "2) Go find your campsite"

    player_choice = raw_input("Enter 1 or 2: ")
    print "player_choice initial: ", player_choice
    print "player_choice initial type: ", type(player_choice)

    """
    -----
    TO DO LIST: Add a looping mechanism to ask the player to input their choice again
                if they don't enter a 1 or 2
    -----
    """
    while player_choice !="1" and player_choice != "2":
        print "Wrong input, try again"
        player_choice = raw_input("Enter 1 or 2: ")
        # print "player_choice: ", player_choice
        # print "player_choice type: ", type(player_choice)   
    return player_choice

def first_choice_one():
    print
    print "You chose to find the source of the noise. You go forward in the forest. in three directions."
    print "Choose a direction:"
    print "1) Left"
    print "2) Forward"
    print "3) Right"
    player_choice = raw_input("Enter 1, 2 or 3: ")
    return player_choice

def first_choice_two():
    print
    print "You chose to go ignore the noise and try to find your campsite. You go forward on the trail but soon stop."
    print "You face a fork in the trail. You try your best to remember but your"
    print "Choose a direction:"
    print "1) Left"
    print "2) Right"
    player_choice = raw_input("Enter 1 or 2: ")
    return player_choice

def main():
    """
    Main game function that starts the game
    """
    # Print the title
    title()

    # Run game
    while True:
        # Launch game
        first_choice = intro()

        if first_choice == "1":
            first_choice_one()

        elif first_choice == "2":
            first_choice_two()

        continue_game = raw_input("Do you want to play again? Enter Yes or No: ")
        if continue_game == "No" or continue_game == "no":
            break

# Good python code for running main function. Good Python etiquette.
if __name__ == "__main__":
    main()
