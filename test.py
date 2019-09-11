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
