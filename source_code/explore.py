import random

import battle
import balance
import units
import jobs
from source_code import manager


def walk(heroes, place):
    world = balance.world
    killed = 0
    for i in range(balance.events):
        event = random.randint(0, 10)

        if event <= place.chest_chance:
            print("You found a chest")
            chest(heroes, place.chest_gold)
        else:
            print("You fight")
            if battle.fight(heroes, generate_enemy(place.level)):
                loot(heroes, place)
                killed += place.level

    if world.main_quest.style == "boss" and world.main_quest.target_place == place.id:
        print("You encounter boss, his level: %d" % place.quest_level)
        boss = [units.Monster(place.quest_level)]
        if battle.fight(heroes, boss):
            print("You won")
            print(" quest: ")
            world.main_quest = jobs.Quest()
            world.main_quest.days_to_complete += 1

    elif world.main_quest.style == "monsters" and \
            world.main_quest.target_place == place.id:
        print("you have defeated %d pesky monsters" % killed)
        world.main_quest.monsters_to_kill -= killed

        if world.main_quest.monsters_to_kill <= 0:
            print("You won")
            print("New quest: ")
            world.main_quest = jobs.Quest()
            world.main_quest.days_to_complete += 1


# walking functions

def chest(heroes, quality):
    # event during exploring which rewards player
    heroes[0].gold += quality


def book(heroes, quality):
    # event during exploring which rewards player
    heroes[0].experience(quality)


def loot(heroes, place):
    # create random exploration event rewarding the player
    if random.randint(0, 1) == 1:
        print("You looted a chest")
        chest(heroes, place.chest_gold)
    else:
        print("You looted a book")
        book(heroes, place.chest_gold)


def generate_enemy(level):
    # event during exploring which challenges player
    enemy = []

    if level == 1:
        enemy.append(units.Monster(1))
        return enemy

    elif level == 2:
        if random.randint(0, 1) == 1:  # 50% chance
            enemy.append(units.Monster(2))

        else:
            enemy.append(units.Monster(1))
            enemy.append(units.Monster(1))

        return enemy

    x = random.randint(0, 3)  # * number of cases

    if x == 0:
        # horde
        for i in range(level):
            enemy.append(units.Monster(1))

    elif x == 1:
        # random
        split = random.randint(0, (level - 2)) + 2  # 2 -> level-1
        resource = level
        for i in range(split):
            next_level = (resource // split) + 1
            enemy.append(units.Monster(next_level))
            resource -= next_level

        enemy.append(units.Monster(resource))

    elif x == 2:
        # single boss
        enemy.append(units.Monster(level))

    return enemy


def walking(heroes, world):
    print("1 Exit", end="  ")
    x = 2
    for place in world.locations:
        print(x, end="  ")
        print(place.short_print(), end=" ")
        x += 1

    print()
    choice = manager.choice()  # User input

    if choice > 1:  # enter location
        walk(heroes, world.locations[choice - 2])
        return True

    return False  # exit world map
