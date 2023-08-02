import random
import time
import os

class Character:
    """
    Initialize player character
    """
    def __init__(self):
        self.name = ""
        self.maxhealth = 1
        self.current_health = 1
        self.attack = 1

class Dragon:
    """
    Initialize dragon enemy character
    """
    def __init__(self):
        self.name = "Dragon"
        self.maxhealth = 1
        self.current_health = 1
        self.attack = 1


def print_pause(message):
    """
    Print a message after a short delay to give enough time for a player to read the message
    """
    print(message)
    time.sleep(1)


def intro():
    """
    Prints the message to welcome player to the game and set the environment of the world
    """
    c = Character()
    players_name = input('Please enter your character name:\n')
    c.name = players_name
    os.system('clear')
    print_pause(f'Welcome, {c.name}!')
    print_pause("You find yourself at the entrance to the dungeon")
    print_pause("It full of dark secrets and treasurs")
    print_pause("But most important - it is a lair of the mighty dragon!")
    print_pause("Will you defeat it, or will you die just like countless heroes died before you?")
    print_pause("Are you ready to start?")

    player_start_selection()

    

def player_start_selection():
    """
    Take player input to start/close the game
    Gives a message if input doesnt match and ask the enter selection once more
    """
    player_choice = input('Press "Y" if you are ready, or "N" if you are affraid of danger: \n')

    
    if player_choice.lower() == 'y':
        start_game()        
    elif player_choice.lower() == 'n':
        print_pause('You decided to exit the game\n')
        exit()
    else:
        print('Please select valid option: "Y" or "N" only\n')
        player_start_selection()

def start_game():
    os.system('clear')
    print_pause('Game has started\n')


intro()


