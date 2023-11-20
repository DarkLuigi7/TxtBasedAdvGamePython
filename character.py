import random
class Character():
   # Create a character
   def __init__(self, char_name, char_description):
      self.name = char_name
      self.description = char_description
      self.conversation = None
   # Describe this character
   def describe(self):
      print(self.name + " is here!")
      print(self.description)
   # Set what this character will say when talked to
   def set_conversation(self, conversation): # its this one
      self.conversation = conversation
   # Talk to this character
   def talk(self):
      if self.conversation is not None:
         print(f"{self.name} says: {self.conversation}")
      else:
         print(f"{self.name} doesn't want to talk to you")
   # Fight with this character
   def fight(self, combat_item):
      print(f"{self.name} doesn't want to fight with you")
      return True
class Enemy(Character):
   def __init__(self, char_name, char_description):
      super().__init__(char_name, char_description)
      self.weakness = None
   def set_weakness(self, weakness):
      self.weakness = weakness
   def get_weakness(self):
      return self.weakness
   def fight(self, current_room):
      item = input("choose an item: ")
      if item == self.weakness:
         print(f"{self.name} KO")
         current_room.remove_character(self)
      else:
         print("it isn't very effective")
         print("\n\n\n\t\tgame over")
         exit()
   def bribe(self, current_room):
      print(f"you try to bribe {self.name}")
      offer = int(input(f"enter an offer for {choice.name}: "))
      want = random.randrange(5,15)
      if offer > want:
         print(f"{self.name} accepts your offer")
         print(f"{self.name} vacates the area")
         current_room.remove_character(self)
      else:
         print(f"\"This is not enough!!!! I wanted at least {want} gold!!!!\"")
         print(f"{self.name} initiates a fight with you")
         item = input("choose an item: ")
         self.fight(item, current_room)
class Friend(Character):
   pass
