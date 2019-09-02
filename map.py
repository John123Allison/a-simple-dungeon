from classes import *
from functions import *

# Rooms are defined with a coordinate that cooresponds to graph. 
# Players are presented with a choice, and based off that choice, another room function is called.

def room00():
    print("You are in a room with Foo")

    choice = input("> ")

    if "east" in choice:
        room01()

def room01():
    print("foo")