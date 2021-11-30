import random

from source_code import units, manager


def attack(dice_pool):
    score = units.attack(dice_pool)

    # counting number of successes
    success = 0
    difficulty = 6

    while difficulty < score:
        score -= difficulty
        difficulty = (difficulty * 1.5)
        success += 1

    return success


def graveyard(fighters):
    for index in range(len(fighters) - 1, -1, -1):
        if fighters[index].HP <= 0:
            fighters.pop(index)

    return len(fighters) == 0


def turn_attacks(attacker, defender):
    # before attack we remove effects from defender
    for fighter in defender:
        fighter.turn_pool = fighter.dice_pool

    # before player attacks we apply effects from players attack to their attacks
    for fighter in attacker:
        fighter.generate_strategy()

    for fighter in attacker:
        for action in range(fighter.attack_speed):
            # here could be a choice to perform different action instead
            target = random.randint(0, len(defender) - 1)

            success = attack(fighter.strategy[action])

            for i in range(success):
                defender[target].HP -= 1

            if success > 0:
                fighter.effect(defender[target].turn_pool, action)


def fight(heroes, enemy):
    # measure the challenge level
    challenge = 0
    for fighter in enemy:
        challenge += fighter.level

    # enemy[0].printing_all_stats()

    # fighting
    print("You encounter", len(enemy), "enemies")

    for rounds in range(50):
        print("1.escape   2.attack")
        choice = manager.choice()
        if choice == 1:  # escape attempt
            # basic roll for each fighter, if player side succeeds
            # if success return false
            if escape():
                return False

        elif choice == 2:
            # player attacks
            # random targets for now
            turn_attacks(heroes, enemy)

            # checking dead enemy
            if graveyard(enemy):
                print("You have won this fight")
                heroes[0].experience(challenge)
                return True

        turn_attacks(enemy, heroes)

        # checking dead in heroes
        if graveyard(heroes):
            print("Your heroes has been defeated GAME OVER")
            exit(666)

    return False  # a draw


def escape():
    if random.randint(0, 1) == 1:
        print("You managed to escape")
        return True
    else:
        print("You failed to escape")
        return False
