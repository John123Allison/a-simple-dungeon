from classes import *
from functions import *
from worldmap import *
from time import sleep


# begin main 
def main():
    # initialize player and inventory
    player = Player()

    # print welcome message
    clear_screen()
    print("------------------------")
    print("Welcome!")
    print("------------------------")


    sleep(5)
    clear_screen()


    test_room(player)
        

if __name__ == '__main__':
    main()