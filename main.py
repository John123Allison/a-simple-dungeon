from modules.classes import *
from modules.functions import *
from modules.worldmap import *
from time import sleep


# begin main
def main():
    """
    Player should be set to Player(), which instantiates a class object Player. The next step is Try/Except loop with looks for a save data file, and if none is found, begins a new game.
    """
    # initialize player and inventory
    player = Player()

    # tries to load game, and runs it from the beginning if no file exists
    try:
        player = load_game()
        player.location(player)
        clear_screen()
        player.location()
    except FileNotFoundError:
        new_game(player, test_room)
        

if __name__ == '__main__':
    main()
