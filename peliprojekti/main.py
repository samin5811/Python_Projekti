import json
# importtaa funktion joka kysyy pelaajan nimen ja iän. Myös kaikki huoneet, loppu tekstit ja luokat huoneiden kautta
from user_info import *
from rooms import *
from ending_texts import *

# Pelaajan aloitus itemit, inventory ja pelaa olion alustus.
starting_items = [Item("Money").name]
inventory = "Inventory"
# Ensimmäisen huoneen luominen.
current_room = create_room(1, starting_items)[0]
player = Player("", starting_items, current_room)
ending = ""
endings_found = []

# Pelaajan kaikki toiminnot koko pelin aikana. Ottaa parametrinä aloitus huoneen ja muokkaa sitä pelin aikana.
def user_actions(current_room:Room, ending=[]):
    while True:
        save_game()
        print("")
        input("Press enter to continue ")
        print("")
        for i in current_room.action_list:
            print(i)
        print("Inventory")
        print("Quit")
        input_choice = input("\nEnter an action: ")
        if input_choice.lower() == "Quit".lower(): # Quit action
            raise SystemExit
        elif input_choice.lower() == current_room.action_list["Take item"].lower(): # Take item action
            inventory_lenght = player.inventory.__len__()
            taken_item = current_room.take_item(str(input("What item do you want to take?: ")), player.inventory)
            if inventory_lenght == player.inventory.__len__():
                print("\nItem not found")
            else:
                print(f"\nYou picked up {taken_item}")
        elif input_choice.lower() == current_room.action_list["Talk"].lower(): # Talk Action
            current_room.talk()
            if ending and current_room.text_list["Talk"].__len__() == 1:
                return ending[1]
        elif input_choice.lower() == current_room.action_list["Move"].lower(): # Move Action
            if ending:
                print(f"Thank you {player.name}! But our dragon is not in another castle!")
            elif input("You can't come back if you move to the next area. Do you still want to go? (yes/no): ") == "yes".lower():
                print("")
                ending = create_room(Room.current_location+2, player.inventory)[1]
                current_room = current_room.move()
                print(current_room.text_list["Move"][0])
        elif "Sleep" in current_room.action_list and input_choice.lower() == current_room.action_list["Sleep"].lower(): # Sleep Action
            current_room.sleep()
        elif "Cook" in current_room.action_list and input_choice.lower() == current_room.action_list["Cook"].lower(): # Cook Action
            current_room.cook()
        elif "Attack" in current_room.action_list and input_choice.lower() == current_room.action_list["Attack"].lower(): # Attack Action
            current_room.attack()
            if ending != []:
                return ending[0]
        elif "Restart" in current_room.action_list and input_choice.lower() == current_room.action_list["Restart"].lower(): # Restart Action
                current_room = current_room.restart()
                print(current_room.text_list["Move"][0])
        elif input_choice.lower() == inventory.lower(): # Inventory Action
            print_inventory = []
            for i in player.inventory:
                print_inventory.append(i)
            print(print_inventory)
        else:
            print("Action not found")

# Tallenna save file
def save_game():
        save_data = {"player": player.name, "room": current_room.name, "inventory": player.inventory, "room_number": Room.current_location+1, "outside": (Outside.talk_index, Outside.attack_index), "forest": (Forest.talk_index, Forest.attack_index), "endings": endings_found}
        with open("save.json", "w") as tiedosto:
            json.dump(save_data, tiedosto)

# Lue save file
try:
    # Tämä jos peli jäi kesken
    with open("save.json", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
        player.name = data_luettu['player']
        player.inventory = data_luettu['inventory']
        endings_found = data_luettu['endings']
        Outside.talk_index = data_luettu['outside'][0]
        Outside.attack_index = data_luettu['outside'][1]
        Forest.talk_index = data_luettu['forest'][0]
        Forest.attack_index = data_luettu['forest'][1]
        print(f"Player name: {data_luettu['player']}, Room: {data_luettu['room']}, Inventory: {data_luettu['inventory']}, Endings found: {endings_found.__len__()}/16")
        if data_luettu['room_number'] >=2:
            for i in range(2, data_luettu['room_number']+1):
                current_room_and_ending = create_room(i, player.inventory)
                Room.current_location += 1
            current_room = current_room_and_ending[0]
            ending = current_room_and_ending[1]
            print("")
            print(current_room.text_list["Move"][0])
        else:
            print("")
            print(current_room.text_list["Move"][0])
except json.decoder.JSONDecodeError:
    # Tämä jos save.json on tyhjä
    player.name = ask_user_info()[0]
    print("")
    print(current_room.text_list["Move"][0])
except KeyError:
    # Tämä jos pelin pääsi läpi
    with open("save.json", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
        player.name = data_luettu['player']
        endings_found = data_luettu['endings']
    print("")
    print(current_room.text_list["Move"][0])

ending = user_actions(current_room, ending)
print("")
input("Press enter to continue ")
print("")
endings(ending, endings_found)
print("")
print(f"Endings found: {endings_found.__len__()}/16")
with open("save.json", "w") as tiedosto:
    json.dump({"player": player.name, "endings": endings_found}, tiedosto)