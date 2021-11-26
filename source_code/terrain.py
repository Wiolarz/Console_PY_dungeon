import random

import jobs
import balance
from economy import roman_numbers


class Earth:
    def __init__(self):
        self.current_day = 1
        self.main_quest = None
        self.amount_location = 7  # max 8
        self.locations = []
        #

        self.location_names = []

    def new_quest(self):
        self.main_quest = jobs.Quest()

    def generate_location(self):
        x = 0
        for place in range(self.amount_location):
            self.locations.append(Location(place + 1, self.amount_location, x))  # location level, overall location number
            x += 1


class Location:
    def __init__(self, location_level, amount, id_x):
        self.id = id_x

        self.name = self.name_generator()

        self.level = location_level
        self.quest_level = location_level + 2
        if self.quest_level > balance.max_power:
            self.quest_level = balance.max_power

        self.chest_gold = location_level * balance.medium

        self.density = 5  # number of events in location
        self.chest_chance = 3  # %(10) chest chance
        self.quest_enemy = 5  # %(10) chance of quest related enemy

        self.location_names = []

        self.amount_location = amount

    def short_print(self):
        return self.name + " " + roman_numbers(self.level)

    def name_generator(self):
    
        prefix = ["", "Green", "Dark", "Toxic", "Inferno", "Orc", "Goblin", "Dragon"]
        core = ["Forest", "Cave", "Dungeon", "Town", "Village", "Mountains", "Graveyard"]
        # suffix = ["", ""]
        new_unique = False
        new_name = ""

        cheking_wrong_balance = 0
        while not new_unique:
            cheking_wrong_balance += 1
            if cheking_wrong_balance > balance.world.amount_location * 5:
                print("Error: cannot create random new location name")
                exit(343)
            new_name = prefix[random.randint(0, len(prefix)-1)] + " " + core[random.randint(0, len(core)-1)]

            if new_name in balance.world.location_names:
                new_unique = False
            else:
                new_unique = True

        balance.world.location_names.append(new_name)
        return new_name
    
