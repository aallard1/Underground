"""
This is a simple console game called 'Underground.' 
In it, players can battle enemies that become progressively stronger after each encounter.
Players can also collect items and use them. The random library is used to determine whether a player encounters enemies and items. 
It is also used to determine whether a player is able to strike enemies, block enemy attacks, or flee from combat.
The game ends when a player's health_stat reaches zero.
"""

import random
import os

# These constants are used to determine the players starting attack_stat and defence_stat
MAX_START_STAT = 10
MIN_START_STAT = 1

def main():
    user_stats = {'attack_stat': 0, 'defence_stat': 0, 'health_stat': 20}
    inventory = []
    items = ['rock', 'first aid kit']
    enemy_stats = {'attack_stat': 1, 'defence_stat': 1, 'health_stat': 5}
    in_combat = False
    intro(inventory)
    get_stats(user_stats)
    menu(user_stats, inventory, enemy_stats, items, in_combat)

# This function clears the console when called
def clear_console():
    os.system('clear')

# This function contains the Intro text and takes input from the user
def intro(inventory):
    print("A hooded figure appears before you.\nAh... you look lost. Welcome to the underground.")
    user_name = str(input("What is your name? "))
    print(f"Well, {user_name} , nice to meet you!\nTake this, you'll need it. I have to go now. Good luck to you!\n...\nThe hooded figure melts away into the darkness.\nWhat's this? They dropped a lantern...")
    user_input = str(input("Well, I guess I'm on my own now... \nPress enter to continue."))
    inventory.append('lantern')
    while user_input == '':
        break

"""
This function uses random.randint to get the user's starting stats.
Starting stats are in the range MIN_START_STAT AND MAX_START_STAT inclusively.
"""
def get_stats(user_stats):
    user_stats['attack_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)
    user_stats['defence_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)

# This function contains the game menu.
def menu(user_stats, inventory, enemy_stats, items, in_combat):
    print('')
    print("What should I do?")
    print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m') # Red text
    user_action = str(input("Choose an action: "))
    while user_action != '':
        if user_action == '1':
            print("You move forward in the darkness...")
            enemy_encounter_chance = random.random()
            item_chance = random.random()
            enemy_encounter(user_stats, enemy_stats, enemy_encounter_chance, inventory, items)
            find_item(item_chance, inventory, items)
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '2':
            check_user_stats(user_stats)
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '3':
            print(f"Inventory: {inventory}")
            use_item(inventory, user_stats, enemy_stats, check_enemy_stats, items, in_combat)
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '0':
            clear_console()
            quit()
        else:
            print("I don't think I can do that...")
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
            
# This function prints user stats.
def check_user_stats(user_stats):
    print(f"Your Stats\nAttack: {user_stats['attack_stat']} | Defence: {user_stats['defence_stat']} | Health: {user_stats['health_stat']}")

# This function prints enemy stats.
def check_enemy_stats(enemy_stats):
    print(f"Enemy Stats\nAttack: {enemy_stats['attack_stat']} | Defence: {enemy_stats['defence_stat']} | Health: {enemy_stats['health_stat']}")

# This function determines if the user encounters an enemy. If yes, the user enters combat.
def enemy_encounter(user_stats, enemy_stats, enemy_encounter_chance, inventory, items):
    if enemy_encounter_chance >= 0.5:
        combat(user_stats, enemy_stats, inventory, items)
    else:
        print("Nothing interesting happens...")

# This function determines if the user encounters an item. If yes, it is added to the user's inventory.
def find_item(item_chance, inventory, items):
    item_found = random.choice(items)
    if item_chance >= 0.4:
        print(f"You found a {item_found}!")
        inventory.append(item_found)
    else:
        print('')

"""
This function determines whether the user is able to flee from combat.
If yes, the user is directed back to the menu. If no, the user remains in combat.
"""
def flee(flee_chance, user_stats, inventory, enemy_stats, items, in_combat):
    if flee_chance >= 0.5:
        print("You were able to flee combat...")
        in_combat = False
        menu(user_stats, inventory, enemy_stats, items, in_combat)
    else:
        print("You were not able to flee combat.")

"""
This function determines whether the user is able to attack the enemy and how much damage is dealt.
Damage dealt is based off of the user's attack_stat and the enemy's defence_stat.
"""
def attack(attack_chance, user_stats, enemy_stats, check_enemy_stats):
    if attack_chance >= 0.5:
        print("You strike the enemy...")
        if user_stats['attack_stat'] > enemy_stats['defence_stat']:
            enemy_stats['health_stat'] -= 5
        elif user_stats['attack_stat'] < enemy_stats['defence_stat']:
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 2
        else:
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 1
    else:
        print("You missed...")
        user_stats['health_stat'] -= 5

"""
This function determines whether the user is able to defend against the enemy and how much damage is dealt.
Damage dealt is based off of the user's defence_stat and the enemy's attack_stat.
"""
def defend(defend_chance, user_stats, enemy_stats, check_enemy_stats):
    if defend_chance >= 0.5:
        print("You block the enemy's blow...")
        if user_stats['defence_stat'] > enemy_stats['attack_stat']:
            enemy_stats['health_stat'] -= 2
        elif user_stats['defence_stat'] < enemy_stats['attack_stat']:
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 2
        else:
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 1
    else:
        print("You failed to block the enemy's blow...")
        user_stats['health_stat'] -= 5

# This function allow the user to use their collected items and removes them from the inventory if used.
def use_item(inventory, user_stats, enemy_stats, check_enemy_stats, items, in_combat):
    user_choice = str(input("Would you like to use an item? (1. Yes, 2. No) "))
    if user_choice == '1':
        user_choice = str(input("Which item will you use? "))
        if user_choice == 'first aid kit' and ('first aid kit' in inventory):
            print("You used the first aid kit...")
            user_stats['health_stat'] += 5
            print("You feel a bit better now!")
            inventory.remove('first aid kit')
        elif user_choice == 'rock' and ('rock' in inventory) and in_combat == True:
            print("You throw the rock at the enemy...")
            rock_hit_chance = random.random()
            if rock_hit_chance >= 0.7:
                print("Bull's-eye!")
                enemy_stats['health_stat'] -= 5
                inventory.remove('rock')
            elif rock_hit_chance >= 0.4:
                print("You hit the enemy!")
                enemy_stats['health_stat'] -= 2
                inventory.remove('rock')
            else:
                print("You missed...")
                inventory.remove('rock')
        elif user_choice == 'rock' and ('rock' in inventory) and in_combat == False:
            print("Maybe I should save this for a fight...")
        elif user_choice == 'lantern':
            print("You hold up the lantern and examine your surroundings...")
            print("What is this place?")
            print('')
        else: 
            print("I don't think I can do that...")
    else:
        print('')

"""
This function allows the user to fight enemies.
If the user wins, their stats increase and the next enemy encountered will have increased stats.
If the user loses, the game ends.
"""
def combat(user_stats, enemy_stats, inventory, items):
    in_combat = True
    print("An enemy approaches you.")
    print('')
    print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
    print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
    user_action = str(input("Choose an action: "))
    while user_action != '':
        if user_action == '1':
            print("You attack the enemy...")
            attack_chance = random.random()
            attack(attack_chance, user_stats, enemy_stats, check_enemy_stats)
            if enemy_stats['health_stat'] <= 0:
                print('\033[31m' + "You beat the enemy!" + '\033[0m')
                in_combat = False
                enemy_stats['attack_stat'] += 1
                enemy_stats['defence_stat'] += 1
                enemy_stats['health_stat'] += 10
                user_stats['attack_stat'] += 1
                user_stats['defence_stat'] += 1
                menu(user_stats, inventory, enemy_stats, items, in_combat)
            elif user_stats['health_stat'] <= 0:
                print('\033[31m' + "You have died..." + '\033[0m')
                user_input = str(input("Press enter to continue."))
                while user_input == '':
                    break
                clear_console()
                quit()
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '2':
            print("You defend yourself...")
            defend_chance = random.random()
            defend(defend_chance, user_stats, enemy_stats, check_enemy_stats)
            if enemy_stats['health_stat'] <= 0:
                print('\033[31m' + "You beat the enemy!" + '\033[0m')
                in_combat = False
                enemy_stats['attack_stat'] += 1
                enemy_stats['defence_stat'] += 1
                enemy_stats['health_stat'] += 10
                menu(user_stats, inventory, enemy_stats, items, in_combat)
            elif user_stats['health_stat'] <= 0:
                print('\033[31m' + "You have died..." + '\033[0m')
                user_input = str(input("Press enter to continue."))
                while user_input == '':
                    break
                clear_console()
                quit()
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '3':
            print(f"Inventory: {inventory}")
            use_item(inventory, user_stats, enemy_stats, check_enemy_stats, items, in_combat)
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '4':
            check_user_stats(user_stats)
            check_enemy_stats(enemy_stats)
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: ")) 
        elif user_action == '5':
            print("You attempt to flee...")
            flee_chance = random.random()
            flee(flee_chance, user_stats, inventory, enemy_stats, items, in_combat)
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '0':
            clear_console()
            quit()
        else:
            print("I don't think I can do that...")
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))

if __name__ == "__main__":
    main()