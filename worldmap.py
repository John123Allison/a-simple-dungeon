from classes import *
from functions import *


# blueprint for rooms in the worldspace
def test_room(player):
    # intialize room inventory and variables
    test_room_inv = generate_room_inv()
    can_sell = True

    # introduction
    print("You're standing in a small room with dank stone walls. Beside you is a small chest. To the north there is a small passageway.\nThere is a vendor.")

    # persistently get input, passing the player, the room inventory, and whether or not you can sell items in this space.
    while True:
        action = get_action(player,test_room_inv,True).lower()
        
        if action == "north":
            test_room2(player)


def test_room2(player):
    # intialize room inventory and variables
    test_room2_inv = None
    can_sell = False

    # introduction
    print("You enter into an empty chamber, devoid of any furnishings.")

    # persistently get input, passing the player, the room inventory, and whether or not you can sell items in this space.
    while True:
        action = get_action(player,test_room2_inv,True).lower()
        
        if action == "direction":
            do_things = "foo"
