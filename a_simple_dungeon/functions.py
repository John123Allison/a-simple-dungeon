import sys
import os
from random import choice
import pickle
from time import sleep
from a_simple_dungeon import classes
from functools import partial


def clear_screen():
    """
    Clears the screen
    """
    # Clear the previously drawn text:
    if sys.platform == 'win32':
        os.system('cls') # Clears Windows terminal.
    else:
        os.system('clear') # Clears macOS/Linux terminal.


# function for generating items
def generate_item():
    """Generates a random item name from a list. The next step is appending that to the if/else statement, where a description and value are assigned based off of the name. Returns a class object Item.
    Would like to turn this into a DIY switch statement.
    """
    name_list = ["gem","candelbra","ruby","stick","mug"] # list of names that can be pulled from
    item_name = choice(name_list) # choose from the name list at random

    # check what item was generated and assign a descripion and random value from a range
    # that fits the item's name
    if item_name == "gem":
        item_description = "a small, shiny gem"
        item_value = choice(range(100,200))
    elif item_name == "candelbra":
        item_description = "a short candelbra, clearly very old"
        item_value = choice(range(25,75))
    elif item_name == "ruby":
        item_description = "a large red ruby"
        item_value = choice(range(300,450))
    elif item_name == "stick":
        item_description = "a long, thin stick that could snap at any moment"
        item_value = choice(range(1,5))
    elif item_name == "mug":
        item_description = "a cracked mug"
        item_value = choice(range(10,20))

    return classes.Item(item_name,item_description,item_value)


# function for generating weapons
def generate_weapon():
    """
    Returns class item Weapon.
    Works the exact same as generate_item(), but with a seperated list of weapon names and an extra damage value.
    """
    name_list = ["axe","sword","club"]
    weapon_name = choice(name_list) # choose from the name list at random

    # check what item is generated and assign a description and random damage value from a range
    if weapon_name == "axe":
        weapon_description = "a hefty axe"
        weapon_value = choice(range(50,90))
        weapon_damage = choice(range(10,25))
    elif weapon_name == "sword":
        weapon_description = "a small shortsword"
        weapon_value = choice(range(70,125))
        weapon_damage = choice(range(15,30))
    elif weapon_name == "club":
        weapon_description = "a sturdy club"
        weapon_value = choice(range(20,50))
        weapon_damage = choice(range(5,15))

    return classes.Weapon(weapon_name,weapon_description,weapon_value,weapon_damage)


def generate_room_inv():
    amount_generated = choice(range(1,10))

    inventory = []

    for i in range(amount_generated):
        type_gen = choice(range(1,2))

        if type_gen == 1:
            item = generate_item()
            inventory.append(item)
        elif type_gen == 2:
            weapon = generate_weapon()
            inventory.append(weapon)

    return inventory


def list_room_inv(room_inv):
    """
    Takes arg room_inv. If it contains items, lists contents.
    """
    if not room_inv:
            print("Room is empty")
    else:
        print("In the room is: ")
        for x in room_inv:
            print(x.name)


def loot_item(player,item,room_inv):
    """
    Takes args player, item, and room_inv.
    Loops over the room inventory and if it matches the item given, appends it to the player's inventory and deletes it from the room inventory.
    """
    for x in room_inv:
        if x.name.lower() == item:
            player.inventory.append(x)
            room_inv.remove(x)
    player.list_inventory()


def save_game(player):
    """
    Takes arg player.
    Creates a data file and serializes the player class object.
    """
    filename = 'data'
    outfile = open(filename,'wb')

    pickle.dump(player,outfile)
    outfile.close()


def load_game():
    """
    Loads .data, a pickled file and returns the player object found in it.
    """
    infile = open('./data','rb')
    player = pickle.load(infile)
    infile.close 

    return player

def move(player, direction, exits):
    if "north" in direction:
        if "north" in exits:
            f = exits["north"]
            f(player)
        else:
            print("You cannot go that way.")
    elif "south" in direction:
        if "south" in exits:
            f = exits["south"]
            f(player)
        else:
            print("You cannot go that way.")
    elif "east" in direction:
        if "east" in exits:
            f = exits["east"]
            f(player)
        else:
            print("You cannot go that way.")
    elif "west" in direction:
        if "west" in exits:
            f = exits["west"]
            f(player)
        else:
            print("You cannot go that way.")


def loot(room_inv, player):
    list_room_inv(room_inv)
    item = input("What do you want to pick up?\n> ")
    loot_item(player, item,room_inv)


def sell_item(player, can_sell):
    player.list_inventory()
    if can_sell == True:
        item_to_sell = input("What do you want to sell?\n> ")
        player.sell_item(item_to_sell)
    else:
        print("You can't sell right now.")


def wield(player):
    player.list_inventory()
    if len(player.inventory) > 0:
        item_to_equip = input("Equip which weapon?\n> ")
        player.equip_weapon(item_to_equip)


def stow(player):
    player.unequip_weapon


def help_menu():
    print("""
        Status: Check on yourself
        Look: Find nearby points of interest
        Take: Brings up a list of lootable items
        Inspect: Inspect an item in your inventory
        North/South/East/West: Move to a new location
        Wield: Equip a weapon from your inventory
        Stow: Unequip your weapon and store it in your inventory
        Drop: Remove and item from your inventory
        Sell: Sell items if there is a vendor in the room
        Save: Saves the game
        """)


def get_action(player, room_inv, can_sell, exits):
    """
    Performs an action based off of the player's input in a given scenario. Input is converted to lower case for easier string comparision. 
    Takes args player, room_inv, can_sell, and exits in order to operate on different objects.

    To modify, simply append a new action as a key and a function as a value to the dictionary mapping.
    Works as a custom implementation of a switch case from Java.
    """
    # -----INPUT-----
    action = input("> ").lower()

    possible_actions = {
        "status": partial(player.check_status),
        "inventory": partial(player.list_inventory),
        "look": partial(list_room_inv, room_inv),
        "north": partial(move, player, "north", exits),
        "east": partial(move, player, "east", exits),
        "south": partial(move, player, "south", exits),
        "west": partial(move, player, "west", exits),
        "take": partial(loot, room_inv, player),
        "loot": partial(loot, room_inv, player),
        "wield": partial(wield, player),
        "stow": partial(stow, player),
        "help": partial(help_menu),
        "save": partial(save_game, player),
        "sell": partial(sell_item, player, can_sell)
        }
    
    # execute function that corresponds to the action from the switch case
    action_to_execute = possible_actions.get(action)
    try:
        action_to_execute()
    except Exception:
        print("Invalid command")
        get_action(player, room_inv, can_sell, exits)
    

def new_game(player, first_room):
    """Takes args player (player object) and first_room(), the function that corresponds to the first room in the game."""
    clear_screen()
    player.choose_race()
    clear_screen()
    player.choose_job()
    clear_screen()
    player.update_stats()
    sleep(1)
 
    # start new game
    first_room(player)


def combat(player, enemy):
    print("You've encountered a %s!" % (enemy.name))
    response = input("Fight or flee?").lower()

    if response == "fight":
        enemy_attack = enemy.damage

        player_attack = player.weapon.damage

        player.change_health(enemy_attack)
        enemy.change_health(player_attack)