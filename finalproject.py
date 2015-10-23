def textParse():
    f = open('adventuretext.txt', 'r')
    data = f.read()
    paragraphs = data.split("\n\n")
    paragraphs = [value for value in paragraphs]
    return paragraphs

def title():
    print '\n','*'*80
    print 'Alone in the Woods'
    print '*'*80,'\n'

def story_choice(num_of_choices=2):
    # validate player input
    if num_of_choices == 2:
        choice = raw_input('Enter 1 or 2: ')
        while choice !='1' and choice != '2':
            print 'Wrong input, try again'
            choice = raw_input('Enter 1 or 2: ')
    elif num_of_choices == 3:
        choice = raw_input('Enter 1, 2, or 3: ')
        while choice !='1' and choice != '2' and choice !='3':
            print 'Wrong input, try again'
            choice = raw_input('Enter 1, 2, or 3: ')
    return choice

def continue_game():
    while True:
        choice = raw_input('\nDo you want to play again? Enter Yes or No: ')
        choice = choice.strip()
        continue_game_choices = ['Yes', 'Y', 'yes', 'y']
        end_game_choices = ['No', 'N', 'no', 'n']
        if choice not in continue_game_choices and choice not in end_game_choices:
            print 'Sorry, wrong input, try again'
        elif choice in end_game_choices:
            print '\nThank you for playing!'
            return 1
            break
        elif choice in continue_game_choices:
            print '\nRestarting game...\n'
            break

def main():
    title()
    intro = textParse()[0]
    noise = textParse()[1]
    noise_left = textParse()[2]
    campsite = textParse()[3]
    fog = textParse()[4]

    while True:
        print intro
        noise_or_campsite = story_choice(2)

        if noise_or_campsite == '1':
            print noise
            noise_direction = story_choice(3)

            if noise_direction == '1':
                print noise_left
                noise_left_direction = story_choice(2)
            elif noise_direction == '2':
                print 'Player chose noise forward'
            else:
                print 'Player chose noise right'

        else:
            print campsite
            campsite_direction = story_choice(2)

            if campsite_direction == '1':
                print 'Player chose campsite left'
            else:
                print 'Player chose campsite right'

        if continue_game() == 1:
            break

def player_input(player_choice, num_of_choices):
    # validate player input
    if num_of_choices == 2:
        while player_choice !="1" and player_choice != "2":
            print "Wrong input, try again"
            player_choice = raw_input("Enter 1 or 2: ")

    elif num_of_choices == 3:
        while player_choice !="1" and player_choice != "2" and player_choice !="3":
            print "Wrong input, try again"
            player_choice = raw_input("Enter 1, 2, or 3: ")

    return player_choice

def intro():
    print "You wake up alone in a dense forest in the middle of the night armed with only a flashlight.\n"
    "You have no recollection of what has happen. You immediately become scared. You hear a noise."
    print "You sense that something or someone is close. It could be one of your friends."
    print "What do you want to do?"
    print "1) Examine the noise"
    print "2) Go find your campsite"

    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)

def noise():
    print
    print "You chose to find the source of the noise. You go forward in the forest. in three directions."
    print "Choose a direction:"
    print "1) Left"
    print "2) Forward"
    print "3) Right"
    player_choice = raw_input("Enter 1, 2 or 3: ")
    return player_input(player_choice, 3)

def noise_left():
    print
    print 'player chose left'
    print "You decided to go left. You walk forward. Calling out for your friend or to anyone that is nearby."
    print "Your voice echoes through the forest. You hear a loud crack and also hear the faint sound of an ominous voice."
    print "Do you wish to go back?"
    print "1) Yes"
    print "2) No"
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)

def back_to_fork():
    player_input
    print "You chose to go back to the where the trail branches out. You make a mental note not to go left. \n" 
    print "You think to yourself, “That was scary. Won’t go in that direction again.”  Choose a different path."
    print  "1. Middle" 
    print  "2. Right"
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)

def choose_new_path():
    print "You choose to go forward. Such bravery. But will it work in your favor? “Hello. Who’s there?” you ask. \n"
    print "You wait several seconds but there is no response. Continue to be brave and proceed forward to through the woods. You see a faint figure in the distance.\n"
    print "What do you do?"
    print "1. Walk to the figure"
    print "2. Change your mind and run like hell"
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)


def middlepath_figure():
    print "You chose to approach the figure. As you approach a thick fog rolls in. You start to shiver. You see a figure that seemed like a man."
    print "A unusually tall but thin figure dress in a black suit but with long arms and clawlike fingers. He face is blank possessing not facial features whatsoever."
    print "People call him The Slender Man. You heard many legends of this creature but you didn’t think it was true. You see a body laying on ground near The Slender Man."
    print "You recognized that the person on the ground is your friend. He is dead. The noise you heard was sound of him dying. Do you wish to take revenge and fight The Slender Man?"
    print "1. Yes"
    print "2. No"
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)

def slenderman_fight():
    print "You cry out in anger and start to strike at The Slender Man. He He lunges forward at you. You try to dodge but he grabs you by the neck with his long claw -like fingers."
    print "You at stare at the figure blank face as his grip tightens. You start to lose conscious. You die. Game over." 
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)

def slenderman_run():
    print "You rather not fight The Slender Man. You decide to run."
    print "However, the fog gets thicker. It starts to surround you. The noise gets louder but you cannot pinpoint where the noise is coming from."
    print "Something grazes you on the shoulder. You are frighten. Your heart starts racing and wildly look around. You turn around."
    print "You are immobilized by fear. He lunges forward at you. You die. Game over."
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)

def noise_forward():
    print
    print "You decided on taking the path in the middle. As you proceed the forest become less dense and leads to a clearing. In the distance you see a light. If there’s light, there could be people! But you heard the strange noise again but louder this time."
    print "You are probably close to the source of the sound. What do you want to do?"
    print "1. Continue investigating the noise" 
    print "2. Go towards the light."
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)

def noise_right():
    print
    print "You chose to go right. You are walking through this vast forest. It doesn’t seem to end. The sound of leaves and sticks crushing beneath your feet echoes through the forest."
    print  "'Hello? Is anyone there?'' you ask to no one in particular. You notice a mound of leaves with some blood on it."
    print "You decide to take a look at it. How so?" 
    print "1. Poke through with a stick"
    print "2. Look with your eyes not with your hands."
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)

def with_astick():
    print
    print "You decide to poke the mound with a stick. Who knows what lies underneath."
    print "You look around for the biggest sticks in your general area and pick it up. You use it to look through the pile of leaves. That’s when you see it. A served arm."
    print "You become disgusted and horrified. Who or what did this? You look around some more. The blood left a trial. You follow the blood trail until it leads you to strange clearing."
    print "It leads to a multiple paths in the forest. Chose a direction."
    print "1. North"
    print "2. East" 
    print "3. South"

def your_eyes():
print
print
print "You rather look than touch. It’s never a good idea to touch anything covered in blood."
print "You look through the pile of leaves and notice something sticking out from the pile. It’s a served arm. You become disgusted and horrified."
print "Who or what did this? You look around some more. The blood left a trial. You follow the blood trail until it leads you to strange clearing."
print "It leads to a multiple paths in the forest. Chose a direction."
print "1. North"
print "2. East"
print "3. South"    

def clearing_north():
print 
print" You chose to go North. You have found the source of the light you saw earlier. The light comes from a log cabin."
print "Finally civilization. Maybe someone is inside. Do you dare to enter?"
print "1. Yes"
print "2. No"

def clearning east():
print
print "You chose to head East. It leads to even more secluded part of the forest."
print "The light of the moon is blocked off from the tall and thick trees leaving you in darkness except your flashlight."
print "Here is where you have a found the source of the noise. A giant beast. Standing on its hind legs, it stares at you growling."
print "What do you chose to do?"
print "1. Fight it!"
print "2. Run!"

def beast_fight():
print
print "Your body goes into fight or flight mode and you chose to fight."
print "You brace yourself to fight the beast. You cry out and try to hit it with your flashlight. It is no use."
print "The beast is much bigger and stronger than you. It claws at you. You are knocked to the ground. You die. You lose."

def beast_run():
print 
print "You start to run as fast you can. Suddenly you trip over a branch on the ground. You get back up. Your flashlight starts flickering and it soon goes out."
print "You hit the flashlight against your palm. It is no use. The batteries have died. You are now walking around in darkness." 
print "Only the luminescence of the moon is your source of light. You start to panic and run around frantically for a way out but it’s too late the beast caught up to you."
print "It tackles you back on the ground. You die. You lose."

def clearing_south():
print 
print "You chose to head South. You find a campsite. 'Maybe someone is still here?'' you think to yourself."
print "You look around you find a fellow camper covered blood. It look like he lost some limbs. This is when you found the source of the noise. A giant beast."
print "It is standing on its hind legs as it stares at you growling. You start to run. Suddenly, you hear a loud metal clang and immediately are overcome with pain. You are unable to move forward. It seems that the pain is coming from your right leg. You look down."
print "You stepped on a bear trap. You try to free your leg but unable. Blood is seeping out of your wound. You call out for help but it is in vain."
print "The pain is too much. You died. The end."


def campsite():
    print
    print "You chose to go ignore the noise and try to find your campsite. You go forward on the trail but soon stop."
    print "You face a fork in the trail. You try your best to remember but your"
    print "Choose a direction:"
    print "1) Left"
    print "2) Right"
    player_choice = raw_input("Enter 1 or 2: ")
    return player_input(player_choice, 2)


def campsite_left():
    print
    print 'player chose left'

def campsite_right():
    print
    print 'player chose right'



