"""
TODO: Write a description here
"""

import random 

MAX_START_STAT = 10
MIN_START_STAT = 1

def main():
    attack_stat = 0
    defence_stat = 0
    health_stat = 20
    intro()
    get_stats(attack_stat, defence_stat)
    menu(attack_stat, defence_stat, health_stat)

def intro():
    print("Ah... you look lost. Welcome to the underground.")
    user_name = str(input("What is your name? "))
    print(f"Well, {user_name}, nice to meet you!")
    print("Take this, you'll need it. I have to go now. Good luck to you!")
    print("What's this? They dropped a lanturn...")
    print('')

def get_stats(attack_stat, defence_stat):
    attack_stat = random.randint(MIN_START_STAT, MAX_START_STAT)
    defence_stat = random.randint(MIN_START_STAT, MAX_START_STAT)
    return attack_stat, defence_stat

def menu(user_attack_stat, user_defence_stat, health_stat):
    print("Well, I guess I'm on my own now... what should I do?")
    print(f"Attack: {attack_stat}")
    print(f"Defence: {defence_stat}")
    print(f"Health: {health_stat}")

if __name__ == "__main__":
    main()