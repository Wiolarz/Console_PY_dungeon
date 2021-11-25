import random

import jobs
import balance
from economy import roman_numbers

class earth:
    def __init__(self):
        self.days = 1

        self.main_quest = jobs.quest()

        self.locations = []
        self.generate_location()
        #

        # location_names
        self.location_number = 7  # max 8

    def new_quest(self):
        self.first_quest = jobs.quest()

    def generate_location(self):
        for place in range(self.location_number): #
            self.locations.append(location(place+1, self.location_number))  # location level, overall location number



class location():
    def __init__(self, location_level, amount):
        #id = location.identification += 1 # debug

        self.name = self.name_generator()

        self.level = location_level
        self.quest_level = location_level + 2
        if self.quest_level > balance.max_power:
            self.quest_level = balance.max_power

        self.chest_gold = location_level * balance.medium

        self.density = 5 # number of events in location
        self.chest_chance = 3 # %(10) chest chance
        self.quest_enemy = 5 # %(10) chance of quest related enemy

        self.location_names = []


        self.amount_location = amount

    def short_print(self):
        return self.name + " " + roman_numbers(self.level)
    

    def name_generator(self):
    
        prefix = ["", "Green", "Dark", "Toxic", "Inferno", "Orc", "Goblin", "Dragon"]
        core = ["Forest", "Cave", "Dungeon", "Town", "Village", "Mountains", "Graveyard"]
        #sufix = ["", ""]
        new_unique = False
        new_name = ""

        cheking_wrong_balance = 0
        while not new_unique:
            cheking_wrong_balance += 1
            if cheking_wrong_balance > self.amount_location * 5:
                print("Error: cannot create random new location name")
                exit(343)
            new_name = prefix[random.randint(0, len(prefix)-1)] + " " + core[random.randint(0, len(core)-1)]



            if new_name in self.location_names:
                new_unique = False
            else:
                new_unique = True


        self.location_names.append(new_name)
        return new_name
    
