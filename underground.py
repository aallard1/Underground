"""
TODO: Write a description here
"""

import random 

MAX_START_STAT = 10
MIN_START_STAT = 1

def main():
    stats = {'attack_stat': 0, 'defence_stat': 0, 'health_stat': 20}
    intro()
    get_stats(stats)
    menu(stats)

def intro():
    print("Ah... you look lost. Welcome to the underground.")
    user_name = str(input("What is your name? "))
    print(f"Well, {user_name}, nice to meet you!")
    print("Take this, you'll need it. I have to go now. Good luck to you!")
    print("What's this? They dropped a lanturn...")
    print('')

def get_stats(stats):
    stats['attack_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)
    stats['defence_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)

def menu(stats):
    print("Well, I guess I'm on my own now... what should I do?")
    print(f"Attack: {stats['attack_stat']}")
    print(f"Defence: {stats['defence_stat']}")
    print(f"Health: {stats['health_stat']}")

if __name__ == "__main__":
    main()