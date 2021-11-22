import random
import balance
import items

class unit():
    def __init__(self):
        self.STR = 1  # STRENGTH number of sides in bonus dices
        self.AG = 1  # AGILITY number of additional dices
        self.INT = 1  # INTELLIGENCE number of additional effects

        self.HP = 1  # health points
        self.max_HP = 1

        self.level = 1

        self.artifact = None  # only one object item can be assigned to a unit

        # full list of dices used to generate strategy
        self.dice_pool = []
        self.turn_pool = []
        self.effects_pool = []

        self.attack_speed = 1  # number of lists in strategy
        # lists of dices used for fighting
        self.strategy = [[]]
        self.magic = [[]]

    def item_change(self):
        self.dice_pool = [4, 5]
        self.effects_pool = []
        # adding item base pool of dices

        for dice in self.artifact.dice_pool:
            self.dice_pool.append(dice)

        self.turn_pool = self.dice_pool.copy()

        # adding item effect pool
        for spell in self.artifact.magic_pool:
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



    def efffect(self, dices, action):
        # we are making copy to avoid saving effect to an object
        for spell in self.magic[action]:
            spell.use(dices)


    # TODO CHANGE THIS ATTACK IT'S BAD
    def attack(self, dices):
        value = 0
        for i in range(len(dices)):
            value += random.randint(1, dices[i])
        return value


    # TODO REMOVE IT OR SOMETHING
    def printing_all_stats(self):
        print("STR: " + self.STR + " AG " + self.AG + " INT: " + self.INT)
        print("HP: " + self.HP + " MAX_HP: " + self.max_HP)
        print("Item base: " + self.dice_pool)
        print("Strategy: " + self.strategy)
        print("Magic: ")
        for spell_list in self.magic:
            for spell in spell_list:
                print(spell.short_print())
        print()


class monster(unit):
    def __init__(self, power):
        super().__init__()
        knight = [3, 2, 1]
        rouge = [2, 3, 1]
        mage = [1, 2, 3]
        roles = [knight, rouge, mage]
        role = roles[random.randint(0, len(roles))]
        self.STR = role[0]
        self.AG = role[1]
        self.INT = role[2]

        if power < 1:
            power = 1
            print("minus level for mercenary        ERROR")
        self.level = power

        self.artefact = items.item(power)
        self.item_change()


        # TODO THIS HP IS PPRETTY LOW MAYBE THATS WHY GAME IS SO EZZ
        self.max_HP = power
        self.HP = self.max_HP





def create_mercenary(power):
    mercenary = hero()
    knight = {3, 2, 1}
    rouge = {2, 3, 1}
    mage = {1, 2, 3}
    roles = {knight, rouge, mage}
    role = roles[random.randint(0, len(roles))]

    if power < 1:
        power = 1
        print("minus level for mercenary        ERROR")

    mercenary.level = power

    mercenary.STR = role[0]
    mercenary.AG = role[1]
    mercenary.INT = role[2]

    mercenary.artefact = items.item(power)
    mercenary.item_change()

    mercenary.max_HP = power
    mercenary.HP = mercenary.max_HP
    return mercenary


class hero(unit):
    def __init__(self):
        super().__init__()
        self.exp = 0
        self.gold = 10
        knight = [3, 2, 1]
        rouge = [2, 3, 1]
        mage = [1, 2, 3]
        roles = [knight, rouge, mage]
        role = roles[random.randint(0, len(roles))]
        self.STR = role[0]
        self.AG = role[1]
        self.INT = role[2]

        artefact = items.item(1)


        artefact.set_stats(self.STR, self.AG, self.INT)


        self.item_change()
        self.generate_strategy()

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
        self.exp += value * balance.weak
        while self.exp > (self.level * balance.levelup_speed):
            if (self.STR+self.AG+self.INT) == (balance.dices.length * 3):
                self.stat_changed()
                return None  # max level

            self.exp -= (self.level * balance.levelup_speed)
            self.level += 1

            levelups = []
            if self.STR < balance.dices.length:
                levelups.append(0)
            if self.AG < balance.dices.length:
                levelups.append(1)
            if self.INT < balance.dices.length:
                levelups.append(2)

            rand = levelups[random.randint(0, len(levelups))]
            if rand == 0:
                self.STR += 1
            elif rand == 1:
                self.AG += 1
            else:
                self.INT += 1

        self.stat_changed()

    def stat_changed(self):
        # adjusting HP
        new_max_HP = self.level * balance.strong
        hp_correct = new_max_HP - self.max_HP
        self.max_HP = new_max_HP
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
        pass
        '''
        # we add hero specific values
        System.out.println("STR: " + STR + " AG: " + AG + " INT: " + INT);
        System.out.println("HP: " + HP + " MAX_HP: " + max_HP);
        System.out.println("Item base: " + dice_pool);
        System.out.println("Strategy: " + strategy);
        System.out.print("MAGIC: ");
        for (ArrayList<effect> spell_list : magic)
        {
            output.print("[");
            for (effect spell : spell_list)
            {
                output.print(spell.short_print());
            }
            output.print("] ");
        }
        System.out.println();
        System.out.println("Gold: " + gold + " Level: " + level + " Exp: " + exp);
        '''


