import random

import balance


class Effect:
    def __init__(self, usage, effect_type, force):
        self.usages = usage
        self.type = effect_type
        self.power = force

    def print(self):
        print("[")
        print("%-10s", ("usages: " + self.usages))
        print("%-12s", ("type: " + self.type))
        print("%-10s", ("power: " + self.power + "]"))

    def short_print(self):
        text = self.usages + " " + self.type + " " + self.power + " "
        # print(text)
        return text

    def use(self, dices):
        if self.type == "value":
            self.value_effect(dices)
        elif self.type == "edge":
            self.edge_effect(dices)
        elif self.type == "random":
            self.r_target_effect(dices)

    def value_effect(self, dices):
        # effect  to a target, changing it to a "type" value
        cur_usage = self.usages
        for i in range(dices):
            if dices[i] == balance.dices[self.power] and cur_usage > 0:
                # effect
                dices[i] = balance.smallest_dice_value

                cur_usage -= 1

    def edge_effect(self, dices):
        # we modify the highest values
        for i in range(self.usages):
            try:
                # effect
                idx = 0
                dices_idx = 0
                max = dices[0]
                
                for dice_val in dices:
                    if max < dice_val:
                        max = dice_val
                        dices_idx = idx
                    idx += 1

                dices[dices_idx] = self.dice_change(dices[dices_idx], -self.power)
            except:
                print("Cannot work with dice pool smaller than 2")

    def r_target_effect(self, dices):
        # random dice from the pool
        for i in range(self.usages):
            try:
                # effect
                target = random.randint(0, (len(dices)-1))
                dices[target] = self.dice_change(dices[target], -self.power)
            except:
                print("cannot work with dice pool smaller than 2")

        # Functions called by the effects:

    def dice_change(self, dice, value):
        # used by other effects to change dice to another one
        address = 0
        for d in balance.dices:
            if d == dice:
                break
            
            address += 1

        for i in range(abs(value)):
            if value > 0:
                if balance.dices.length-1 == address:
                    return dice  # if dice is already at max value we cannot upgrade it
                address += 1
                dice = balance.dices[address]
            else:
                if 0 == address:
                    return dice  # if dice is already at min value we cannot downgrade it
                
                address -= 1
                dice = balance.dices[address]

        return dice
