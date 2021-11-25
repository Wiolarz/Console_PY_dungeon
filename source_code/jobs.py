import random

import balance


from economy import roman_numbers


class quest:
    def __init__(self):
        self.days_to_complete = 0
        self.target_place = 0

        self.quest_gold = 0
        self.monsters_to_kill = 0

        self.type = ""

        self.story = ""
        self.fail_story = ""

        self.random_quest()

    def print_info(self):
        print("You have: " + self.days_to_complete + " days to " + self.story)
        if(self.type == "boss"):
            print("Enemy boss awaits at " + roman_numbers(self.target_place + 1) + " location")
        elif(self.type == "gold"):
            print("You need to gather " + self.quest_gold)
        elif (self.type == "monsters"):
            print("Enemy monsters awaits at " + roman_numbers(self.target_place + 1) + " location " +
                self.monsters_to_kill + " are still alive")
        else:
            print("quest print_info() -> wrong type")


    def location_and_time(self, current_day):
        # days to complete quest
        base = balance.weak
        difficulty =\
        [[base * balance.week, balance.powerful, 3],
        [base * balance.medium, balance.strong, 2],
        [base * balance.strong, balance.medium, 1],
        [base * balance.powerful, balance.week, 1]]


        for level in difficulty:
            if (current_day < level[0]):
                location = random.randint(0, (balance.world.location_number / level[2]))

                time = level[1]
                return location, time, level[0]

        time = 1
        location = balance.world.location_number-1 # last spot

        return location, time, base * balance.powerful


    def random_quest(self):
        loc_time = self.location_and_time(balance.world.current_day)
        self.days_to_complete = loc_time[1]

        rng = random.randint(0, 2)

        if rng == 0:  # boss to kill
            type = "boss"
            target_place = loc_time[0]

            story = "kill a warlock in dungeon, he is currently preparing to summon a demo"
            fail_story = "Time has run out, and warlock has managed to summon a demon, the world is doomed"
        elif rng == 1: # gold to pay

            story = "pay poor villagers taxes. Gather gold in order to help them!"
            fail_story = "Time has run out, and village was burned to the ground by our glorious king"

            type = "gold"
            quest_gold = balance.weak * balance.world.current_day
        elif rng == 2: # monsters to kill

            story = " eradicate pesky monsters who are annoying our merchants,"
            fail_story = "Time has run out, and merchants have traveled to a different village"

            type = "monsters"
            target_place = loc_time[0]
            monsters_to_kill = loc_time[2]
        else:
            print("quest random_quest() -> switch_random")


    def check_quest(self, player):
        if self.type == "boss" or self.type == "monsters":  # those are checked in locations
            return
        elif self.type == "gold":
            if (player.pay(self.quest_gold)):

                print("You have helped poor villagers")
                balance.world.main_quest = quest()
        else:
            print("quest check_quest() -> wrong type")



        # story text generator



        # TODO finish quest generator
        # types of quests, enemy to kill, location, maybe reward system, maybe optional quests etc











