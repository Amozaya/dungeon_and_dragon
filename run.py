import random
import time
import os

class Character:
    """
    Initialize player character
    """
    def __init__(self):
        self.name = ""
        self.maxhealth = 20
        self.current_health = 20
        self.attack = 1

character = Character()

class Dragon:
    """
    Initialize dragon enemy character
    """
    def __init__(self):
        self.name = "Dragon"
        self.maxhealth = 1
        self.current_health = 1
        self.attack = 1

dragon = Dragon()

def print_pause(message):
    """
    Print a message after a short delay to give enough time for a player to read the message
    """
    print(message)
    time.sleep(1)

def start_game():   
    """
    Ask a player to input the name for their character and asisgns it to the Character class
    """ 
    players_name = input('Please enter your character name:\n')
    player.name = players_name
    intro()

def intro():
    """
    Prints the message to welcome player to the game and set the environment of the world
    """  
    
    os.system('clear')
    print_pause(f'Welcome, {player.name}!')
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
        first_room()        
    elif player_choice.lower() == 'n':
        print_pause('You decided to exit the game\n')
        exit()
    else:
        print('Please select valid option: "Y" or "N" only\n')
        player_start_selection()

def first_room():
    """
    First room of the dungeon that gives player the choice of 2 directions:
    - left, which leads further into the dungeon
    - right, which leads to the trap room
    """
    os.system('clear')
    print_pause('You are in the first room of the dungeon')
    print_pause('You see two corridors:')
    print_pause('One is on your left')
    print_pause('And the other one is on your right')
    print_pause('Which one will you choose?')
    print_pause('Left or Right')
    corridor_selection()

def corridor_selection():
    """
    Takes input from the player depending which direction they want to go
    If input is invalid it asks player to enter their option once more
    """
    selection = input('>>> ')

    if selection.lower() == 'left':
        second_room()
    elif selection.lower() == 'right':
        trap_room()
    else:
        print('Please select valid option: "Left" or "Right"\n')
        corridor_selection()

def second_room():
    os.system('clear')
    print_pause('You are in the second room')


def trap_room():
    """
    When player walks into trap room it deals the damage
    Damage is random
    After that, it takes the player back to the prvious room
    """
    os.system('clear')
    print_pause('You enter the room to the right and trigger the trap')
    damage = random.randint(1, 5)    
    print_pause(f'Trap deals {damage} damage')
    player.current_health -= damage
    print_pause(f'You have {player.current_health} out of {player.maxhealth} health left')
    print_pause('\n')
    print_pause('After escaping the trap you notice this coridor is a dead end.')
    print_pause('You have to return back to the firt room')
    first_room()

"""
Create global variables to have access to Player character and Dragon enemy attributes
"""
global player
player = character
global enemy
enemy = dragon


trap_room()


