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
    menu(user_stats, inventory, enemy_stats, items)

def clear_console():
    os.system('clear')

def intro(inventory):
    print("A hooded figure appears before you.\nAh... you look lost. Welcome to the underground.")
    user_name = str(input("What is your name? "))
    print(f"Well, {user_name}, nice to meet you!\nTake this, you'll need it. I have to go now. Good luck to you!\n...\nThe hooded figure melts away into the darkness.\nWhat's this? They dropped a lantern...")
    inventory.append('lantern')
    user_input = input("Well, I guess I'm on my own now... \nPress enter to continue.")
    print('')
    while user_input == '':
        break

def get_stats(user_stats):
    user_stats['attack_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)
    user_stats['defence_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)

def menu(user_stats, inventory, enemy_stats, items):
    print('')
    print("What should I do?")
    print("Move: 1\nCheck Stats: 2\nCheck Inventory: 3\nQuit: 4")
    user_action = str(input("Choose an action: "))
    while user_action != '':
        if user_action == '1':
            print("You move forward in the darkness...")
            enemy_encounter_chance = random.random()
            item_chance = random.random()
            enemy_encounter(user_stats, enemy_stats, enemy_encounter_chance, inventory, items)
            find_item(item_chance, inventory, items)
            user_action = str(input("Choose an action: "))
        elif user_action == '2':
            check_user_stats(user_stats)
            user_action = str(input("Choose an action: "))
        elif user_action == '3':
            print(f"Inventory: {inventory}")
            use_item(inventory, user_stats, enemy_stats, check_enemy_stats, items)
            user_action = str(input("Choose an action: "))
        elif user_action == '4':
            quit()
        else:
            print("I don't think I can do that...")
            user_action = str(input("Choose an action: "))

def check_user_stats(user_stats):
    print(f"Your Stats\nAttack: {user_stats['attack_stat']}\nDefence: {user_stats['defence_stat']}\nHealth: {user_stats['health_stat']}")

def check_enemy_stats(enemy_stats):
    print(f"Enemy Stats\nAttack: {enemy_stats['attack_stat']}\nDefence: {enemy_stats['defence_stat']}\nHealth: {enemy_stats['health_stat']}")

def enemy_encounter(user_stats, enemy_stats, enemy_encounter_chance, inventory, items):
    if enemy_encounter_chance >= 0.5:
        combat(user_stats, enemy_stats, inventory, items)
    else:
        print("Nothing interesting happens...")

def find_item(item_chance, inventory, items):
    item_found = random.choice(items)
    if item_chance >= 0.6:
        print(f"You found a {item_found}!")
        inventory.append(item_found)
    else:
        print('')

def flee(flee_chance, user_stats, inventory, enemy_stats, items):
    if flee_chance >= 0.5:
        print("You were able to flee combat...")
        in_combat = False
        menu(user_stats, inventory, enemy_stats, items)
    else:
        print("You were not able to flee combat.")

def attack(attack_chance, user_stats, enemy_stats, check_enemy_stats):
    if attack_chance >= 0.5:
        print("You strike the enemy...")
        if user_stats['attack_stat'] > enemy_stats['defence_stat']:
            enemy_stats['health_stat'] -= 5
            check_enemy_stats(enemy_stats)
        elif user_stats['attack_stat'] < enemy_stats['defence_stat']:
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 2
            check_enemy_stats(enemy_stats)
    else:
        print("You missed...")
        user_stats['health_stat'] -= 5
        check_enemy_stats(enemy_stats)

def defend(defend_chance, user_stats, enemy_stats, check_enemy_stats):
    if defend_chance >= 0.5:
        print("You block the enemy's blow...")
        if user_stats['defence_stat'] > enemy_stats['attack_stat']:
            enemy_stats['health_stat'] -= 2
            check_enemy_stats(enemy_stats)
        elif user_stats['defence_stat'] < enemy_stats['attack_stat']:
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 2
            check_enemy_stats(enemy_stats)
    else:
        print("You failed to block the enemy's blow...")
        user_stats['health_stat'] -= 5
        check_enemy_stats(enemy_stats)

def use_item(inventory, user_stats, enemy_stats, check_enemy_stats, items):
    user_choice = str(input("Would you like to use an item? (Yes: 1, No: 2) "))
    if user_choice == '1':
        user_choice = str(input("Which item will you use? "))
        if user_choice == 'first aid kit' and ('first aid kit' in inventory):
            user_stats['health_stat'] += 5
            inventory.remove('first aid kit')
        elif user_choice == 'rock' and ('rock' in inventory) and in_combat == True:
            print("You throw the rock at the enemy...")
            rock_hit_chance = random.random()
            if rock_hit_chance >= 0.7:
                print("Bull's-eye!")
                enemy_stats['health_stat'] -= 5
                inventory.remove('rock')
                check_enemy_stats(enemy_stats)
            elif rock_hit_chance >= 0.5:
                print("You hit the enemy!")
                enemy_stats['health_stat'] -= 2
                inventory.remove('rock')
                check_enemy_stats(enemy_stats)
            else:
                print("You missed...")
                inventory.remove('rock')
        elif user_choice == 'rock' and ('rock' in inventory) and in_combat == False:
            print("Maybe I should save this for a fight...")
        elif user_choice == 'lantern':
            print("You hold up the lantern and examine your surroundings...")
            print("What is this place?")
        else: 
            print("I don't think I can do that...")
    else:
        print('')

def combat(user_stats, enemy_stats, inventory, items):
    in_combat = True
    print("An enemy approaches you.")
    print(f"Attack: {enemy_stats['attack_stat']}\nDefence: {enemy_stats['defence_stat']}\nHealth: {enemy_stats['health_stat']}")
    print('')
    print("Attack: 1\nDefend: 2\nUse Item: 3\nCheck Stats: 4\nFlee: 5")
    user_action = str(input("Choose an action: "))
    while user_action != '':
        if user_action == '1':
            print("You attack the enemy...")
            attack_chance = random.random()
            attack(attack_chance, user_stats, enemy_stats, check_enemy_stats)
            if enemy_stats['health_stat'] <= 0:
                print("You beat the enemy!")
                in_combat = False
                enemy_stats['attack_stat'] += 1
                enemy_stats['defence_stat'] += 1
                enemy_stats['health_stat'] += 10
                user_stats['attack_stat'] += 1
                user_stats['defence_stat'] += 1
                menu(user_stats, inventory, enemy_stats)
            elif user_stats['health_stat'] <= 0:
                print("You have died...")
                quit()
                clear_console()
            user_action = str(input("Choose an action: "))
        elif user_action == '2':
            print("You defend yourself...")
            defend_chance = random.random()
            defend(defend_chance, user_stats, enemy_stats, check_enemy_stats)
            if enemy_stats['health_stat'] <= 0:
                print("You beat the enemy!")
                in_combat = False
                enemy_stats['attack_stat'] += 1
                enemy_stats['defence_stat'] += 1
                enemy_stats['health_stat'] += 10
                menu(user_stats, inventory, enemy_stats, items)
            elif user_stats['health_stat'] <= 0:
                print("You have died...")
                quit()
                clear_console()
            user_action = str(input("Choose an action: "))
        elif user_action == '3':
            print(f"Inventory: {inventory}")
            use_item(inventory, user_stats, enemy_stats, check_enemy_stats, items)
        elif user_action == '4':
            check_user_stats(user_stats)
            user_action = str(input("Choose an action: ")) 
        elif user_action == '5':
            print("You attempt to flee...")
            flee_chance = random.random()
            flee(flee_chance, user_stats, inventory, enemy_stats, items)
            user_action = str(input("Choose an action: "))
        else:
            print("I don't think I can do that...")
            user_action = str(input("Choose an action: "))

if __name__ == "__main__":
    main()