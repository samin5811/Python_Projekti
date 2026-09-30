import random
from user_info import *
from rooms import *

inventory_list = [Item("Money")]
inventory = "Inventory"

player = Player("", inventory_list, bedroom)

current_room = bedroom

def user_actions(current_room:Room):
    while True:
        print("")
        input("Press enter to continue ")
        print("")
        for i in current_room.action_list:
            print(i)
        print("Quit")
        input_choice = input("\nEnter an option: ")
        if input_choice.lower() == "Quit".lower(): # Quit action
            raise SystemExit
        elif input_choice.lower() == current_room.action_list["Take item"].lower(): # Take item action
            current_room.take_item(str(input("What item do you want to take?: ")), player.inventory)
            for i in player.inventory:
                print(i.name)
        elif input_choice.lower() == current_room.action_list["Drop item"].lower(): # Drop item Action
            current_room.drop_item(str(input("What item do you want to drop?: ")), player.inventory)
        elif input_choice.lower() == current_room.action_list["Talk"].lower(): # Talk Action
            current_room.talk()
        elif input_choice.lower() == current_room.action_list["Move"].lower(): # Move Action
            if input("You can't come back if you move to the next area. Do you still want to go? (yes/no): ") == "yes".lower():
                current_room = current_room.move()
        elif input_choice.lower() == current_room.action_list["Sleep"].lower(): # Sleep Action
            current_room.sleep()
        elif input_choice.lower() == current_room.action_list["Cook"].lower(): # Cook Action
            current_room.cook()
        elif input_choice.lower() == inventory.lower(): # Inventory Action
            print_inventory = []
            for i in player.inventory:
                print_inventory.append(i.name)
            print(print_inventory)   
ask_user_info()
user_actions(current_room)