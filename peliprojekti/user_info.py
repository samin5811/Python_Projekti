import random
from paketti import Player
from paketti import Room
from paketti import Item

inventory = []
pillow = Item("Pillow", random.randint(1,10))
bedroom = Room("Bedroom", pillow)
player = Player("", inventory, pillow)
username = input("What is your name? ")
user_age = input("What is your age? ")

action1 = "take item"
action2 = "inventory"
action3 = "drop item"
action4 = "quit"


def action_1():
    taken_item = input("What item do you want to take?: ")
    inventory.append(taken_item)
    return
def action_2():
    print("Opening inventory...")
    print(inventory)
    return
def action_3():
    dropped_item = input("What item do you want to drop?: ")
    for item in inventory:
        if dropped_item == item:
            inventory.remove(item)
    return
def action_4():
    print("Quitting...")
    return

print(f"Your name is {username} and your age is {user_age}. Is this correct? (yes/no)")
if input().lower() == "yes":
    if int(user_age) < 12:
        print("You are too young.")
        raise SystemExit
    else:
        print("Welcome.")

while True:
    print("")
    print(action1)
    print(action2)
    print(action3)
    print(action4)
    input_choice = input("\nEnter an option: ")
    if input_choice.lower() == action4:
        raise SystemExit
    elif input_choice.lower() == action1:
        action_1()
    elif input_choice.lower() == action2:
        action_2()
    elif input_choice.lower() == action3:
        action_3()