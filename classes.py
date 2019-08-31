from time import sleep
import sys

class Player():
    def __init__(self):
        self.inventory = []
        self.health = 100
        self.armor = 0
        self.is_alive = True
        self.gold = 0

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

    def add_to_inventory(self,item):
        self.inventory.append(item)

    def sell_item(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.gold = self.gold + item.value
        else:
            print("Error: item doesn't exist")
    
    def die():
        print("You're dead! Game over ):")
        sleep(5)
        sys.exit(0)

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


class Weapon(Item):
    def __init__(self,name,description,value,damage):
        self.damage = damage
        super().__init__(name, description, value)


class Armor(Item):
    def __init__(self,name,description,value,armor):
        self.armor = armor
        super().__init__(name, description, value)



     