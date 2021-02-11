# --------------------------------------Text Based Adventure Game--------------------------------------
# The user has the choice to select an option and the aim of the game is to survive
# Author: Amar Plakalo
# Date: 06/02/2021

# Declare and initialise variables so that they can be used in the game
gun = 0


def start_of_game():
    print("You spent the night in the forest with your friends. It was so fun and you enjoyed yourself. Then, your friends told you "
    "to go get some more wood from the forest.You anxiously walk towards the dark forest and look for some wood. All of a sudden"
    " a big bear appears. Your heart starts pouding quickly. You will: \n")
    print("A. Throw a rock at the bear and see how the bear reacts\n"
    "B. Lie down and hope that he doesn't kill you\n"
    "C. Run as fast as you can")
    option_select = input() # the game looks for input from the user. The user has to select either of the options
    if option_select == "A" or option_select == "a": # if they selected A
        throw_rock() # go to this function if A was selected
    elif option_select == "B" or option_select == "b": # if they selected B
        print("Damn it. You died") # prints message to screen
    elif option_select == "C" or option_select == "c": # if they selected C
        run_away() # go to this function if C was selected by the user
    else: # if none of the options was selected
        print("You have to select either A or B or C. Back to the start!!!") # prompt user to select either A or B or C
        start_of_game() # return to the start of the game
def throw_rock():
    print("You throw the rock and the bear is slightly stunned. After a couple of seconds, the bear regains control. Will you: \n")
    print("A. Run because you have little chance\n"
    "B. Throw another rock because it did stun him\n"
    "C. Find some shelter where you can hide")
    option_select = input() # looks for input from user. They should select either A or B or C depending on what they think is correct
    if option_select == "A" or option_select == "a": # if they selected A
        run_away() # go to this function if the option selected is A
    elif option_select == "B" or option_select == "b": # if the option selected was B
        print("Ah damn it. You threw the rock and it missed the bear. You die") # print error messsage
    elif option_select == "C" or option_select == "c": # if the option selected is C
        find_shelter() # go to this function
    else: # if none of the options was selected
        print("You have to select either A or B or C. Back to the part where you threw the rock!!!") # error message printed
        throw_rock() # calls the function which means that this function is run again so the user can pick correctly their option
def run_away():
    print("You decide to run away but that bear is running so quickly. What do you do: \n")
    print("A. Hide behind a big rock\n"
    "B. Fight and hope you kill the bear\n"
    "C. Run towards that small house right ahead. I hope it's unlocked.\n")
    option_select = input() # look for input from the user i.e. select A or B or C
    if option_select == "A" or option_select == "a": # if A was selected
        print("Oh that was dumb. The bear is huge. He saw you behind the rock. You die.") # print error message
    elif option_select == "B" or option_select == "b": # if B was selected
        print("You thought that you could kill him without any weapons?? Damn, you die!!!") # print error message
    elif option_select == "C" or option_select == "c": # if C was selected
        small_house() # call function if C was selected
    else: # in case none of the options was selected
        print("You have to select either A or B or C. Try again!!!") # print error message
        run_away() # return back to this function
def find_shelter():
    print("You found a dark cave. Fortunately, a gun is on the floor. Someone must have had the same issue like me! What do you do: \n")
    print("A. Take the gun\n"
    "B. Don't take the gun. Just hide and hope the bear doesn't find you\n")
    option_select = input() # the option is remembered i.e. whether the user wants A or B 
    if option_select == "A" or option_select == "a": # if A was selected
        gun = 1 # this value indicates that the user took the gun
        print("You took the gun. Now, will you stay where you are or fight?\n"
        "A. Fight\n"
        "B. Stay where you are and don't fight\n")
        option_select = input() # asks user to input either A or B
        if option_select == "A" or option_select == "a" and gun == 1: # if A was inputted and user has a gun
            print("You choose to fight. You take your gun and the bear walks in. You are shaking with fear. You pull the trigger "
            "and the bear is shot. You survive!!!!!!!") # prints message to screen
        elif option_select == "B" or option_select == "b" and gun == 1: # if option B was selected and the user has the gun
            print("Wait, you have a gun and you aren't fighting?? Wow, you die. That was lame") # error message
    elif option_select == "B" or option_select == "b": # if option B is selected
        gun = 0 # this value indicates that the user does not have a gun
        print("You decide not to take the gun. The fear of taking the gun and fighting is too strong. What do you do: \n")
        print("A. Stay there and hide\n"
        "B. Run away\n")
        option_select = input() # option A or B can be entered by the user
        if option_select == "A" or option_select == "a" and gun == 0: # if option is A and the user does not have a gun
            print("Well, you decided not to take the gun and the bear has just arrived into the cave."
            "The bear has decided to attack you and he manages to kill you. You die!!") # error message printed
        elif option_select == "B" or option_select == "b" and gun == 0: # if user selected B and the user does not have a gun
            print("You decide to run. The bear sees you in the cave but you somehow manage to fly past the bear"
            "and you seem to be runnning really quickly.") # message printed to screen
            run_away() # call function so that it can execute the next step
    else: # if none of the options were selected
        print("You had to select either A or B. Back to the part where you were finding shelter.") # error message
        find_shelter() # return back to the function
def small_house():
    print("You run towards the small house. Your heart is so close to exploding. You fear that something bad will happen."
    "You hope that the door is unlocked. As you arrive, you turn the door knob and it is unlocked. You hurry in and close the door."
    "The bear is outside the door and he is punching the door. What do you do? \n")
    print("A. Hide in a room and hope the bear doesn't find you.\n"
    "B. There is a chocolate bar on the table. Maybe give it to the bear\n")
    option_select = input() # option is remembered inside the variable
    if option_select == "A" or option_select == "a": # if user chose option A
        print("Well, the bear breaks through the door and looks for you. He sees a bed and looks under it. He finds you. You die!!!!")
    elif option_select == "B" or option_select == "b": # if user chose option B
        print("The bear walks in and sees you with a chocolate bar in your hand. You give it to the bear and the bear eats it."
        "Then, all of a sudden, the bear turns around and walks out of the room. That was easy! You Survive!!!!!") # message printed
    else: # if none of the options was selected
        print("You select either A or B. Back to the part where you go inside a small house.") # error message
        small_house() # return back to the function
start_of_game() # start with this function
