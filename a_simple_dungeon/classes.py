from time import sleep
from random import choice
import sys


class Player():
    """Most values of players are stored as variables, with the inventory as a simple list
    values of the player's status are changed by methods attached to the class"""
    def __init__(self):
        self.inventory = []
        self.spells = []
        self.health = 100 # affected by interactions with weapon objects
        self.max_health = self.health
        self.mana = 20
        self.max_mana = self.mana
        self.armor = 0 # affected by inventory
        self.weapon = 0
        self.is_alive = True # set to false to trigger restart and/or death sequence
        self.gold = 0
        self.location = None

        self.job = "Adventurer"
        self.level = 1
        self.xp = 0
        self.constitution = 3
        self.strength = 3
        self.dexterity = 3
        self.intellect = 3
        self.luck = 3


    def choose_race(self):
        r = input("Of what race were you born?\n1. Human\n2. Elf\n3. Dwarf\n> ").lower()
        if "human" in r or "1" in r:
            self.race = "Human"
            self.constitution += 3
            self.strength += 1
            self.dexterity += 1
            self.intellect += 1
            self.luck += 2
        elif "elf" in r or "2" in r:
            self.race = "Elf"
            self.constitution += 1
            self.strength += 1
            self.dexterity += 3
            self.intellect += 2
            self.luck += 1
        elif "dwarf" in r or "3" in r:
            self.race = "Dwarf"
            self.constitution += 3
            self.strength += 3
            self.dexterity += 0
            self.intellect += 1
            self.luck += 0

    def choose_job(self):
        r = input("What job did you have?\n1. Warrior\n2. Hunter\n3. Thief\n4. Noble\n5. Alchemist\n> ").lower()
        if "warrior" in r or "1" in r:
            self.job = "Warrior"
            self.constitution += 2
            self.strength += 2
            self.dexterity += 2
        elif "hunter" in r or "2" in r:
            self.job = "Hunter"
            self.constitution += 1
            self.strength += 1
            self.dexterity += 3
            self.intellect += 1
        elif "thief" in r or "3" in r:
            self.job = "Thief"
            self.dexterity += 3
            self.intellect += 2
            self.luck += 3
        elif "noble" in r or "4" in r:
            self.job = "Noble"
            self.dexterity += 1
            self.intellect += 3
            self.luck += 1
        elif "alchemist" in r or "5" in r:
            self.job = "Alchemist"
            self.constitution += 2
            self.strength += 2
            self.intellect += 2

    def xp_need(self):
        return(30+(self.level*25+self.level*10))

    def check_status(self):
        #Character
        print("--------------------------------------")
        print("Level %s %s %s" % (self.level,self.race,self.job))
        print("XP: %s / %s" % (self.xp,self.xp_need()))
        print("Health: %s / %s" % (self.health,self.max_health))
        print("Mana: %s / %s" % (self.mana,self.max_mana))
        #Equipment
        print("--------------------------------------")
        if self.weapon != 0:
            print("Weapon: %s" % (self.weapon.name))
        else:
            print("Weapon: Unarmed")
        if self.armor != 0:
            print("Armor: %s" % (self.armor.name))
        else:
            print("Armor: Unclothed")
        print("Gold: %s" % (self.gold))
        #Stats
        print("--------------------------------------")
        print("CON: %s" % (self.constitution))
        print("STR: %s" % (self.strength))
        print("DEX: %s" % (self.dexterity))
        print("INT: %s" % (self.intellect))
        print("LUK: %s" % (self.luck))
        print("--------------------------------------")

    def status(self):
        if self.health <= 0:
            self.is_alive = False
        else:
            pass

        if self.is_alive == False:
            self.die()

    def change_health(self, value):
        if self.health > 0:
            self.health = self.health + value
        elif self.health <= 0:
            self.is_alive = False
        self.check_status

    def add_to_inventory(self, item):
        """
        Takes arg item.
        """
        self.inventory.append(item)

    def unequip_weapon(self):
        if self.weapon == 0:
            print("You are not wielding anything")
        else:
            print(self.weapon.name + " was unequipped")
            self.inventory.append(self.weapon)
            self.weapon = 0

    def equip_weapon(self, item):
        """
        Takes arg item.
        """
        equipped_something = False
        for x in self.inventory:
            if x.name.lower() == item:
                if self.weapon != 0:
                    self.unequip_weapon()
                self.weapon = x
                self.inventory.remove(x)
                print(self.weapon.name + " is now equipped")
                equipped_something = True
                break
        if equipped_something == False:
            print("That's not a weapon")

    def gain_xp(self, amount):
        """
        Takes arg amount.
        """
        self.xp += amount
        xpneed = self.xp_need()
        # check for level up
        while self.xp >= xpneed:
            self.xp -= xpneed
            self.level += 1
            print("Level Up!\nYou reached level %s" % (self.level))
            i = 0
            # increase random stats
            while i < choice(range(2,4)):
                i += 1
                a = choice(range(1,5))
                if (a == 1):
                    self.constitution += 1
                    print("Constitution increases by 1")
                elif (a == 2):
                    self.strength += 1
                    print("Strength increases by 1")
                elif (a == 3):
                    self.dexterity += 1
                    print("Dexterity increases by 1")
                elif (a == 4):
                    self.intellect += 1
                    print("Intellect increases by 1")
                elif (a == 5):
                    self.luck += 1
                    print("Luck increases by 1")

            # Update resources to reflect new stats
            update_stats()

    def update_stats(self):
        self.max_health = self.constitution*20
        self.health = self.max_health
        self.max_mana = self.intellect*5
        self.mana = self.max_mana

    def learn_spell(self, spell):
        """
        Takes arg spell.
        """
        self.spells.append(spell)

    def list_inventory(self):
        if not self.inventory:
            print("--------------Inventory---------------")
            print("empty")
            print("--------------------------------------")
        else:
            print("--------------Inventory---------------")
            for x in self.inventory:
                print(x.name)
            print("--------------------------------------")

    def sell_item(self, item):
        """
        Takes arg item.
        """
        for x in self.inventory:
            if x.name == item:
                self.inventory.remove(x)
                self.gold = self.gold + x.value
            else:
                print("Error: item doesn't exist")

    def inspect_item(self, item):
        for x in self.inventory:
            if x.name == item:
                print(x)

    def die(self):
        print("You're dead! Game over ):")
        sleep(5)
        sys.exit(0)


class Enemy():
    """Enemies inherit most attributes from the player indirectly
    They work very similarly, but are completely independent.
    Initialized with name, health, armor."""
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage
        self.is_alive = True

    def check_status(self):
        if self.health <= 0:
            self.is_alive = False
        else:
            pass

        if self.is_alive == False:
            self.die()

    def change_health(self, value):
        if self.health > 0:
            self.health = self.health - value
        elif self.health <= 0:
            self.is_alive = False
        self.check_status


class Item():
    """Attributes name, description, and value. Method description returns a formatted string displaying the item information. 
    Initialized with name, description, value."""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    def __eq__(self,other):
        return self.name == other
    def description(self):
        return "%s: %s. Damage: %s. Worth %s gold" % (self.name, self.description, self.damage, self.value)



class Weapon(Item):
    """Weapons inherit from items, but have another damage var."""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)


class Armor(Item):
    """Armor inherits from items, but also has an armor var."""
    def __init__(self, name, description, value, armor):
        self.armor = armor
        super().__init__(name, description, value)
