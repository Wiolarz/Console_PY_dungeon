import random
import balance
import arcane

class item():
    def __init__(self, power):
        

        self.STR_req = 0
        self.AG_req = 0
        self.INT_req = 0

        '''creating type of item
        there are 3 values each containing a stat example: STR AG 
        is an item that balances every stat
        STR STR STR is a powerful strength item, while AG AG  is a mix
        '''

        if power > balance.max_power:
            power = balance.max_power
        self.level = power

        type = [0, 0, 0]  # used to create types of items



        for i in range(3):
            type[i] = random.randint(0, 2)
        

        counter = 0
        for i in range(power):
            if type[counter] == 0 and self.STR_req != len(balance.dices):
                self.STR_req += 1
            elif type[counter] == 1 and  self.AG_req != len(balance.dices):
                self.AG_req += 1
            elif type[counter] == 2 and  self.INT_req != len(balance.dices):
                self.INT_req += 1

            counter += 1
            if counter == 3:
                counter = 0



        '''
        STR big dices
        AG many dices
         smaller enemy dices
        placeholder but maybe fine generator for basic quality items:
        each po is a die, with a chance of spawning related thing:
        STR making this die a larger one
        AG spawn appenditional die
         spawn effect
        '''

        # base pool of dices
        self.base_pool = []
        self.magic_pool = []

        # we are appending randomly sized dices to the pool in a number equal to "power" of the item
        scope = len(balance.dices)
        weak_dices =   (scope // 4)
        normal_dices = (scope // 2)
        # strong_dices =

        for i in range(self.STR_req):
            self.base_pool.append(balance.dices[random.randint(0,  (scope - 3)) + 3]) # magic number no sadge
        

        for i in range(self.AG_req):
            self.base_pool.append(balance.dices[random.randint(0,  weak_dices)])
            self.base_pool.append(balance.dices[random.randint(0,  normal_dices)])
        

        for i in range(self.INT_req):
        
            self.base_pool.append(balance.dices[random.randint(0,  weak_dices)])
            x = random.randint(0, 2)
            
            if x == 0:
                self.magic_pool.append(arcane.effect(1, "edge", 2))
            if x == 1:
                self.magic_pool.append(arcane.effect(2, "edge", 1))
            if x == 2:
                self.magic_pool.append(arcane.effect(1, "random", 3))
        
    


    def set_stats(self, STR,  AG, INT):
    
        self.STR_req = STR
        self.AG_req = AG
        self.INT_req = INT

        # base pool of dices
        self.base_pool = []
        self.magic_pool = []

        # we are appending randomly sized dices to the pool in a number equal to "power" of the item
        scope = len(balance.dices)
        weak_dices = (scope // 4)
        normal_dices = (scope // 2)
        # strong_dices =

        for i in range(self.STR_req):
            self.base_pool.append(balance.dices[random.randint(0, (scope - 3 - 1)) + 3])  # magic number

        for i in range(self.AG_req):
            self.base_pool.append(balance.dices[random.randint(0, weak_dices)])
            self.base_pool.append(balance.dices[random.randint(0, normal_dices)])

        for i in range(self.INT_req):

            self.base_pool.append(balance.dices[random.randint(0, weak_dices)])
            x = random.randint(0, 2)

            if x == 0:
                self.magic_pool.append(arcane.effect(1, "edge", 2))
            if x == 1:
                self.magic_pool.append(arcane.effect(2, "edge", 1))
            if x == 2:
                self.magic_pool.append(arcane.effect(1, "random", 3))

    def Does_Fit(self, UNIT):
        if UNIT.STR >= self.STR_req and UNIT.AG >= self.AG_req and UNIT.INT >= self.INT_req:
            return True
        else:
            return False



    def print_item(self):

        print("STR " + self.STR_req + " AG " + self.AG_req + "  " + self.INT_req)
        for i in self.base_pool:
            print(i, end=" ")

        print()
        for spell in self.magic_pool:
            spell.print()
        print()
