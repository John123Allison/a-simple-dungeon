from classes import *
from functions import *
from worldmap import *
from time import sleep


# begin main
def main():
    # initialize player and inventory
    player = Player()

    # print welcome message
    #clear_screen()
    #print("------------------------")
    #print("Welcome!")
    #print("------------------------")

    # new game
    clear_screen()
    player.choose_race()
    clear_screen()
    player.choose_job()
    clear_screen()
    player.update_stats()
    sleep(1)
    test_room(player)


if __name__ == '__main__':
    main()
