# Kaikki pelin loppu tekstit
def endings(ending, endings_found):
    print(f"{ending} ending")
    print("")
    if ending == "Weak":
        print("You died. You failed. Call it whatever you want, the dragon is still terrorizing the village and everybody is starving. If there is even one tiny positive side to this,\nit would be that you will never be remembered as the weakest hero of all time.")
    elif ending == "Strong":
        print("You annihilated the dragon and saved everybody in the village. Now everybody is celebrating your victory with pineapple pizzas and mead.\nThe villagers also build a statue of you, that looks way more muscular than you actually are. You will forever be remembered as the strongest dragon obilerator.")
    elif ending == "Speedrun":
        print("You never took anything. You didn't wear any clothes. You didn't take a weapon. No armor. Not even a rock. You also never asked for help.\nYou knew all you needed was you body and nothing else. Everybody would be celebrating your victory but you were so fast that nobody saw you and they don't even know what happened. Everybody just continues their lifes normally thinking that the dragon left on its own.")
    elif ending == "Overencumbered":
        print("Did you seriously take every item you saw? Why would you do that? How were you gonna fight with your pockets full of useless trinkets?\nDid you not even think how much all of that weighs? You even took the rock, what were you gonna do with a rock? Maybe you should not take every item you see next time?")
    elif ending == "Lone survivor":
        print("Exausted and injured you look around the battlefield. The dragon is dead but you are not happy. After tending to your wounds and resting a bit,\nyou get up and start digging holes so you can bury your friends. You return to the village and everybody there is celebrating your victory but you walk past them and make your way home. You fall on your bed face first and cry yourself to sleep. The village is saved but the nightmares never stop. ")
    elif ending == "Unexpected alliance":
        print("The three of you go back to the village and celebrate with everybody. The next day you talk with your allies about future plans and all of you decide to form a party\nto slay more dragons. After many years your party becomes the most successful and well known dragon slayers of all time.")
    elif ending == "Sad":
        print("That's so sad. Please try harder next time, i can't keep watching this.")
    elif ending == "Revengeance":
        print("Long ago, a haunted castle stood deserted atop a hill. Every night, the people in the nearby village heard a voice screaming from the castle. On every blood moon,\neverybody in the village locks their doors and hide all night long, because if you don't your corpse will be found in pieces. The villagers offer a huge amount of money to anyone who would get rid of the entity from the castle. Brave adventurers from everywhere came to try, but each time, when the villagers came to see what had happened in the morning, they found the adventurer dead. The entity became known as 'Jack the Ripper'")
    elif ending == "Slicing and dicing":
        print("Everybody celebrates you victory with a big cauldron of dragon soup. You continue training you knife skills. Even though you can cut a dragon with one slash,\nyou know you haven't reached the pinnacle yet. Maybe someday you can cut a mountain in half or maybe even the sky.")
    elif ending == "Maybe you should not trust the first goblin you see?":
        print("The dragon hates everything you just said so it just burns you to ashes and destroys the nearby village and forest. Maybe try something else?")
    elif ending == "The Cost of winning":
        print("You won against the dragon, but at what cost. You bury your friend and return home. Every villager is happy that the dragons is gone thanks you,\nbut you just ignore them and continue your life. You never raise you lips to smile ever again.")
    elif ending == "Pacifist":
        print("You are happy, your friends are happy and the villagers are happy, everybody is happy. Well maybe not the dragon but it's doing okay.\nThe dragons is now living in the village, helping where it can earning its keep, rather than stealing.")
    elif ending == "Coward":
        print("You run, run and run, farther and farther, never stopping, but no matter how far you run, they always follow you, disturbing your sleep. The nightmares never stop.")
    elif ending == "Backstabbed":
        print("Wow i did not see that coming, did you?. Well better luck next time i guess.")
    elif ending == "BFF":
        print("Both of you become the saviors of the village. You continue to support each other every you go and accomplish many great feats.\nThere will be many trials in your future, but you know that together, you can do anything.")
    elif ending == "Betrayed":
        print("Maybe don't take fighting advice from a goblin next time?")
    if ending not in endings_found:
        endings_found.append(ending)