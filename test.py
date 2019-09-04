from classes import *
from time import sleep


# begin main 
def main():
    # always define the player as player = Player()
    player = Player()
    inventory = player.inventory   
    while True:
        current_x = player.x
        current_y = player.y

        # constantly get user input
        action = input("> ").lower()

        # determine if the action is a movement
        if action == "north":
            player.move("north")
        elif action == "east":
            player.move("east")
        elif action == "south":
            player.move("south")
        elif action == "west":
            player.move("west")
        else:
            pass
        
        # check current status
        if action == "status":
            player.check_status()
        else:
            pass
        
        # sell items
        if action == "sell":
            player.list_inventory()
            try:
                item_to_sell = input("What do you want to sell?\n> ")
                player.sell_item(item_to_sell)
            except:
                print("Error")
        

if __name__ == '__main__':
    main()