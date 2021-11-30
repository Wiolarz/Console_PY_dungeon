import random

import balance


from economy import roman_numbers


class Quest:
    def __init__(self):
        self.days_to_complete = 0
        self.target_place = 0

        self.quest_gold = 0
        self.monsters_to_kill = 0

        self.style = ""

        self.story = ""
        self.fail_story = ""

        self.random_quest()

    def print_info(self):
        print(("You have: %d days to " + self.story) % self.days_to_complete)
        if self.style == "boss":
            print("Enemy boss awaits at " + roman_numbers(self.target_place + 1) + " location")
        elif self.style == "gold":
            print("You need to gather %d" % self.quest_gold + " gold")
        elif self.style == "monsters":
            print("Enemy monsters awaits at " + roman_numbers(self.target_place + 1) +
                  " location %d are still alive" % self.monsters_to_kill)
        else:
            print("quest print_info() -> wrong style")

    def location_and_time(self, current_day):
        # days to complete quest
        base = balance.weak
        difficulty = [
            [base * balance.week, balance.powerful, 3],
            [base * balance.medium, balance.strong, 2],
            [base * balance.strong, balance.medium, 1],
            [base * balance.powerful, balance.week, 1]]

        for level in difficulty:
            if current_day < level[0]:
                location = random.randint(0, int(balance.world.amount_location // level[2]))

                self.days_to_complete = level[1]
                return location, level[0]

        location = balance.world.amount_location - 1  # last spot
        self.days_to_complete = 1
        return location, base * balance.powerful

    def random_quest(self):
        loc_time = self.location_and_time(balance.world.current_day)

        rng = random.randint(0, 2)

        if rng == 0:  # boss to kill
            self.style = "boss"
            self.target_place = loc_time[0]

            self.story = "kill a warlock in dungeon, he is currently preparing to summon a demo"
            self.fail_story = "Time has run out, and warlock has managed to summon a demon, the world is doomed"

        elif rng == 1:  # gold to pay
            self.story = "pay poor villagers taxes. Gather gold in order to help them!"
            self.fail_story = "Time has run out, and village was burned to the ground by our glorious king"

            self.style = "gold"
            self.quest_gold = balance.weak * balance.world.current_day

        elif rng == 2:  # monsters to kill
            self.story = " eradicate pesky monsters who are annoying our merchants,"
            self.fail_story = "Time has run out, and merchants have traveled to a different village"

            self.style = "monsters"
            self.target_place = loc_time[0]
            self.monsters_to_kill = loc_time[1]

        else:
            print("quest random_quest() -> switch_random")

    def check_quest(self, player):
        if self.style == "boss" or self.style == "monsters":  # those are checked in locations
            return
        elif self.style == "gold":
            if player.pay(self.quest_gold):

                print("You have helped poor villagers")
                balance.world.main_quest = Quest()
        else:
            print("quest check_quest() -> wrong style")

        # TODO story text generator
        # styles of quests, enemy to kill, location, maybe reward system, maybe optional quests etc
