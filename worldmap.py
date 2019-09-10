from classes import *
from functions import *


# blueprint for rooms in the worldspace
def test_room(player):
    # intialize room inventory and variables
    test_room_inv = generate_room_inv()
    can_sell = True
    exits = {"north": test_room2}

    # introduction
    print("You're standing in a small room with dank stone walls. Beside you is a small chest. To the north there is a small passageway.\nThere is a vendor.")

    # persistently get input, passing the player, the room inventory, and whether or not you can sell items in this space.
    while True:
        action = get_action(player,test_room_inv,True,exits)


def test_room2(player):
    # intialize room inventory and variables
    test_room2_inv = [Weapon("Silver Sword","A shortsword made of silver. Warewolves hate these.",500,8)]
    can_sell = False
    exits = {"south": test_room}

    # introduction
    print("You enter into an empty chamber, devoid of any furnishings.")

    # persistently get input, passing the player, the room inventory, and whether or not you can sell items in this space.
    while True:
        action = get_action(player,test_room2_inv,True,exits)

        if action == "direction":
            do_things = "foo"
