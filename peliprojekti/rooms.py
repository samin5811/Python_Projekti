import copy
from classes import *
basic_actions = {"Take item": "Take item", "Talk": "Talk", "Move": "Move"}
Default_texts = {"Talk":["You talk with the voices in your head."], "Move":["Vaihda tämä teksti"]}

# Room 1
pillow = Item("Pillow")
book = Item("Book")
bedroom_actions = basic_actions.copy()
bedroom_actions["Sleep"] = "Sleep"
bedroom_texts = copy.deepcopy(Default_texts)
bedroom_texts["Move"][0] = "You wake up early in the morning and get out of bed. Then you look around your messy room and see your [pillow] on the floor and a random [book] under your broken window."
bedroom_texts["Sleep"] = ["You fall back on your bed and close your eyes to fall asleep. You wake up couple hours later.", "You are not tired."]
bedroom = Bedroom("Bedroom", [pillow, book], bedroom_actions, bedroom_texts)

# Room 2
knife = Item("Knife")
kitchen_actions = basic_actions.copy()
kitchen_actions["Cook"] = "Cook"
kitchen_texts = copy.deepcopy(Default_texts)
kitchen_texts["Move"][0] = "You go into your kitchen and check the fridge... it's empty. But you can still cook the pizza in your freezer. You also see a [knife] on the floor and think to yourself 'that's dangerous'."
kitchen_texts["Cook"] = ["You take the pizza from the freezer and cook it on the stove flipping it every now and then. After some time you eat half of the pizza and you feel energized.", "You are not hungry."]
kitchen = Kitchen("Kitchen", [knife], kitchen_actions, kitchen_texts)

# Room 3
clothes = Item("Clothes")
living_room_actions = basic_actions.copy()
living_room_texts = copy.deepcopy(Default_texts)
living_room_texts["Move"][0] = "You go into your living room and see some [clothes] scattered around. You go to your front door and pick up todays newspaper. On the front page you see a headline 'a dragon has destroyed all food in the village and nobody can make pizza anymore'. You know what you need to do."
living_room = LivingRoom("Living room", [clothes], living_room_actions, living_room_texts)

# Room 4
rock = Item("Rock")
outside_actions = basic_actions.copy()
outside_actions["Attack"] = "Attack"
outside_texts = copy.deepcopy(Default_texts)
outside_texts["Move"][0] = "You go outside and see the dragon on top of the castle on the hill beyond the forest. As you start your journey before you get to the forest you meet a goblin who throws a [rock] in front of you."
outside_texts["Talk"] = ["The goblin says something but you don't understand it."]
outside_texts["Attack"] = ["You knock out the goblin with your fist.", "You kick the unconscious goblin. No respect for goblins."]
outside = Outside("Outside", [rock], outside_actions, outside_texts)

# Room 5
helmet = Item("Helmet")
forest_actions = basic_actions.copy()
forest_actions["Attack"] = "Attack"
forest_texts = copy.deepcopy(Default_texts)
forest_texts["Move"][0] = "You continue your journey into the forest and hear strange noises. You see a shadowy figure in the distance. When you get closer you realize it's and orc. You also see a [helmet] on the ground."
forest_texts["Talk"] = ["The orc says something but you don't understand it."]
forest_texts["Attack"] = ["You go in for a swing but the orc blocks it. Now it looks angry.", "You want to swing again but the orc attacks first. You Dodge the attack and use your special technique to knock down the orc.", "You kick the unconscious orc. No respect for orcs."]
forest = Forest("Forest", [helmet], forest_actions, forest_texts)

# Room 6
pile_of_pizza = Item("Pile of Pizza")
castle_actions = basic_actions.copy()
castle_actions["Attack"] = "Attack"
castle_texts = copy.deepcopy(Default_texts)
castle_texts["Move"][0] = "You run to the castle and burst in through the gates. The dragon is right in front of you. Between you and the dragon is a [pile of pizza]."
castle_texts["Talk"] = ["The dragon says something but you don't understand it."]
castle_texts["Attack"] = ["You run towards the dragon and it starts to breathe fire. You dodge the fire and use your ultimate technique to pierce through the dragons scales and cut its tail off. Wicked! The dragon flees without its tail between its legs.", "You kick the dragon tail. No respect for dragons."]
castle = Castle("Castle", [pile_of_pizza], castle_actions, castle_texts)

# Room 7
ending_actions = {"Restart": "Restart"}
ending_texts = copy.deepcopy(Default_texts)
ending_texts["Move"][0] = "You have defeated the dragon and saved the village. To celebrate your victory everyone eats raw dragon tail pizza."
ending = Ending("Ending", [], ending_actions, ending_texts)