from classes import *
from functions import *
from time import sleep

player = Player()
inventory = player.inventory

test1 = Weapon("axe","a hefty axe",100,10)
test2 = Item("gem","a shiny gem",200)

player.add_to_inventory(test1)
player.add_to_inventory(test2)
list_inventory(inventory)

sleep(5)

player.sell_item(test1)
list_inventory(inventory)
print(player.gold)

sleep(5)

player.change_health(50)

sleep(2)

player.change_health(51)