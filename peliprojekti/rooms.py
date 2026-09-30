from classes import *
basic_actions = {"Take item": "Take item", "Drop item": "Drop item", "Talk": "Talk", "Move": "Move"}
Default_texts = {"Talk":["You talk with the voices in your head."], "Move":["Vaihda tämä teksti"]}
# Room 1
pillow = Item("Pillow")
bedroom_actions = basic_actions.copy()
bedroom_actions["Sleep"] = "Sleep"
bedroom = Bedroom("Bedroom", [pillow], bedroom_actions)
bedroom.text = "You wake up early in the morning and get out of bed. Then you look around your messy room and see your pillow."
bedroom.sleep_text = ["You fall back on your bed and close your eyes to fall asleep. You wake up couple hours later.", "You are not tired."]

# Room 2
knife = Item("Knife")
kitchen_actions = basic_actions.copy()
kitchen_actions["Cook"] = "Cook"
kitchen = Kitchen("Kitchen", [knife], kitchen_actions)

# Room 3
living_room_actions = basic_actions.copy()
living_room = Room("Living room", [], basic_actions)
