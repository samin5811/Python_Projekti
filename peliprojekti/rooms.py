import copy
# Importtaa luokat
from classes import *
basic_actions = {"Take item": "Take item", "Talk": "Talk", "Move": "Move"}
Default_texts = {"Talk":["You talk with the voices in your head."], "Move":["Vaihda tämä teksti"]}

# Kaikki huoneet ja niiden luomis funktio
def create_room(room_number:int, player_inventory:list, ending=""):
    current_room = ""
    goblin = "Goblin"
    orc = "Orc"
    if room_number == 1:
        # Room 1
        pillow = Item("Pillow")
        book = Item("Book")
        bedroom_actions = basic_actions.copy()
        bedroom_actions["Sleep"] = "Sleep"
        bedroom_texts = copy.deepcopy(Default_texts)
        bedroom_texts["Move"] = ["You wake up early in the morning and get out of bed. Then you look around your messy room and see your [pillow] on the floor and a random [book] under your broken window."]
        bedroom_texts["Sleep"] = ["You fall back on your bed and close your eyes to fall asleep. You wake up couple hours later.", "You are not tired."]
        bedroom = Bedroom("Bedroom", [pillow, book], bedroom_actions, bedroom_texts)
        current_room = bedroom
    if room_number == 2:
        # Room 2
        knife = Item("Knife")
        kitchen_actions = basic_actions.copy()
        kitchen_actions["Cook"] = "Cook"
        kitchen_texts = copy.deepcopy(Default_texts)
        kitchen_texts["Move"] = ["You go into your kitchen and check the fridge... it's empty. But you can still cook the pizza in your freezer. You also see a [knife] on the floor and think to yourself 'that's dangerous'."]
        kitchen_texts["Cook"] = ["You take the pizza from the freezer and cook it on the stove flipping it every now and then. After some time you eat half of the pizza and you feel energized.", "You are not hungry."]
        kitchen = Kitchen("Kitchen", [knife], kitchen_actions, kitchen_texts)
        current_room = kitchen
    if room_number == 3:
        # Room 3
        clothes = Item("Clothes")
        living_room_actions = basic_actions.copy()
        living_room_texts = copy.deepcopy(Default_texts)
        living_room_texts["Move"] = ["You go into your living room and see some [clothes] scattered around. You go to your front door and pick up todays newspaper.\nOn the front page you see a headline 'a dragon has destroyed all food in the village and nobody can make pizza anymore'. You know what you need to do."]
        living_room = LivingRoom("Living room", [clothes], living_room_actions, living_room_texts)
        current_room = living_room
    if room_number == 4:
        # Room 4
        rock = Item("Rock")
        outside_actions = basic_actions.copy()
        outside_actions["Attack"] = "Attack"
        outside_texts = copy.deepcopy(Default_texts)
        if "Book" in player_inventory and "Knife" in player_inventory:
            outside_texts["Move"] = ["You go outside and see the dragon on top of the castle on the hill beyond the forest. As you start your journey before you get to the forest, you meet a goblin who throws a [rock] at your face\nbut you cut the rock in half with your knife and take a defensive stance."]
            outside_texts["Talk"] = ["The goblin says that he needs help stopping his friend the dragon rampaging in the castle but there is something wrong with his story. How can a goblin and dragon be friends? Will you trust him?","You try to ask him more details but he keeps saying that he doesn't have time to talk. He needs your help now!"]
            outside_texts["Attack"] = ["You ready you knife and dash forward to attack the goblin. The goblin starts running away but you catch up and defeat the goblin with one hit to his head.", "You kick the unconscious goblin. No respect for goblins."]
        elif "Book" in player_inventory:
            outside_texts["Move"] = ["You go outside and see the dragon on top of the castle on the hill beyond the forest. As you start your journey before you get to the forest you meet a goblin who throws a [rock] in front of you."]
            outside_texts["Talk"] = ["The goblin says that he needs help stopping his friend the dragon rampaging in the castle but there is something wrong with his story. How can a goblin and dragon be friends? Will you trust him?", "You try to ask him more details but he keeps saying that he doesn't have time to talk. He needs your help now!"]
            outside_texts["Attack"] = ["You knock out the goblin with your fist.", "You kick the unconscious goblin. No respect for goblins."]
        elif "Knife" in player_inventory:
            outside_texts["Move"] = ["You go outside and see the dragon on top of the castle on the hill beyond the forest. As you start your journey before you get to the forest, you meet a goblin who throws a [rock] at your face\nbut you cut the rock in half with your knife and take a defensive stance."]
            outside_texts["Talk"] = ["The goblin says something but you don't understand it."]
            outside_texts["Attack"] = ["You ready you knife and dash forward to attack the goblin. The goblin throws another rock at you but you dodge it and defeat the goblin with one swift strike.", "You kick the unconscious goblin. No respect for goblins."]
        else:
            outside_texts["Move"] = ["You go outside and see the dragon on top of the castle on the hill beyond the forest. As you start your journey before you get to the forest you meet a goblin who throws a [rock] in front of you."]
            outside_texts["Talk"] = ["The goblin says something but you don't understand it."]
            outside_texts["Attack"] = ["You knock out the goblin with your fist.", "You kick the unconscious goblin. No respect for goblins."]
        outside = Outside("Outside", [rock], outside_actions, outside_texts)
        current_room = outside
    if room_number == 5:
        # Room 5
        helmet = Item("Helmet")
        forest_actions = basic_actions.copy()
        forest_actions["Attack"] = "Attack"
        forest_texts = copy.deepcopy(Default_texts)
        if "Book" in player_inventory and "Knife" in player_inventory:
            if Outside.attack_index == 0 and Outside.talk_index > 0:
                player_inventory.append(goblin)
                forest_texts["Move"] = ["You continue your journey with the goblin into the forest and hear strange noises. You see a shadowy figure in the distance. When you get closer you realize it's an orc.\nYou ready your knife just in case. You also notice a [helmet] on the ground."]
                forest_texts["Talk"] = ["You and the goblin try to ask the orc to help you with the dragon but the orc doesn't say anything and just pick up his weapon.", "You tell the orc to drop his weapon but he doesn't.", "You ask the orc if he wants to join you but still no response."]
                forest_texts["Attack"] = ["You charge at the orc with your knife but the orc blocks your attack and kicks you down.", " The orc attacks while you're down but the goblin attacks the orc and together you manage to defeat it.", "You kick the unconscious orc. No respect for orcs."]
            else:
                forest_texts["Move"] = ["You continue your journey into the forest and hear strange noises. You see a shadowy figure in the distance. When you get closer you realize it's an orc. You ready your knife just in case.\nYou also noitce a [helmet] on the ground."]
                forest_texts["Talk"] = ["You greet the orc and wait to see his reaction. The orc picks up his weapon and stares at you.", "You tell the orc about your mission to stop the dragon and he silenty just listens to you.", "You ask if the orc wants to join you on your journey and he just nods his head."]
                forest_texts["Attack"] = ["You charge at the orc with your knife and the orc blocks your attack but you cut through his weapon and armor.", " Disarmed and wounded the orc can't fight back and you defeat the orc.", "You kick the unconscious orc. No respect for orcs."]
        elif "Book" in player_inventory:
            if Outside.attack_index == 0 and Outside.talk_index > 0:
                player_inventory.append(goblin)
                forest_texts["Move"] = ["You continue your journey with the goblin into the forest and hear strange noises. You see a shadowy figure in the distance. When you get closer you realize it's an orc.\nYou also notice a [helmet] on the ground."]
                forest_texts["Talk"] = ["You and the goblin try to ask the orc to help you with the dragon but the orc doesn't say anything and just pick up his weapon.", "You tell the orc to drop his weapon but he doesn't.", "You ask the orc if he wants to join you but still no response."]
                forest_texts["Attack"] = ["You go in for a swing but the orc blocks it. Now it looks angry.", "You want to swing again but the orc attacks first. You try to dodge the attack but you are too slow and get knocked down. The orc tries to hit you again while you're down but the goblin comes from behind and knocks out the orc.", "You kick the unconscious orc. No respect for orcs."]
            else:
                forest_texts["Move"] = ["You continue your journey into the forest and hear strange noises. You see a shadowy figure in the distance. When you get closer you realize it's an orc. You also notice a [helmet] on the ground."]
                forest_texts["Talk"] = ["You greet the orc and wait to see his reaction. The orc picks up his weapon and stares at you.", "You tell the orc about your mission to stop the dragon and he silenty just listens to you.", "You ask if the orc wants to join you on your journey and he just nods his head."]
                forest_texts["Attack"] = ["You go in for a swing but the orc blocks it. Now it looks angry.", "You want to swing again but the orc attacks first. You Dodge the attack and use your special technique to knock down the orc.", "You kick the unconscious orc. No respect for orcs."]
        elif "Knife" in player_inventory:
            forest_texts["Move"] = ["You continue your journey into the forest and hear strange noises. You see a shadowy figure in the distance. When you get closer you realize it's an orc. You ready your knife just in case.\nou also noitce a [helmet] on the ground."]
            forest_texts["Talk"] = ["The orc says something but you don't understand it."]
            forest_texts["Attack"] = ["You charge at the orc with your knife and the orc blocks your attack but you cut through his weapon and armor.", "Disarmed and wounded the orc can't fight back and you defeat the orc.", "You kick the unconscious orc. No respect for orcs."]
        else:
            forest_texts["Move"] = ["You continue your journey into the forest and hear strange noises. You see a shadowy figure in the distance. When you get closer you realize it's an orc. You also notice a [helmet] on the ground."]
            forest_texts["Talk"] = ["The orc says something but you don't understand it."]
            forest_texts["Attack"] = ["You go in for a swing but the orc blocks it. Now it looks angry.", "You want to swing again but the orc attacks first. You Dodge the attack and use your special technique to knock down the orc.", "You kick the unconscious orc. No respect for orcs."]
        forest = Forest("Forest", [helmet], forest_actions, forest_texts)
        current_room = forest
    if room_number == 6:
        # Room 6
        castle_actions = basic_actions.copy()
        castle_actions["Attack"] = "Attack"
        castle_texts = copy.deepcopy(Default_texts)
        if "Book" in player_inventory and "Knife" in player_inventory:
            if player_inventory.__len__() > 6:
                castle_texts["Move"] = ["You slowly make your way to the castle and when i say slowly i mean reallllly slowwwwwly like slower than a snail and when i say slower than a snail it's not a exaggeration,\nduring your walk you actually see a snail passing you and making its way to the castle faster than you. After what feels like years or maybe even decades you arrive at the castle gates. Too weak to even push the doors open you crawl through the doggy door on the gate and when you look up you see the dragon staring at you and for some reason it looks bigger and older than it did when you left your house."]
                castle_texts["Attack"] = ["You are on the ground on all fours how the hell can you attack from there? Anyway the dragon spits a fireball on you."]
                ending = "Overencumbered"
                castle_texts["Talk"] = ["You open your mouth and before you can get even a single syllable out of your mouth the dragon spits a fireball on you"]
                ending = "Overencumbered"
            elif Forest.attack_index == 0 and Forest.talk_index > 1:
                player_inventory.append(orc)
                if goblin in player_inventory:
                    castle_texts["Move"] = ["Three humanoids walked into a castle, one after another: a goblin, an orc, and you. The goblin tries to order the dragon to stop stealing pizza go back home.\nThe orc does the same but with just his eyes never opening his mouth. Then it's your turn what will you do?"]
                    castle_texts["Attack"] = ["Clearly seeing that the dragon can't be talked down you take matters into your own hands. With your knife you slash the dragon from behind while it is distracted by the goblin and orc. The dragon turns around trying to counterattack but turning around only means the goblin and orc can attack from behind it again. It's a hard fight even though it's three against one but eventually you three manage to beat the dragon."]
                    ending = "Unexpected alliance"
                    castle_texts["Talk"] = ["With the goblins silver tongue, the orcs civilization felling stare and your unlimited charisma the three of you manage to convince the dragon to return all the pizzas,\nnever to repeat this incident again."]
                    ending = "Pacifist"
                else:
                    castle_texts["Move"] = ["You and the orc reach the castle gates and together you push the doors open. On the other side is the dragon eating a pile of pizza. You and the orc look at each other and nod.\nBoth of you get ready to face the dragon."]
                    castle_texts["Attack"] = ["Both of you charge at the dragon, with your knife and axe dealing the first blow before the dragons has time to react. The dragon attacks with its fire breath, sharp claws,\nbig bites and tail whips, but with the unbreakble bond you and the orc have, none of the dragons attacks stop your assault. With perfect teamwork, impeccably timed support and assists you manage to defeat the dragon."]
                    ending = "BFF"
                    castle_texts["Talk"] = ["You try to talk to the dragon and the orc is helping by staring at the dragon really hard. You explain that it needs to stop stealing pizzas or it will become hunted by angry villagers.\nYou almost get through to the dragon but it's not enough, feels like you are missing something or somebody. The dragon is done listening and unleashes its fire breath on you almost scorching you, but the orc pushes you away to save you. Seeing your ally burn to ashes in front of you makes something snap in your head and endless rage and bloodlust starts pouring out. With knife in hand you rush to attacks the dragon but you don't even see it because all you're seeing is red."]
                    ending = "Revengeance"
            elif goblin in player_inventory:
                    castle_texts["Move"] = ["You and the goblin arrive at the castle gates. You ask the goblin what's the plan. The goblin explains that you distract the dragon while the goblin deals with it.\nYou don't really understand but the goblin must have a way to deal with it right? You go in the castle and see the dragon in front of you next to a pile of pizza"]
                    castle_texts["Attack"] = ["You get ready to attack and reach for your knife but then you realize your knife is missing. Before you have a chance to figure out what happaned,\nyou look down and see a knife going through your chest. You fall down on the ground and feel somebody emptying your pockets. With your vision and consciousness fading the last thing you hear is the maniacal laughter of your backstabber."]
                    ending = "Backstabbed"
                    castle_texts["Talk"] = ["You try talking to the dragon. The goblin told you exactly what to say to calm down the dragon so this should be easy. As you continue talking, the dragon keeps getting angrier with every word you say\nbut you don't notice it and just keep going."]
                    ending = "Maybe you should not trust the first goblin you see?"
            else:
                castle_texts["Talk"] = ["You talk with your knife about tomorrows breakfast", "Your knife says it want pineapple pizza for breakfast and you consider throwing it far away from you."]
                if Outside.attack_index > 0 and Forest.attack_index > 1:
                    castle_texts["Move"] = ["You slice and dice your way through the castle gates and cut the doors to tiny pieces. You see the dragon in front of you and between you and the dragon is a pile of pizza."]
                    castle_texts["Attack"] = ["The dragon is right in front of you and you get ready to fight, but soon you realize the dragon is not moving. You wait a bit and the dragon falls apart into small bite size pieces,\nthen you realize you accidentally sliced the dragon when cutting the doors. Looks like you are a true master of slicing and dicing."]
                    ending = "Slicing and dicing"
                else:
                    castle_texts["Move"] = ["You go to the castle gates and wonder how you are going to get in."]
                    castle_texts["Attack"] = ["You try to cut the castle gates open but your knife technique is not good enough. While trying to open the gates, the dragon blows the doors down on top of you and you get stuck under the them.\nWith no way to lift the heavy doors, you are stuck alone, hungry and in pain. You die of starvation."]
                    ending = "Sad"
        elif "Book" in player_inventory:
            if Forest.attack_index == 0 and Forest.talk_index > 1:
                player_inventory.append(orc)
                if goblin in player_inventory:
                    castle_texts["Move"] = ["Three humanoids walked into a castle, one after another: a goblin, an orc, and you. The goblin tries to order the dragon to stop stealing pizzas and go back home.\nThe orc does the same but with just his eyes never opening his mouth. Then it's your turn what will you do?"]
                    castle_texts["Attack"] = ["Before the dragon has a chance to do anything you attack it with your fists. The dragon is now angry and is going to attack you but the orc grabs the dragons tail.\nThe goblin jumps on the dragons head and blinds it. With the three of you attacking from all sides it looks like you are winning, until the dragons unleashes all its power and spits fire everywhere burning you and the pile of pizza on the ground. It's a hard fight but eventually you manage to bring down the dragon."]
                    ending = "Lone survivor"
                    castle_texts["Talk"] = ["With the goblins silver tongue, the orcs civilization felling stare and your immeasurable charisma, the three of you manage to convince\nthe dragon to return all the pizzas and never to repeat this incident again."]
                    ending = "Pacifist"
                else:
                    castle_texts["Move"] = ["You and the orc reach the castle gates and together you push the doors open. On the other side is the dragon eating a pile of pizza. You and the orc look at each other and nod.\nBoth of you get ready to face the dragon."]
                    castle_texts["Attack"] = ["Both of you charge at the dragon with your fists, dealing the first blow before the dragons has time to react. The fight is going well, with both you and the orc working in perfect tandem,\nbut without weapons the fight eventually turns around. Everybody is battered and exhausted, the battle will be decided in the next 5 second. You go in for the final blow but the dragon somehow manages to dodge and counterattack. The orc jumps in front of the attack and takes it in your stead, allowing you to defeat the dragon with your last attack, as you fall down on the ground having used up all your strength."]
                    ending = "The Cost of winning"
                    castle_texts["Talk"] = ["You try to talk to the dragon and the orc is helping by staring the dragon really hard. You explain that it need to stop stealing pizzas or it will become hunted by angry villagers.\nYou almost get through to the dragon but it's not enough it feels like you are missing something or somebody. The dragon is done listening and unleashes its fire breath on you almost scorching you but the orc pushes you away to save you. Seeing the orc burn to ashes in front of you makes something makes you get up and run for your life."]
                    ending = "Coward"
            elif goblin in player_inventory:
                    castle_texts["Move"] = ["You and the goblin arrive at the castle gates. You ask the goblin what's the plan. The goblin explains that you distract the dragon while the goblin deals with it.\nYou don't really understand but the goblin must have a way to deal with it right? You go in the castle and see the dragon in front of you next to a pile of pizza"]
                    castle_texts["Attack"] = ["You raise your fists and get ready to attack. The goblin told you all of the dragons attack patterns and habits so this should be an easy fight. You get beaten down extremely badly.\nYou fly against the castle wall and you fall face down on the ground an inch away from dying. With the last of you strength you lift your face and see the reason you are now on the brink of leaving this world. The goblin standing in front of you with a wide grin on its face is the last thing you see when your soul leaves your body. "]
                    ending = "Betrayed"
                    castle_texts["Talk"] = ["You try talking to the dragon. The goblin told you exactly what to say to calm down the dragon so this should be easy. As you continue talking\nthe dragon keeps getting angrier with every word you say but you don't notice it and just keep going."]
                    ending = "Maybe you should not trust the first goblin you see?"
            else:
                castle_texts["Talk"] = ["Your head is empty", "Unga goes #bunga"]
                castle_texts["Move"] = ["You go to the castle through the gates and see the dragon in front of you. Between you and the dragon is a pile of pizza. You raise your fists and\nprepare to fight the dragon."]
                if Outside.attack_index > 0 and Forest.attack_index > 1:
                    castle_texts["Attack"] = ["You charge the dragon and punch it with the force of a centillion pineapple pizzas. With your fist trained in many battles and your technique perfected since this morning.\nYour punch blows away the dragons scales like plucking feathers from a chicken leaving its skin smooth as a baby's bottom. Your punch was so powerful that not even a speck of the dragon is left."]
                    ending = "Strong"
                else:
                    castle_texts["Attack"] = ["You charge the dragon and punch it. You have no battle experience and zero technique so to nobodys surprise the dragon doesn't even flinch.\nWhy did you think you could defeat a dragon with your fists? The dragon stomps on you and only a you sized hole is left in the ground where you once were."]
                    ending = "Weak"
        elif "Knife" in player_inventory:
            castle_texts["Talk"] = ["No time to talk."]
            if Outside.attack_index > 0 and Forest.attack_index > 1:
                castle_texts["Move"] = ["You slice and dice your way through the castle gates and cut the doors to small bite size pieces. You see the dragon in front of you and between you and the dragon is a pile of pizza."]
                castle_texts["Attack"] = ["The dragon is right in front of you and you get ready to fight but soon you realize the dragon is not moving. You wait a bit and the dragon falls apart into small bite size pieces\nthen you realize you accidentally sliced the dragon when cutting the doors. Looks like you are a true master of slicing and dicing."]
                ending = "Slicing and dicing"
            else:
                castle_texts["Move"] = ["You go to the castle gates and wonder how you are going to get in."]
                castle_texts["Attack"] = ["You try to cut the castle gates open but your knife technique is not good enough. While trying to open the gates the dragon blows the doors down on top of you and you get stuck under the them.\nWith no way to lift the heavy doors you are stuck alone, hungry and in pain. You die of starvation."]
                ending = "Sad"
        else:
            castle_texts["Talk"] = ["No time to talk."]
            if player_inventory.__len__() == 1:
                castle_texts["Move"] = ["You run to the castle and burst in through the gates blowing the doors to smithereens. The dragon is right in front of you probably wondering why you have no clothes on.\nBetween you and the dragon is a pile of pizza."]
                castle_texts["Attack"] = ["With no clothes to weigh you down, you run faster than you have ever ran. You are running towards the dragon as it starts to breathe fire but you are so fast it feels like time is slowing down.\nYou dodge the fire and use your ultimate technique to pierce through the dragons scales with your hand and cut its tail off. Wicked! The dragon flees without its tail between its legs.\nYou kick the dragon tail. No respect for dragons."]
                ending = "Speedrun"
            else:
                castle_texts["Move"] = ["You go to the castle through the gates and see the dragon in front of you. Between you and the dragon is a pile of pizza. You raise your fists and\nprepare to fight the dragon."]
                if Outside.attack_index > 0 and Forest.attack_index > 1:
                    castle_texts["Attack"] = ["You charge the dragon and punch it with the force of a centillion pineapple pizzas. With your fist trained in many battles and your technique perfected since this morning,\nyour punch blows away the dragons scales, like plucking feathers from a chicken, leaving its skin smooth as a baby's bottom. Your punch was so powerful that not even a speck of the dragon is left."]
                    ending = "Strong"
                else:
                    castle_texts["Attack"] = ["You charge the dragon and punch it. You have no battle experience to speak of and negative technique, so to nobodys surprise the dragon doesn't even flinch.\nWhy did you think you could defeat a dragon with your fists? The dragon stomps on you and only a you sized hole is left in the ground where you once were."]
                    ending = "Weak"
        castle = Castle("Castle", [], castle_actions, castle_texts)
        current_room = castle
    return current_room, ending