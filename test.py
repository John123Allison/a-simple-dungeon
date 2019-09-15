from classes import *
from functions import *
from worldmap import *
from time import sleep


# begin main
def main():
    # initialize player and inventory
    player = Player()

    # tries to load game, and runs it from the beginning if no file exists
    try:
        player = load_game()
        player.location(player)
        clear_screen()
        player.location()
    except Exception:
        new_game(player, test_room)
        

if __name__ == '__main__':
    main()
