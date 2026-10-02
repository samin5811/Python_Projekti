class Player:
    def __init__(self, name:str, inventory:list, health=100, damage=1):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.damage = damage

class Room:
    rooms = []
    current_location = 0
    def __init__(self, name:str, items:list, action_list, text_list):
        self.name = name
        self.items = items
        self.text_list = text_list
        self.action_list = action_list
        self.talk_index = 0
        Room.rooms.append(self)
    def move(self):
        Room.current_location += 1
        next_room = Room.rooms[Room.current_location]
        return next_room
    def take_item(self, item_name:str, inventory:list):
        for i in self.items:
            if i.name.lower() == item_name.lower():
                inventory.append(i)   
                self.items.remove(i)
    def talk(self):
        print(self.text_list["Talk"][self.talk_index])
        if self.talk_index < self.text_list["Talk"].__len__()-1:
            self.talk_index += 1

class Bedroom(Room):
    def __init__(self, name, items, action_list, text_list):
        super().__init__(name, items, action_list, text_list)
        self.sleep_index = 0
    def sleep(self):
        print(self.text_list["Sleep"][self.sleep_index])
        if self.sleep_index < self.text_list["Sleep"].__len__()-1:
            self.sleep_index += 1
class Kitchen(Room):
    def __init__(self, name, items, action_list, text_list):
        super().__init__(name, items, action_list, text_list)
        self.cook_index = 0
    def cook(self):
        print(self.text_list["Cook"][self.cook_index])
        if self.cook_index < self.text_list["Cook"].__len__()-1:
            self.cook_index += 1
class LivingRoom(Room):
    def __init__(self, name, items, action_list, text_list):
        super().__init__(name, items, action_list, text_list)
class Outside(Room):
    def __init__(self, name, items, action_list, text_list):
        super().__init__(name, items, action_list, text_list)
        self.attack_index = 0
    def attack(self):
        print(self.text_list["Attack"][self.attack_index])
        if self.attack_index < self.text_list["Attack"].__len__()-1:
            self.attack_index += 1
class Forest(Outside):
    def __init__(self, name, items, action_list, text_list):
        super().__init__(name, items, action_list, text_list)
class Castle(Outside):
    def __init__(self, name, items, action_list, text_list):
        super().__init__(name, items, action_list, text_list)
class Ending(Room):
    def __init__(self, name, items, action_list, text_list):
        super().__init__(name, items, action_list, text_list)
    def restart(self):
        Room.current_location = 0
        next_room = Room.rooms[Room.current_location]
        return next_room
class Item:
    def __init__(self, name:str):
        self.name = name