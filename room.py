class Room():
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = []
    def set_description(self, room_description):
        self.description = room_description
    def get_description(self):
        return self.descriptio
    def set_character(self, character):
        self.character.append(character)
    def remove_character(self, character):
        (self.character).remove(character)
    def get_character(self):
        return self.character
    def set_name(self, name):
        self.name
    def get_name(self):
        return self.name
    def describe(self):
        print(self.description)
    def link_room(self, roomtolink, direction):
        self.linked_rooms [direction] = roomtolink
        #print(f"{self.name} linked rooms: {repr(self.linked_rooms)}")
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")
    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
        
