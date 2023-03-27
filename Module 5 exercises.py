# What is the difference between a tuple and a list?
#  Both are seuqences, but lists are able to be modified
# How is a list different than a dictionary?
#  A list is made of index value pairs while a dictionary is made of pairs of keys and values.
# Create a program that prints a list of words in random order. The program should print all the words and not repeat any.

import random

words = ["apples", "bananas", "lemons", "limes", "mangoes"]

print (words)

print("\n Shuffle, shuffle, shuffle\n")
random.shuffle(words)

print(words)


# Write a Character Creator program for a role-playing game. The player should be given a pool of 30 points to spend on four attributes: Strength, Health, Wisdom, and Dexterity. The player should be able to spend points from the pool on any attribute and should also be able to take points from an attribute and put them back into the pool.

stats = {"STRENGTH": 0,
        "HEALTH": 0,
        "WISDOM": 0,
        "DEXTERITY": 0}

print("\n\nIn the kingdom of Azarelia lived a peaceful people, that is, until the Katosmos Empire attacked. It's been 1000 years since that day, but the prophecy of a hero has been foretold. You are that hero, destined to defeat Emperor Bercerus. Will you do it with overhwleming Power, divine Knowledge, or incredible Technique. The stats you assign now will dictate your ending")

MAX_POINTS = 30

pointsUsed = 0



while True:  

    pointsAvailable = (30 - pointsUsed)

    print ("\n\nThese are your current stats:\n")
    print(stats)
    print ("Points left: ", pointsAvailable)
    choice = int(input(""" \nPress the appropiate keys
    0: Allocate Points
    
    1: Remove Points
    
    2: Confirm point allocation\n
    """
          ))
    if choice == 0:
        att = input("\nWhich attribute do you want to allocate points to: ")
        att = att.upper()
        if att in stats:
            upgrade = int(input('\nHow many points do you want to allocate to this att.? '))
            if upgrade < 0 or upgrade > 30 - pointsUsed:
                print("\nYou cannot allocate that amount of points.")
            else:
                pointsUsed += upgrade
                stats[att] += upgrade
        else:
            print('\nThat is not an upgradeable attribute Hero!')
    elif choice == 1:
        att = input("\nWhich attribute do you want to remove points from: ")
        att = att.upper()
        if att in stats:
            downgrade = int(input('\nHow many points do you want to remove from this att.? '))
            if downgrade < 0 or downgrade > stats[att]:
                print("\nYou cannot remove that amount of points.")
            else:
                stats[att] -= downgrade
                pointsUsed -= downgrade
    elif choice == 2:
        print("\nMay your legend be succesful young Hero! Your adventure starts now. Goodbye")
        break
    else:
        print("\nPlease enter an appropiate number.")



# Write a Who’s Your Daddy? program that lets the user enter the name of a male and produces the name of his father. (You can use celebrities, fictional characters, or even historical figures for fun.) Allow the user to add, replace, and delete son-father pairs.

families = [("Homer", "Bart"),
            ("Vader", "Luke"),
            ("Vito", "Mike"),
            ("Mufasa", "Simba"),
            ("Marlin", "Nemo")]

while True:

    print(
    """
    Who's Your Daddy?
    
    0: Quit
    
    1: Show all pairs
    
    2: Add a pair
    
    3: Replace a pair

    4: Delete a pair

    """
    )
    
    choice = input("Choice: ")
    print()
    if choice == "0":
        print("\nGood-bye.")
        break

    elif choice == "1":
        print("Pairs:\n")
        print("SON\t\tDAD")
        for pair in families:
            dad, son = pair    
            print(son, "\t\t", dad)

    elif choice == "2":
        son = input("\nWhat is the son's name?: ")
        dad = input("\nWhat is the dad's name?: ")
        pair = (dad, son)
        families.append(pair)
        print("\nPair has been added")

    elif choice == "3":
        position = int(input("\nWhat pair do you want to remove from the list? (refer to their number position)\nPosition: "))
        son = input("\nWhat is the replacement son's name?: ")
        dad = input("\nWhat is the replacement dad's name?: ")
        pair = (dad, son)
        del families[position]
        families.insert(position, pair)
        print("\nPair has been replaced")

    elif choice == "4":
        position = int(input("What pair do you want to remove from the list? (refer to their number position)\nPosition: "))
        del families[position]
        print("\nPair has been removed")

    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

