from classes import *
from functions import *


def test_room(player):
    # introduction
    print("You're standing in a small room with dank stone walls. Beside you is a small chest. There is a vendor.")

    # intialize room inventory and variables
    room_inv = generate_room_inv()
    can_sell = True

    # -----INPUT-----
    while True:
        action = input("> ").lower()

        # check current status
        if action == "status":
            player.check_status()
        # ------sell items---------
        elif action == "sell":
            player.list_inventory()
            if can_sell == True:
                item_to_sell = input("What do you want to sell?\n> ")
                player.sell_item(item_to_sell)
            else:
                print("You can't sell right now.")
         # ------------------------
        else:
            print("Invalid command")
   
            
        
