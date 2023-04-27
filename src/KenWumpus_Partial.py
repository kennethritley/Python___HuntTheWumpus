#--------------------------------------------------------------------
# KEN, 05 April 2022
#
# Written as a "skeleton" so that other people can write a fully-
# functioning "Hunt the Wumpus" game in around one hour or so if they
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






# Demonstrate printing out a dictionary object and how to use it

print("\n\n*** HUNT THE WUMPUS ***\n")


print("--- Now we show different options")
print (cave)
print("-----")
print(cave[11])
print("-----")
print(cave[11][0], cave[11][1], cave[11][2], cave[11])
print("-----")
nodes = cave[11]  # Here cave is a type "dictionary" and nodes is type "list"
print(nodes)
print("-----")
print(len(cave))
print("-----")


# Pick a starting room for us and for the wumpus    
print("Pick a room for yourself")
myroom=choose_start_room()
print("Pick a room for the wumpus")
wumpusroom=choose_start_room()



# Now take turns running around the maze
myroom=select_new_room(myroom)
wumpusroom=select_new_wumpusroom(wumpusroom)

myroom=select_new_room(myroom)
wumpusroom=select_new_wumpusroom(wumpusroom)

myroom=select_new_room(myroom)
wumpusroom=select_new_wumpusroom(wumpusroom)

myroom=select_new_room(myroom)
wumpusroom=select_new_wumpusroom(wumpusroom)



# NOW CREATE YOUR OWN HUNT-THE-WUMPUS GAME. SHOULD BE VERY EASY TO DO WITH THESE
# FUNCTIONS YOU FIND ABOVE!
#
#  Easiest suggestion: Create a "while" loop on the outside
#       1. Ask the user if she wants to shoot (s) or move (m) or quit (q)
#       2. Get desired room 
#       3. If user shoots into room and wumpus is there, she wins 
#            "Congratulations! You shot the wumpus"
#       4. If user moves into room and wumpus is there, she loses
#            "You find yourself face to face with the wumpus"
#            "It eats you whole"
#            "You have met your demise"
#       5. Do not move the wumpus - the wumpus always stays in the same room 
#
#  Next improvement
#       5. First see if wumpus is in adjacent room
#       6. If yes, print "You smell something terrible nearby."
#
#  If you can do this, then you have implemented 85% of the original game!
#  The original game also had bats that could fly you to a random room.
#  The original game also had a "bottomless pit" and if you stepped into that room, you die
#





