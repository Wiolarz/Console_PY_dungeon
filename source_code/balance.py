import terrain

global world


def generate_world():
    global world
    world = terrain.Earth


# set of dices used in a game, its number should not be smaller than 1
# length min(2) else effects will not work
# sorted else effects will not work
dices = [4, 6, 8, 10, 12, 20]  # 4, 6, 8, 10, 12, 20

# max player stats = dices.length
max_power = len(dices)


smallest_dice_value = 1

# main balance values to create gameplay
powerful = 7
strong = 5
medium = 3
weak = 1

# rare = 30 # % chance for something rare to occur

events = 5  # number of events in locations

levelup_speed = 2

# less used ones
shop_items_amount = 15


week = 7

'''
    static void split_dices()
    { # splitting dices into groups based on their highest multiplier
        # kinda works, most likely useless

        ArrayList<ArrayList<Integer>> groups = new ArrayList<>((dices[dices.length-1]) / 2)

        for (int i = 1 i <= (dices[dices.length-1]) / 2 i++)
        {
            groups.add(new ArrayList<>())
            System.out.print(i + " ")
            for (int dice : balance.dices)
            {
                if (dice % i == 0)
                {
                    groups.get(i-1).add(dice)
                }
            }
            System.out.println(groups.get(i-1))
        }
        ArrayList<Integer> existing = new ArrayList<>()
        ArrayList<ArrayList<Integer>> fin = new ArrayList<>(groups.size()-1)
        for (int i  = groups.size() i > 0 i--)
        {
            fin.add(new ArrayList<Integer>())
        }

        for (int i  = groups.size() i > 0 i--)
        {


            for (int dice : groups.get(i-1))
            {
                boolean  existed = false
                for (int d : existing)
                {
                    if (dice == d) existed = true
                }

                if (!existed) fin.get(i-1).add(dice)
            }


            for (int dice : groups.get(i-1))
            {
                existing.add(dice)
            }

            System.out.println(fin.get(i-1))
        }
        System.out.println(fin)

    }'''