import units
import economy
import balance
import explore


def gameplay_loop(heroes):
    balance.generate_world()

    balance.world.main_quest.print_info()

    heroes.append(units.create_mercenary(balance.world.days))

    print(balance.world.days)
    print(heroes)

    shops_items = economy.generate_items(1)

    choice = 0
    while choice != 9:
        choice = int(input())

        if balance.world.main_quest.days_to_complete <= 0:
            # Time has run out DEFEAT
            print(balance.world.main_quest.fail_story)
            exit()

        # if choice == 0: # starting value, also assigned in case of wrong input

        if choice  < 3: # if choice was not to explore the days are not passing
            pass
        else:
            balance.world.main_quest.days_to_complete -= 1
            balance.world.main_quest.check_quest(heroes[0]) #
            balance.world.days += 1
            heroes.append(units.create_mercenary(balance.world.days))
            item_list = economy.generate_items(balance.world.days)

            balance.world.main_quest.print_info()
            print("Day " + balance.world.days + "  1 info   2 shop  3 world  9 Exit game")

            choice = int(input())

            # list of locations
            if choice == 1:
                heroes[0].printing_all_stats()  # info
            elif choice == 2:
                economy.shop(heroes[0], item_list)  # shop
            elif choice == 3:
                if not explore.walking(heroes, balance.world, balance.world.days):
                    choice = 0  # player didn't explore anything
                    # TODO this system is bad, day system should be remade
            elif choice == 8:
                heroes[0].cheats()


if __name__ == "__main__":

    print("Start")

    # player creation

    heroes = []
    heroes.append(units.hero())

    gameplay_loop(heroes)



