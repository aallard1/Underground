"""
TODO: Write a description here
"""

import random
import os

MAX_START_STAT = 10
MIN_START_STAT = 1

def main():
    stats = {'attack_stat': 0, 'defence_stat': 0, 'health_stat': 20}
    inventory = []
    items = []
    enemy = {'attack_stat': 1, 'defence_stat': 1, 'health_stat': 5}
    intro(inventory)
    get_stats(stats)
    menu(stats, inventory, enemy)

def clear_console():
    os.system('clear')

def intro(inventory):
    print("A hooded figure appears before you.")
    print("Ah... you look lost. Welcome to the underground.")
    user_name = str(input("What is your name? "))
    print(f"Well, {user_name}, nice to meet you!")
    print("Take this, you'll need it. I have to go now. Good luck to you!")
    print("...")
    print("The hooded figure melts away into the darkness.")
    print("What's this? They dropped a lanturn...")
    inventory.append('lanturn')
    user_input = input('')
    while user_input == '':
        break

def get_stats(stats):
    stats['attack_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)
    stats['defence_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)

def menu(stats, inventory, enemy):
    print("Well, I guess I'm on my own now... what should I do?")
    print("Move: 1")
    print("Check Stats: 2")
    print("Check Inventory: 3")
    print("Quit: 4")
    user_action = str(input("Choose an action: "))
    while user_action != '':
        if user_action == '1':
            print("You move forward in the darkness...")
            enemy_encounter_chance = random.random()
            # item_chance = random.random()
            enemy_encounter(stats, enemy, enemy_encounter_chance)
            user_action = str(input("Choose an action: "))
        elif user_action == '2':
            check_stats(stats)
            user_action = str(input("Choose an action: "))
        elif user_action == '3':
            print(f"Inventory: {inventory}")
            user_action = str(input("Choose an action: "))
        elif user_action == '4':
            quit()
        else:
            print("I don't think I can do that...")
            user_action = str(input("Choose an action: "))

def check_stats(stats):
    print(f"Attack: {stats['attack_stat']}")
    print(f"Defence: {stats['defence_stat']}")
    print(f"Health: {stats['health_stat']}")

def enemy_encounter(stats, enemy, enemy_encounter_chance):
    if enemy_encounter_chance >= 0.5:
        combat(stats, enemy)
    else:
        print("Nothing interesting happens...")

def combat(stats, enemy):
    print("An enemy approaches you.")
    print("Attack: 1")
    print("Defend: 2")
    print("Flee: 3")
    user_action = str(input("Choose an action: "))

if __name__ == "__main__":
    main()