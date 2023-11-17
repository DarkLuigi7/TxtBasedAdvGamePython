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
dave = Enemy("dave", "is a zombie ")
dave.set_conversation("braaaaaaaaains")
dave.set_weakness("cheese")
dininghall.set_character(dave)
janet = Enemy("janet", "is a skeleton")
janet.set_conversation("i've got a BONE to pick with you")
janet.set_weakness("acid")
ballroom.set_character(janet)
current_room = kitchen
#item = input("choose an item: ")
#dave.fight(item)

def fight():
    if inhabitant is not None:
        item = input("choose an item: ")
        if not (inhabitant.fight(item)):
            print("\n\n\n\t\tgame over")
            break
        current_room.set_character(None)
    else:
        print("nobody is here to fight")
    

while True:
    print("\n")
    print(f"You are in the {current_room.name}")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input(">")
    if command in ["North", "South", "East", "West"]:
        current_room = current_room.move(command)
    elif command  == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("nobody is here")
    elif command == "fight":
        if inhabitant is not None:
            item = input("choose an item: ")
            if not (inhabitant.fight(item)):
                print("\n\n\n\t\tgame over")
                break
            current_room.set_character(None)
        else:
            print("nobody is here to fight")
    elif command == "bribe":
        if inhabitant is not None:
            print(f"you try to bribe {inhabitant.name}")
            offer = int(input(f"enter an offer for {inhabitant.name}"))
            if (inhabitant.bribe(offer)):
                
        else:
            print("nobody is here to bribe")
        








