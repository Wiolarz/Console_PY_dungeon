import random

import items
import balance


def generate_items(days):
    # generation of list of item objects to a shop
    shops_items = []
    power = (balance.max_power // 2) + days
    if power > balance.max_power:
        power = balance.max_power
    
    # lowest_item_level = 1
    
    for i in range(balance.shop_items_amount):
        # TODO over time there should be less weaker items generated
        thing = items.Item(random.randint(1, power))
        shops_items.append(thing)

    return shops_items
    

def generate_folders(all_items):
    # We split all items into x smaller groups
    amount_of_folders = 3  # rest of the code works only for 3 folders

    folders = []

    for i in range(amount_of_folders):
        folders.append([])

    for thing in all_items:
        if thing.level < balance.max_power // 4:  # weakest items
            folders[0].append(thing)

        elif thing.level < balance.max_power // 2.75:  # medium items
            folders[1].append(thing)

        else:  # best items
            folders[2].append(thing)
        
        return folders
    

def open_folder(player,  folder):
    # interface to buy items from a smaller folder of items
    # printing possible choices
    print("Welcome to shop 1 exit ")

    x = -1
    for thing in folder:
        x += 1
        info = []

        for dice in thing.base_pool:
            info.append(dice)
        
        info2 = []
        for spell in thing.magic_pool:
            info2.append(spell.short_print())
        
        # printing details about items
        print("%-16s", x + 2 + " level: " + roman_numbers(thing.level), end="")
        print("%-12s", ("price: " + thing.level * balance.medium), end="")
        print("%-34s", "STR_req: %d AG_req: %f INT_req: %e" % (thing.STR_req, thing.AG_req, thing.INT_req), end=" ")
        print("%-70s", ("base: " + info), end="")
        print("%-70s", ("Magic: " + info2), end="")
        print()

    choice = 0
    while choice != 9:
    
        choice = int(input())

        if choice == 1:
            return

        elif choice > 1 and folder[choice - 2].does_fit(player):
            if player.pay(folder[choice - 2].level * balance.medium):
                player.item_change(folder[choice - 2])


def shop(player, item_list):
    # general shop interface
    folders = generate_folders(item_list)

    choice = 0
    while choice != 9:

        # Info for player
        print("Welcome to shop 1 exit 2 medic's shop")

        for i in range(len(folders)):
            print("%d folder" % (i+3), end=" ")
        
        print()

        choice = int(input())  # Read user input

        if choice == 1:
            choice = 9  # exit
        elif choice == 2:
            medic(player)
        else:
            open_folder(player, folders[choice-3])


def medic(player):
    healing = [[1, 3], [2, 5], [3, 6], [5, 8]]

    print("Welcome to medic's shop 1 exit 2 auto-heal", end=" ")
    x = 3
    for item in healing:
        print("%d [heal: %f price: %e]" % (x, item[0], item[1]), end=" ")
        x += 1

    print()

    choice = int(input())  # User input

    if choice == 1:
        return  # exit medic shop
    elif choice == 2:  # auto-heal to max possible HP
        auto_heal(player, healing)
        return
    elif 2 < choice < 1 + len(healing):  # enter healing manually
        if player.pay(healing[choice - 3][1]):
            player.heal(healing[choice - 3][0])
            return
        else:
            print("Not enough money")
            return
    else: 
        print("Wrong choice")
        return
    

def auto_heal(player, healing):
    while player.gold >= healing[0][1] and player.HP < player.max_HP:
        for item in range(len(healing) - 1, 0, -1):
            while player.HP + healing[item][0] <= player.max_HP and player.pay(healing[item][1]):
                player.HP += healing[item][0]
    print("gold: %d HP: %f" % (player.gold, player.HP))


def roman_numbers(value):
    # Conversion of int into a roman number (works correctly to a max number of 39)
    result = ""
    while value > 10:
        result += "X"
        value -= 10
    rome = {
        0: "0",  # it's not correct but works
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X"}
    result += rome[value]
    return result
