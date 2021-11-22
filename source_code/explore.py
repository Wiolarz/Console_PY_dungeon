import random

import balance
import units

def walk(company, place):
    # takes
    killed = 0
    for i in range(balance.events):
        event = random.randint(0,  10)

        if event <= place.chest_chance:
            print("You found a chest")
            chest(company, place.chest_gold)
        else:
            print("You fight")
            if fight(company, generate_enemy(place.level)):
                killed += place.level
               
        if balance.world.main_quest.type.equals("boss") and balance.world.main_quest.target_place == place.id:
            print("You encounter boss, his level: " + place.quest_level)
            boss = []
            boss.append(units.monster(place.quest_level))
            if fight(company, boss):
            
                print("You won")
                print(" quest: ")
                balance.world.main_quest = quest(day)
                balance.world.main_quest.days_to_complete+= 1
            
        
        elif balance.world.main_quest.type.equals("units.monsters") and balance.world.main_quest.target_place == place.id:
            print("you have defeated " + killed + " units.monsters")
            balance.world.main_quest.units.monsters_to_kill -= killed
            if balance.world.main_quest.units.monsters_to_kill <= 0:
                print("You won")
                print(" quest: ")
                balance.world.main_quest = quest(day)
                balance.world.main_quest.days_to_complete += 1
            
        

    


# walking functions

def chest(company, quality):
    # event during exploring which rewards player
    company.get(0).gold += quality



def  generate_enemy(level):
    # event during exploring which challenges player
    enemy = []
    
    if level == 1:
        enemy.append(units.monster(1))
        return enemy
    
    elif level == 2:
        if random.randint(0, 1) == 1: #50% chance
            enemy.append(units.monster(2))
        
        else:
            enemy.append(units.monster(1))
            enemy.append(units.monster(1))
        
        return enemy
    

    x = random.randint(0, 3) # * number of cases
    
    if x == 0:
        # horde
        for i in range(level):
            enemy.append( units.monster(1))
        
    elif x == 1:
        # random
        split = random.randint(0,  level-2) + 2 # 2 -> level-1
        resource = level #
        for i in range(split):
            next_level = ((resource) / (split )) + 1 
            enemy.append( units.monster(next_level))
            resource -= next_level
        
        enemy.append(units.monster(resource))
        
    elif x == 2:
        # single boss
        enemy.append(units.monster(level))

    return enemy




# fight functions

def attack(dice_pool):
    score = units.attack(dice_pool)

    # counting number of successes
    success = 0
    difficulty = 6

    while difficulty < score:
        score -= difficulty
        difficulty = (difficulty * 1.5)
        success+= 1

    return success


def graveyard(fighters):
    for fighter in range(fighters.size() - 1, 0, -1):
        if fighters.get(fighter).HP <= 0:
            fighters.remove(fighter)

    return len(fighters) == 0


def turn_attacks(attacker, defender):
    # before attack we remove effects from defender
    for fighter in defender:
        fighter.turn_pool = fighter.dice_pool

    # before player attacks we apply effects from players attack to their attacks
    for fighter in attacker:
        fighter.generate_strategy()

    for fighter in attacker:
        for action in range(fighter.attack_speed):
            # here could be a choice to perform different action instead
            target = random.randint(0, len(defender)-1)

            success = attack(fighter.strategy.get(action))

            for i in range(success):
                defender[target].HP -= 1

            if success > 0:
                fighter.effect(defender[target].turn_pool, action)

############# TUUUUUUUUUUUU


def fight(company, enemy):

    # measure the challenge level
    challenge = 0
    for fighter in enemy:
        challenge += fighter.level


    #enemy.get(0).printing_all_stats()

    # fighting

    for rounds in range(50):
        choice = int(input())

        if choice == 1: # escape attempt
            # basic roll for each fighter, if player side succeeds
            #if success return false
            return False

        elif choice == 2:
            # player attacks
            # random targets for now
            turn_attacks_hero(company, enemy)

            # checking dead enemy
            if graveyard(enemy):
                print("You have won this fight")
                company.get(0).experience(challenge)
                return True

        turn_attacks_units.monster(enemy, company)

        # checking dead in company
        if graveyard(company):
            print("Your company has been defeated GAME OVER")
            System.exit(666)



    return False # a draw



def walking(company,  world,day)

   choice

    while (true)
    
        output.print("1 Exit  ")
       x = 2
        for (location place : world)
        
            output.print(x + " " + place.short_print() + "  ")
            x+= 1
        
        print("")

        choice = int(input())  # User input

        if (choice == 1) return false # exit world map
        elif (choice > 1) # enter location
        
            walk(company, world.get(choice - 2), day)
            return true
        
    




def  generate_world()

     world =  ()
    for (place = 1 place < balance.location_number+1 place+= 1)
    
        world.append( location(place)) # location level
    
    return world
    