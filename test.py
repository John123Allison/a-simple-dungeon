from classes import *
from time import sleep
import sys
import os

def clear_screen():
    # Clear the previously drawn text:
    if sys.platform == 'win32':
        os.system('cls') # Clears Windows terminal.
    else:
        os.system('clear') # Clears macOS/Linux terminal.

# begin main 
def main():
    # always define the player as player = Player()
    # initialize player and inventory
    player = Player()
    inventory = player.inventory   

    # print welcome message
    print("------------------------")
    print("Welcome!")
    print("------------------------")

    sleep(5)
    clear_screen()

    while True:
        # constantly get user input
        action = input("> ").lower()

        # check current status
        if action == "status":
            player.check_status()
        # sell items
        elif action == "sell":
            player.list_inventory()
            try:
                item_to_sell = input("What do you want to sell?\n> ")
                player.sell_item(item_to_sell)
            except:
                print("Error")
        else:
            print("Invalid command")
        

if __name__ == '__main__':
    main()