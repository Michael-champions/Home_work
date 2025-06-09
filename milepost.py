# Text Adventure Game - by [Your Name]
# Creative Additions: Includes a secret option ("SWIM") not shown in the prompt. Also added 3+ choices in some scenarios.

print("You wake up on a mysterious island. In front of you are three paths: one leads to a CAVE, another to a BEACH, and the third into the JUNGLE.")
choice1 = input("Do you choose the CAVE, BEACH, or JUNGLE? ").strip().lower()

if choice1 == "cave":
    print("\nYou step into the dark cave and hear bats fluttering. You spot a SHINY object and a STRANGE hole in the wall.")
    choice2 = input("Do you investigate the SHINY object or crawl into the STRANGE hole? ").strip().lower()

    if choice2 == "shiny":
        print("\nIt's a jeweled dagger! But the sound of growling grows closer.")
        choice3 = input("Do you FIGHT with the dagger or ESCAPE back to the entrance? ").strip().lower()
        if choice3 == "fight":
            print("\nYou bravely fight the beast and win! You are a legend.")
        elif choice3 == "escape":
            print("\nYou escape safely, but empty-handed.")
        else:
            print("\nYou freeze in fear. The beast catches you. Game over.")

    elif choice2 == "strange":
        print("\nThe tunnel leads to an underground lake. It's glowing blue.")
        choice3 = input("Do you DRINK the water, REST by the shore, or EXPLORE the lake edge? ").strip().lower()
        if choice3 == "drink":
            print("\nThe water grants you strange powers. You gain night vision!")
        elif choice3 == "rest":
            print("\nYou fall asleep and wake up back on the beach — it was all a dream!")
        elif choice3 == "explore":
            print("\nYou find ancient markings — a clue to hidden treasure!")
        else:
            print("\nConfused, you slip into the water and disappear.")

    else:
        print("\nYou hesitate too long. The cave collapses behind you. Game over.")

elif choice1 == "beach":
    print("\nYou walk along the beach and find a BOAT, a MESSAGE in a bottle, and something moving in the WATER.")
    choice2 = input("Do you take the BOAT, read the MESSAGE, or check the WATER? ").strip().lower()

    if choice2 == "boat":
        print("\nThe boat has a small engine. It might work.")
        choice3 = input("Do you SAIL away or SEARCH for supplies first? ").strip().lower()
        if choice3 == "sail":
            print("\nYou escape the island safely. You're free!")
        elif choice3 == "search":
            print("\nYou find extra fuel and treasure, then leave richer than ever!")
        else:
            print("\nWhile hesitating, the tide drags the boat away. You're stuck.")

    elif choice2 == "message":
        print("\nThe message has coordinates and the word 'DANGER'.")
        choice3 = input("Do you FOLLOW the coordinates, BURY the message, or IGNORE it? ").strip().lower()
        if choice3 == "follow":
            print("\nYou find a secret bunker with food and radio — you're saved!")
        elif choice3 == "bury":
            print("\nYou hide the truth, and the mystery remains unsolved.")
        elif choice3 == "ignore":
            print("\nYou wander aimlessly and eventually build a home on the island.")
        else:
            print("\nYou tear the paper and throw it in the sea. It's lost forever.")

    elif choice2 == "water" or choice2 == "swim":  # hidden "swim" path
        print("\nA dolphin pops up and leads you to a coral cave!")
        choice3 = input("Do you FOLLOW it, STAY on shore, or DIVE deep? ").strip().lower()
        if choice3 == "follow":
            print("\nThe dolphin guides you to a hidden paradise!")
        elif choice3 == "stay":
            print("\nYou watch the waves, feeling peaceful.")
        elif choice3 == "dive":
            print("\nYou discover sunken ruins with golden statues.")
        else:
            print("\nThe tide pulls you out. You wake up hours later on shore.")

    else:
        print("\nA wave crashes over you. You black out. Game over.")

elif choice1 == "jungle":
    print("\nThe jungle is thick and buzzing with life. You find a MAP, a BACKPACK, and a path to a TREEHOUSE.")
    choice2 = input("Do you pick the MAP, take the BACKPACK, or climb to the TREEHOUSE? ").strip().lower()

    if choice2 == "map":
        print("\nThe map shows a path to treasure — but through dangerous territory.")
        choice3 = input("Do you RISK it, or look for a SAFE route? ").strip().lower()
        if choice3 == "risk":
            print("\nYou face wild animals but find the treasure!")
        elif choice3 == "safe":
            print("\nYou reach a village. They welcome you and share their stories.")
        else:
            print("\nYou wander off the path and get lost.")

    elif choice2 == "backpack":
        print("\nThe backpack contains food, tools, and a flare gun.")
        choice3 = input("Do you USE the flare, SAVE the supplies, or SHARE with others? ").strip().lower()
        if choice3 == "use":
            print("\nA rescue helicopter sees your flare — you're saved!")
        elif choice3 == "save":
            print("\nYou survive many days, building shelter and fire.")
        elif choice3 == "share":
            print("\nYou find other survivors, and together, you thrive.")
        else:
            print("\nAnimals smell the food and steal your backpack!")

    elif choice2 == "treehouse":
        print("\nYou climb the treehouse and spot a distant smoke signal.")
        choice3 = input("Do you SIGNAL back, CLIMB higher, or REST? ").strip().lower()
        if choice3 == "signal":
            print("\nThe sender responds — it's a lost explorer!")
        elif choice3 == "climb":
            print("\nYou get a better view — and a glimpse of civilization.")
        elif choice3 == "rest":
            print("\nYou nap in safety and dream of rescue.")
        else:
            print("\nYou slip and fall. Game over.")

    else:
        print("\nA snake slithers nearby. You run away in panic. Game over.")

else:
    print("\nThat's not a valid option. The island remains a mystery...")

