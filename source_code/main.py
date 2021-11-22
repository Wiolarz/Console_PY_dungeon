import terrain
import units
import economy

'''

ArrayList<item> item_list = economy.generate_items(days);
ArrayList<location> world = explore.generate_world();


while (choice != 9)
{

    if (main_quest.days_to_complete <= 0)
    { // Time has run out DEFEAT
        output.println(main_quest.fail_story);
        System.exit(3);
    }

    switch (choice)
    {
        case 0 -> {} // starting value, also assigned in case of wrong input
        case 1, 2 -> {}// if choice was not to explore the days are not passing
        default ->
                {
                    main_quest.days_to_complete--;
                    main_quest.check_quest(company.get(0)); //
                    days++;
                    company.add(hero.create_mercenary(days));
                    item_list = economy.generate_items(days);
                }
    }


    main_quest.print_info();
    output.println("Day " + days + "  1 info;   2 shop;  3 world;  9 Exit game");

    choice = input.choice();


    // list of locations
    switch (choice){
        case 1 -> company.get(0).printing_all_stats(); // info
        case 2 -> economy.shop(company.get(0), item_list); // shop
        case 3 -> {
            if(explore.walking(company, world, days))
            {

            }
            else
            {
                choice = 0; // player didn't explore anything
                // TODO this system is bad, day system should be remade
            };
        }
        case 8 -> company.get(0).cheats(); // :))
    }
}
    
'''


def gameplay_loop(heroes):
    world = terrain.earth()
    world.first_quest.print_info()

    heroes.append(units.create_mercenary(world.days))

    print(world.days)
    print(heroes)

    choice = 0

    while choice != 9:
        choice = int(input())



if __name__ == "__main__":

    print("Start")

    # player creation

    heroes = []
    heroes.append(units.hero())

    gameplay_loop(heroes)



