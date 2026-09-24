class Player:
    def __init__(self, name:str, items:list, location:Room):
        self.name = name
        self.items = items
        self.location = location
    def Move(self, destination:Room):
        self.destination = destination
    def Take_item(self):
        pass

class Room:
    def __init__(self, name:str, item:Item):
        self.name = name
        self.item = item

class Item:
    def __init__(self, name:str, weight:float):
        self.name = name
        self.weight = weight