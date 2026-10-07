# importtaa funktion joka kysyy pelaajan nimen ja iän. Myös kaikki huoneet, loppu tekstit ja luokat huoneiden kautta
from user_info import *
from rooms import *
from ending_texts import *

# Pelaajan aloitus itemit, inventory ja pelaa olion alustus.
inventory_list = [Item("Money")]
inventory = "Inventory"
# Ensimmäisen huoneen luominen.
current_room = create_room(1)[0]
player = Player("", inventory_list, current_room)

# Pelaajan kaikki toiminnot koko pelin aikana. Ottaa parametrinä aloitus huoneen ja muokkaa sitä pelin aikana.
def user_actions(current_room:Room):
    ending = ""
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
        elif input_choice.lower() == current_room.action_list["Talk"].lower(): # Talk Action
            current_room.talk()
            if "Book" in player.inventory and ending == "":
                return ending
        elif input_choice.lower() == current_room.action_list["Move"].lower(): # Move Action
            if current_room == Castle:
                print(f"Thank you {player.name}! But our dragon is not in another castle!")
            elif input("You can't come back if you move to the next area. Do you still want to go? (yes/no): ") == "yes".lower():
                ending = create_room(Room.current_location+2, inventory_list)[1]
                current_room = current_room.move()
                print(current_room.text_list["Move"][0])
        elif "Sleep" in current_room.action_list and input_choice.lower() == current_room.action_list["Sleep"].lower(): # Sleep Action
            current_room.sleep()
        elif "Cook" in current_room.action_list and input_choice.lower() == current_room.action_list["Cook"].lower(): # Cook Action
            current_room.cook()
        elif "Attack" in current_room.action_list and input_choice.lower() == current_room.action_list["Attack"].lower(): # Attack Action
            if ending == "":
                current_room.attack()
            else:
                return ending
        elif "Restart" in current_room.action_list and input_choice.lower() == current_room.action_list["Restart"].lower(): # Restart Action
                current_room = current_room.restart()
                print(current_room.text_list["Move"][0])
        elif input_choice.lower() == inventory.lower(): # Inventory Action
            print_inventory = []
            for i in player.inventory:
                print_inventory.append(i.name)
            print(print_inventory)

ask_user_info()
# with open("save.txt", "w") as tiedosto:
#     tiedosto.write("Pelaajan nimi")
# with open("save.txt", "r") as tiedosto:
#     data = tiedosto.read()
#     print(data)
print(current_room.text_list["Move"][0])
ending = user_actions(current_room)
print("")
input("Press enter to continue ")
print("")
endings(ending)
