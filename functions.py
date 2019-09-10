import sys
import os
from random import choice
from classes import *

def clear_screen():
    # Clear the previously drawn text:
    if sys.platform == 'win32':
        os.system('cls') # Clears Windows terminal.
    else:
        os.system('clear') # Clears macOS/Linux terminal.


# function for generating items
def generate_item():
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

    return Item(item_name,item_description,item_value)


# function for generating weapons
def generate_weapon():
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

    return Weapon(weapon_name,weapon_description,weapon_value,weapon_damage)


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
    if not room_inv:
            print("Room is empty")
    else:
        print("In the room is: ")
        for x in room_inv:
            print(x.name)


def loot_item(player,item,room_inv):
    for x in room_inv:
        if x.name == item:
            player.inventory.append(x)
    player.list_inventory()


def get_action(player,room_inv,can_sell,exits):
    # -----INPUT-----
    action = input("> ").lower()

    # check current status
    if action == "status":
        player.check_status()
    # ------list room contents-----
    elif "look" in action:
        list_room_inv(room_inv)
    # ------move-----
    elif "north" in action:
        if "north" in exits:
            f = exits["north"]
            f(player)
        else:
            print("You cannot go that way.")
    elif "south" in action:
        if "south" in exits:
            f = exits["south"]
            f(player)
        else:
            print("You cannot go that way.")
    elif "east" in action:
        if "east" in exits:
            f = exits["east"]
            f(player)
        else:
            print("You cannot go that way.")
    elif "west" in action:
        if "west" in exits:
            f = exits["west"]
            f(player)
        else:
            print("You cannot go that way.")
    # -----looting-----
    elif "pick up" in action:
        list_room_inv(room_inv)
        pick_up = input("What do you want to pick up?\n> ")
        loot_item(player,pick_up,room_inv)
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
        pass

    return action
