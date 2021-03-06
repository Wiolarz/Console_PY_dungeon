import random
import balance
import items


class Unit:
    def __init__(self):
        self.STR = 1  # STRENGTH number of sides in bonus dices
        self.AG = 1  # AGILITY number of additional dices
        self.INT = 1  # INTELLIGENCE number of additional effects

        self.HP = 1  # health points
        self.max_HP = 1

        self.level = 1

        self.artefact = None  # only one object item can be assigned to a unit

        # full list of dices used to generate strategy
        self.dice_pool = []
        self.turn_pool = []
        self.effects_pool = []

        self.attack_speed = 1  # number of lists in strategy
        # lists of dices used for fighting
        self.strategy = [[]]
        self.magic = [[]]

    def item_change(self):
        self.dice_pool = []
        self.effects_pool = []
        # adding item base pool of dices

        for dice in self.artefact.base_pool:
            self.dice_pool.append(dice)

        self.turn_pool = self.dice_pool.copy()

        # adding item effect pool
        for spell in self.artefact.magic_pool:
            self.effects_pool.append(spell)

        self.generate_strategy()  # adding new dices to the strategy

    def generate_strategy(self):
        # adjusting attack speed
        self.strategy = []
        self.magic = []
        for action in range(self.attack_speed):
            self.strategy.append([])
            self.magic.append([])

        # place where strategy is generated
        counter = 0
        for i in range(len(self.turn_pool)):
            self.strategy[counter].append(self.turn_pool[i])
            counter += 1
            if counter == self.attack_speed:
                counter = 0

        counter = 0
        for i in range(len(self.effects_pool)):
            self.magic[counter].append(self.effects_pool[i])
            counter += 1
            if counter == self.attack_speed:
                counter = 0

    def effect(self, dices, action):
        for spell in self.magic[action]:
            spell.use(dices)

    def printing_all_stats(self):
        print("STR: %d  AG: %d  INT: %d" % (self.STR, self.AG, self.INT))
        print("HP: %d MAX_HP: %d" % (self.HP, self.max_HP))
        print("Item base:", end=" ")
        print(self.dice_pool)
        print("Strategy:", end=" ")
        print(self.strategy)
        print("Magic:", end=" ")
        for spell_list in self.magic:  # TODO i think it can be contained in a single line
            print("[", end="")
            if(len(spell_list) > 0):
                for spell in spell_list[:-1]:
                    print(spell.short_print(), end=" | ")
                print(spell_list[-1].short_print(), end="")
            print("]", end=" ")
        print()


class Monster(Unit):
    def __init__(self, power):
        super().__init__()
        knight = [3, 2, 1]
        rouge = [2, 3, 1]
        mage = [1, 2, 3]
        roles = [knight, rouge, mage]
        role = roles[random.randint(0, len(roles)-1)]
        self.STR = role[0]
        self.AG = role[1]
        self.INT = role[2]

        if power < 1:
            power = 1
            print("minus level for mercenary        ERROR")
        self.level = power

        self.artefact = items.Item(power)
        self.item_change()

        # TODO this hp is really has low value maybe that's why game is so easy
        self.max_HP = (power * 2)
        self.HP = self.max_HP


def create_mercenary(power):
    mercenary = Hero()
    knight = [3, 2, 1]
    rouge = [2, 3, 1]
    mage = [1, 2, 3]
    roles = [knight, rouge, mage]
    role = roles[random.randint(1, len(roles))-1]

    if power < 1:
        power = 1
        print("minus level for mercenary        ERROR")

    mercenary.level = power

    mercenary.STR = role[0]
    mercenary.AG = role[1]
    mercenary.INT = role[2]

    mercenary.artefact = items.Item(power)
    mercenary.item_change()

    mercenary.max_HP = power
    mercenary.HP = mercenary.max_HP
    return mercenary


class Hero(Unit):
    def __init__(self):
        super().__init__()
        self.__exp = 0
        self.gold = 10
        knight = [3, 2, 1]
        rouge = [2, 3, 1]
        mage = [1, 2, 3]
        roles = [knight, rouge, mage]
        role = roles[random.randint(0, len(roles) - 1)]
        self.STR = role[0]
        self.AG = role[1]
        self.INT = role[2]

        self.artefact = items.Item(1)

        self.artefact.set_stats(self.STR, self.AG, self.INT)

        self.item_change()

        self.max_HP = self.level * balance.strong
        self.HP = self.max_HP

    def pay(self, price):
        # used in shop,if player has enough money to pay the price it returns true
        if price <= self.gold:
            self.gold -= price
            return True
        else:
            print("not enough money " + (price - self.gold) + " needed")
            return False

    def experience(self, value):
        self.__exp += value * balance.weak
        while self.__exp > (self.level * balance.levelup_speed):
            if (self.STR+self.AG+self.INT) == (len(balance.dices) * 3):
                self.stat_changed()
                return None  # max level

            self.__exp -= (self.level * balance.levelup_speed)
            self.level += 1

            levelups = []
            if self.STR < len(balance.dices):
                levelups.append(0)
            if self.AG < len(balance.dices):
                levelups.append(1)
            if self.INT < len(balance.dices):
                levelups.append(2)

            rand = levelups[random.randint(0, len(levelups) - 1)]
            if rand == 0:
                self.STR += 1
            elif rand == 1:
                self.AG += 1
            else:
                self.INT += 1

        self.stat_changed()

    def stat_changed(self):
        # adjusting HP
        new_max_hp = self.level * balance.strong
        hp_correct = new_max_hp - self.max_HP
        self.max_HP = new_max_hp
        self.HP += hp_correct

    def heal(self, value):
        self.HP += value
        if self.HP > self.max_HP:
            self.HP = self.max_HP

    def cheats(self):
        self.STR = 6
        self.AG = 6
        self.INT = 6
        self.max_HP = 420
        self.HP = self.max_HP
        self.gold += 1000

    def printing_all_stats(self):
        super().printing_all_stats()
        # we add hero specific values
        print("Gold: %d Level: %d Exp: %d" % (self.gold, self.level, self.__exp))



# TODO CHANGE THIS ATTACK IT'S BAD
def attack(dices):
    value = 0
    for i in range(len(dices)):
        value += random.randint(1, dices[i])
    return value
