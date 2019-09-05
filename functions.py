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
    name = choice(name_list)

    # check what item was generated and assign a descripion and random value from a range 
    # that fits the item's name
    if name == "gem":
        description = "a small, shiny gem"
        value = choice(range(100,200))
    elif name == "candelbra":
        description = "a short candelbra, clearly very old"
        value = choice(range(25,75))
    elif name == "ruby":
        description = "a large red ruby"
        value = choice(range(300,450))
    elif name == "stick":
        description = "a long, thin stick that could snap at any moment"
        value = choice(range(1,5))
    elif name == "mug":
        description = "a cracked mug"
        value = choice(range(10,20))

    return Item(name,description,value)


# function for generating weapons
def generate_weapon():
    name_list = ["axe","sword","club"]
    name = choice(name_list)

    # check what item is generated and assign a description and random damage value from a range
    if name == "axe":
        description = "a hefty axe"
        value = choice(range(50,90))
        damage = choice(range(10,25))
    
