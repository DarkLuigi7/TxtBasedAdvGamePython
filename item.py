class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
class Weapon(Item):
    def __init__(self, name, weight, value, damange, durability, critical):
        super.__init__(name, weight, value)
        self.damage = damage
        self.durability = durability
        self.critical = critical
class Potion(Item):
    def __init__(self, name, weight, value, uses):
        super.__init__(name, weight, value)
        self.uses = uses
        self.duration = duration
class Health(Potion):
    def __init__(self, name, weight, value, uses, health):
        super.__init__(name, weight, value, uses)
        self.health = health
class Damage(Potion):
    def __init__(self, name, weight, value, uses, duration, multiplier):
        super.__init__(name, weight, value, uses)
        self.duration = duration
        self.multiplier = multiplier
class Key(Item):
    def __init__(self, name, weight, value, room):
        super.__init__(name, weight, value)
        self.room = room
