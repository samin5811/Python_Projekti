class Player:
    def __init__(self, name:str, inventory:list, health=100, damage=1):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.damage = damage

class Room:
    rooms = []
    current_location = 0
    def __init__(self, name:str, items:list, action_list, move_text="Vaihda tämä teksti", talk_text:list=["You talk with the voices in your head."]):
        self.name = name
        self.items = items
        self.move_text = move_text
        self.talk_text = talk_text
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
    def drop_item(self, item_name:str, inventory:list):
        for i in self.items:
            if i.name.lower() == item_name.lower():
                inventory.remove(i)   
                self.items.append(i)
    def talk(self):
        print(self.talk_text[self.talk_index])
        if self.talk_index < self.talk_text.__len__():
            self.talk_index += 1

class Bedroom(Room):
    def __init__(self, name, items, action_list, sleep_text:list=["Vaihda tää teksti"], move_text="Vaihda tämä teksti", talk_text=["You talk with the voices in your head."]):
        super().__init__(name, items, action_list, move_text, talk_text)
        self.sleep_text = sleep_text
        self.sleep_index = 0
    def sleep(self):
        print(self.sleep_text[self.sleep_index])
        if self.sleep_index < self.sleep_text.__len__()-1:
            self.sleep_index += 1
class Kitchen(Room):
    def __init__(self, name, items, action_list, move_text="Vaihda tämä teksti", talk_text = ["You talk with the voices in your head."]):
        super().__init__(name, items, action_list, move_text, talk_text)
class LivingRoom(Room):
    pass
class Item:
    def __init__(self, name:str):
        self.name = name