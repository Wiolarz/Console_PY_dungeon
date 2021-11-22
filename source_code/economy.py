import random

import items
import balance

def generate_items(days):
    # generation of list of item objects to a shop
    shops_items = []
    power = (balance.max_power/2) + days
    if power > balance.max_power:
        power = balance.max_power
    
    lowest_item_level = 1
    
    for i in range(balance.shop_items_amount):
        #TODO over time there should be less weaker items generated
        thing = items.item(random.randint(1, power))
        shops_items.append(thing)
    
    
    return shops_items
    


def generate_folders(all_items):
    # We split all items into x smaller groups
    amount_of_folders = 3 # rest of the code works only for 3 folders

    folders = []

    for i in range(amount_of_folders):
        folders.append([])

        for thing in all_items:
            if thing.level < balance.max_power/4:  # weakest items
                folders[0].append(thing)
            
            elif thing.level < balance.max_power/2.75: # medium items
                folders[1].append(thing)
            
            else: # best items
                folders[2].append(thing)
        
        return folders
    



def open_folder(player,  folder):
    # interface to buy items from a smaller folder of items
    #printing possible choices
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
        print("%-16s", x + 2 + " level: " + roman_numbers(thing.level))
        print("%-12s", ("price: " + thing.level * balance.medium))
        print("%-34s",
                          ("STR_req: " + thing.STR_req + " AG_req: " + thing.AG_req + " INT_req: " + thing.INT_req))
        print("%-70s", ("base: " + info))
        print("%-70s", ("Magic: " + info2))
        print()
    


    #println(inputs_shop(folder)) # it is so not working correctly, and first print replaces it ^



    choice = 0
    while choice != 9:
    
        choice = int(input())

        if choice == 1:
            return

        elif choice > 1 and folder.get(choice - 2).Does_Fit(player):
            if player.pay(folder.get(choice - 2).level * balance.medium):
                player.item_change(folder.get(choice - 2))
            
        
    




def inputs_shop(shop_list):
    # code not used, most likely to be deleted
    options = []
    if shop_list.size() < 7: # code would still work, it's just a design choice
        x = 1 # we appended folders
        for thing in shop_list:
            x += 1
            #options.append(x +"  Item - " + roman_numbers(thing.level))
    else:
    
        print("folders_generator failed")
    
    return options




def shop(player,  item_list):
    # general shop interface
    folders = generate_folders(item_list)

    choice = 0
    while choice != 9:

        # Info for player
        print("Welcome to shop 1 exit 2 medic's shop")

        for i in len(folders):
            print(i+3 + " folder", end=" ")
        
        print()


        choice = int(input())  # Read user input


        if choice == 1:
            choice = 9 # exit
        elif choice == 2:
            medic(player) #
        else:
            open_folder(player, folders[choice-3])
        
    


def medic(player):
    healing = [[1, 3], [2, 5], [3, 6], [5, 8]]

    print("Welcome to medic's shop 1 exit 2 auto-heal", end= " ")
    x = 3
    for item in healing:
        print(x++ + " [heal: " + item[0] + " price: " + item[1] + "]", end=" ")

    print()

    choice = int(input())  # User input

    if choice == 1:
        return # exit medic shop
    elif choice == 2:  # auto-heal to max possible HP
        autoHeal(player, healing)
        return
    
    elif choice > 2 and choice < 1 + len(healing): #enter healing manually
    
        if player.pay(healing[choice - 3][1]):
            player.heal(healing[choice - 3][0])
            return
        else:
            print("Not enough money")
            return
        
    
    else: 
        print("Wrong choice")
        return
    



def autoHeal(player,  healing):
    while player.gold >= healing[0][1] and player.HP < player.max_HP:
        for item in range(len(healing) - 1, 0, -1):
            while player.HP + healing[item][0] <= player.max_HP and player.pay(healing[item][1]):
                player.HP += healing[item][0]
    print("gold: " + player.gold + " HP: " + player.HP)


def roman_numbers(value):
# Conversion of int into a roman number (works correctly to a max number of 39)
        result = ""
        while value > 10:
            result += "X"
            value-=10
        rome = {
            0 : "0", # it's not correct but works
            1 : "I",
            2 : "II",
            3 : "III",
            4 : "IV",
            5 : "V",
            6 : "VI",
            7 : "VII",
            8 : "VIII",
            9 : "IX",
            10 : "X"
            #default : "?"
        }

        result += rome[value]
        return result


