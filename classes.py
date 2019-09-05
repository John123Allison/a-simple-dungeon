from time import sleep
import sys


# most values of players are stored as variables, with the inventory as a simple list
# values of the player's status are changed by methods attached to the class
class Player():
    def __init__(self):
        self.inventory = []
        self.health = 100 # affected by interactions with weapon objects
        self.armor = 0 # affected by inventory
        self.is_alive = True # set to false to trigger restart and/or death sequence
        self.gold = 0
        self.can_sell = False # set to true when in market or speaking to a vendor

    def check_status(self):
        print("Current health: %s" % (self.health))
        print("Current armor: %s" % (self.armor))
        print("Current gold: %s" % (self.gold))

    def status(self):
        if self.health <= 0:
            self.is_alive = False
        else:
            pass
        
        if self.is_alive == False:
            self.die()
    
    def change_health(self,value):
        if self.health > 0:
            self.health = self.health + value
        elif self.health <= 0:
            self.is_alive = False
        self.check_status

    def add_to_inventory(self,item):
        self.inventory.append(item)

    def list_inventory(self):
        if not self.inventory:
            print("Inventory is empty")
        else:
            print("Inventory: ")
            for x in self.inventory:
                print(x.name)    

    def sell_item(self,item):
        if self.can_sell == True:
            for x in self.inventory:
                if x.name == item:
                    self.inventory.remove(x)
                    self.gold = self.gold + x.value
                else:
                    print("Error: item doesn't exist")
        else:
            print("You can't sell that right now.")
    
    def die():
        print("You're dead! Game over ):")
        sleep(5)
        sys.exit(0)


# Enemies inherit most attributes from the player indirectly
# They work very similarly, but are completely independent
class Enemy():
    def __init__(self,name,health,armor):
        self.name = name
        self.health = health
        self.armor = armor
        self.is_alive = True
    
    def check_status(self):
        if self.health <= 0:
            self.is_alive = False
        else:
            pass
        
        if self.is_alive == False:
            self.die()
    
    def change_health(self,value):
        if self.health > 0:
            self.health = self.health - value
        elif self.health <= 0:
            self.is_alive = False
        self.check_status


class Item():
    def __init__(self,name,description,value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    def __eq__(self,other):
        return self.name == other
    def description(self):
        return "%s: %s. Damage: %s. Worth %s gold" % (self.name, self.description, self.damage, self.value)


# Weapons inherit from items, but have another damage var
class Weapon(Item):
    def __init__(self,name,description,value,damage):
        self.damage = damage
        super().__init__(name, description, value)


# Armor inherits from items, but also have an armor var
class Armor(Item):
    def __init__(self,name,description,value,armor):
        self.armor = armor
        super().__init__(name, description, value)
