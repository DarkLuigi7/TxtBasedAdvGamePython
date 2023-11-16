from room import Room
from item import*
from character import*

kitchen = Room("kitchen")
kitchen.set_description("dark dinghy room")
#kitchen.describe()
dininghall = Room("dining hall")
dininghall.set_description("long table littered with speckles of blood")
#dininghall.describe()
ballroom = Room("ballroom")
ballroom.set_description("long abandoned ballroom, this place has not seen dancers in years")
#ballroom.describe()
kitchen.link_room(dininghall, "South")
dininghall.link_room(kitchen, "North")
dininghall.link_room(ballroom, "West")
ballroom.link_room(dininghall, "East")
dave = Enemy("dave", "zombie and that")
dave.set_conversation("oy oy savalloy")
dave.talk()
dave.set_weakness("cheese")
current_room = kitchen
item = input("choose an item: ")
dave.fight(item)



"""while True:
    print("\n")
    print(f"You are in the {current_room.name}")
    current_room.get_details()
    command = input(">")
    current_room = current_room.move(command)"""

