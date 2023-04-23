#--------------------------------------------------------------------
# KEN, 05 April 2022
#
# Written as a "skeleton" so that other people can write a fully-
# functioning "Hunt the Wumpus" game in around one hour if they
# are new to the language.
#--------------------------------------------------------------------

# This is needed for wumpus moving in function select_new_wumpusroom
import random

# Define a "dictionary" variable with all the room nodes.  The way to understand
# this is that each "key" (1-20) is attached to a 3-room list "value". For example, if you
# are in room 5, then the next available rooms are 2, 9, and 11.

cave = {1: [2,3,4], 2: [1,5,6], 3: [1,7,8], 4: [1,9,10], 5:[2,9,11],
	6: [2,7,12], 7: [3,6,13], 8: [3,10,14], 9: [4,5,15], 10: [4,8,16], 
	11: [5,12,17], 12: [6,11,18], 13: [7,14,18], 14: [8,13,19], 
	15: [9,16,17], 16: [10,15,19], 17: [11,20,15], 18: [12,13,20], 
	19: [14,16,20], 20: [17,18,19]}


# Define the function to be called once, so the user can choose what room he
# or she wants to start in. Not really needed, but nice example of while

def choose_start_room():
    """ Let's the user select a starting room. """
    while True:
        myroom = int(input("Enter a room between 1 and 20\n"))
        print("Your room is", myroom)
        if myroom >0 and myroom <21:
            return myroom
        else:
            print("You must enter a room from 1 to 20")

# The dictionary variable "cave" contains (key,value) pairs, where key is an
# integer room, and value is a list of three integers that are the attached
# rooms that someone can move into or shoot into

def select_new_room(myroom):
    """ User selects the next room when she is in myroom """
    # First, display the available rooms to choose from
    for room, nodes in cave.items():
        if room==myroom:
            print("You are in room", myroom)
            print("Tunnels lead to", nodes[0],nodes[1],nodes[2])
            break
    # Next, have the user input a valid room to move or shoot to
    while True:
        nextroom = int(input("Which room do you choose\n"))
        if nextroom ==nodes[0] or nextroom ==nodes[1] or nextroom ==nodes[2]:
            # print("Good choice", nextroom)
            return nextroom
        else:
            print("You must enter a room from", nodes)

# Just a useful function if someone wants the wumpus to move
# randomly from room to adjacent room. Probably for the easiest case
# the wumpus is fat and lazy and you don't need this function

def select_new_wumpusroom(myroom):
    """ Returns a random room for the wumpus to move to """
    nodes=cave[myroom]
    nextroom = nodes[random.randint(0,2)]
    print("The wumpus has moved to room", nextroom)
    return nextroom

# Just a useful function if someone wants the wumpus to move
# randomly from room to adjacent room. Probably for the easiest case
# the wumpus is fat and lazy and you don't need this function

def do_i_small_a_wumpus(myroom, wumpusroom):
    nodes=cave[wumpusroom]
    if myroom in nodes:
        print("You smell something terrible nearby.")


# Start the game!

print("\n\n*** HUNT THE WUMPUS ***\n")

# Pick a starting room for the player   
# print("Pick a room for yourself")
myroom=choose_start_room()
# myroom = 0
#myroom = 2
print("You are in room", myroom)
print("Tunnels lead to", 2, 3, 4)
# myroom=select_new_room(myroom)


# Pick a starting room for the wumpus - just for testing, should be random   
# print("Pick a room for the wumpus")
# wumpusroom=choose_start_room()
wumpusroom = 10

# Initialize shootroom
shootroom = 0

# The hunt is on!  We keep looping until you get the wumpus or the wumpus gets you!
while True:
    # do_i_small_a_wumpus(myroom, wumpusroom)
    answer=input("Do you want to (s) shoot, (m) move, or (q) quit?")
    if answer == "q":
        break
    elif answer == "m":
        myroom=select_new_room(myroom)
    elif answer == "s":
        shootroom=select_new_room(myroom)
    else:
        print("You must enter s, m, or q")
    if myroom == wumpusroom:
        print("You find yourself face to face with the wumpus.")
        print("It eats you whole.")
        print("You have met your demise.")
        break
    elif shootroom == wumpusroom:
        print("Congratulations! You shot the wumpus.")
        break
    
print("Game over.")





