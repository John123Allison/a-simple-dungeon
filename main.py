from a_simple_dungeon import classes, functions, worldmap
from time import sleep


# begin main
def main():
    """
    player should be set to Player(), which instantiates a class object Player. The next step is Try/Except loop with looks for a save data file, and if none is found, begins a new game.
    """
    # initialize player and inventory
    player = classes.Player()

    # tries to load game, and runs it from the beginning if no file exists
    try:
        player = functions.load_game()
        player.location(player)
        functions.clear_screen()
        player.location()
    except FileNotFoundError:
        functions.new_game(player, worldmap.test_room)
        

if __name__ == '__main__':
    main()
