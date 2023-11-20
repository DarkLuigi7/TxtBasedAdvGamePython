from room import Room
from item import*
from character import*

#initialise

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
susan = Enemy("susan", "the skeleton")
susan.set_conversation("i've got a BONE to pick with you")
susan.set_weakness("acid")
ballroom.set_character(susan)
current_room = kitchen

#end of initialisation

def select_character(inhabitant):
    print("\nchoose a character:\n")
    for i in range(len(inhabitant)):
        print(f"{i+1}: {(inhabitant[i]).name}")
        choice = int(input("enter a choice:\t"))
        return inhabitant[choice-1]
    
#main loop:
while True:
    print("\n")
    print(f"You are in the {current_room.name}\n")
    current_room.get_details()
    print("\n")
    inhabitant = current_room.get_character()
    
    for i in range(len(inhabitant)):
        inhabitant[i].describe()
    command = input(">")
    if command in ["North", "South", "East", "West"]:
        current_room = current_room.move(command)
    elif command  == "talk":
        if inhabitant != 0:
            select_character(inhabitant).talk()
        else:
            print("nobody is here")
    elif command == "fight":
        if inhabitant != 0:
            select_character(inhabitant).fight(current_room)
        else:
            print("there is nobody here to fight")
    elif command == "bribe":
        if inhabitant != 0:
            select_character(inhabitant).bribe(current_room)
        else:
            print("nobody is here to bribe")
    elif command == "commands":
            print("list of commands:\n- North / South / East / West\n- talk\n- fight\n- bribe")
    else:
        print("command not recognised")

#end of main loop








