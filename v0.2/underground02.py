import random
import os

# This function clears the console when called
def clear_console():
    os.system('clear')

class user:
    winCount = 0
    user_health = 20
    user_attack = 0
    user_defence = 0

    def init():
        pass
    
# class enemy(user):
#     x = y

class gameEngine():
    seed = random.randint(0,10_000) # 2, 10
    player = user()
    enemy = user()

    def gameMenu():
        userInput = input("0) Exit\nH) Help\n1) Explore")
        if "0" in userInput:
            return 0
            # Exit program
        elif "H" in userInput:
            clear_console()
            print("I) Inventory\nM) Map\nS) Stats")
        elif "1" in userInput:
            pass
            #gameLogic()

    def gameLogic():
        pass
    def engineStart(): # Run all processes
        pass
    def engineOff(): # Cease all processes
        pass

def main():
    # Could collect user alanytics
