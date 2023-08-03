import random
import time
import os


class Character:
    """
    Initialize player character
    """
    def __init__(self):
        self.name = ""
        self.maxhealth = 30
        self.current_health = self.maxhealth
        self.attack = 5
        self.armor = 0
        self.potion = 2




class Dragon:
    """
    Initialize dragon enemy character
    """
    def __init__(self):
        self.name = "Dragon"
        self.maxhealth = 50
        self.current_health = 50
        self.attack = 10




def print_pause(message):
    """
    Print a message after a short delay
    to give enough time for a player to read the message
    """
    print(message)
    time.sleep(1)


def start_game():
    """
    Ask a player to input the name for their character
    and asisgns it to the Character class
    """
    players_name = input('Please enter your character name:\n')
    player.name = players_name
    print_pause(f'Your name is {player.name}!')
    current_player_health()
    current_player_attack()
    current_player_armor()
    current_player_potion()
    print_pause("")
    intro()


def intro():
    """
    Prints the message to welcome player to the game
    and set the environment of the world
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
    player_choice = input('Press "Y" if ready, or "N" if you are not:\n')

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
    current_player_health()
    print_pause('\n')
    print_pause('After escaping the trap you notice this coridor is a dead end.')
    print_pause('You have to return back to the firt room')
    first_room()


def second_room():
    """
    Gives player an option to open a chest
    Requires player's input
    If yes - player will attempt to open chest
    If no - player will skip the chest
    """
    os.system('clear')
    print_pause('You proceed farther into the dungeon')
    print_pause('You find yourself in the large room')
    print_pause('In the middle of the room you see a chest')
    print_pause('You approach to the chest and see the following writing: \n')
    print_pause('This chest is cursed. If you wish to open it you need to make a sacrifice.\n')

    option = input('Do you dare to open it? "Y/Yes" to try and open, or any other key to leave the chest alone:\n')

    if option.lower() == 'y' or option.lower() == 'yes':
        open_chest()

    else:
        print_pause('You decided not to open the chest')
        dragon_lair()


def open_chest():
    """
    Will take an input from the player to make sacrifice
    Checks for incorrect value and loops until player enters correct value
    """
    os.system('clear')
    print_pause('You decided to open the chest')
    print_pause('When you trying to open it you hear a voice in your head:\n')
    print_pause('"If you wish to gain our treasures you must make a sacrifice..."')
    print_pause('"Some of your health or your potion for our treasuers"')
    print_pause('"What are you willing to sacrifice?"\n')

    while True:
        sacrifice_option = input('Will you sacrifice "Health" or "Potion"?:\n')
        if sacrifice_option.lower() == 'health' or sacrifice_option.lower() == 'potion':
            option = sacrifice_option.lower()
            sacrifice(option)
            return False
        else:
            print_pause('Please chose the correct option: "Health" or "Potion"!')


def sacrifice(option):
    """
    Depending on the sacrifice player decided to make
    player will get some bonus:
    - for potion - extra attach and armor
    - for health - extra potion and attack
    """
    os.system('clear')
    print_pause(f'You decided to sacrfice your {option}')

    if option == "health":
        player.current_health -= 5
        print_pause('You have sacrificied 5 of your health')
        current_player_health()
        player.attack += 3
        player.potion += 1

        print_pause('As a reward, you receive "+3" to Attack, and "+1" to Potion')
        current_player_attack()
        current_player_potion()

    if option == "potion":
        player.potion -= 1
        current_player_potion()

        player.armor += 30
        player.attack += 2
        print_pause('As a reward, you receive "+2" to Attack, and "+30" to Armor')
        current_player_attack()
        current_player_armor()
    dragon_lair()


def dragon_lair():
    """
    Final room where the dragon lives
    It will introduce player to the dragon and start the fight
    """
    os.system('clear')
    print_pause('You walk away from the chest and make your way deeper into the dungeon')
    print_pause('Finally you arrive to the last room')
    print_pause('You look around...')
    print_pause('The room is full of treasuers')
    print_pause('And the bones of fallen heroes')
    print_pause("It's a dragon lair!")
    print_pause('You start hearing some heavy steps')
    print_pause('They are getting closer...')
    print_pause('The dragon has returned!')
    print_pause('There is no escape from this room')
    print_pause('You draw your sword and prepare to fight')
    input('\nPress any key to start...')
    final_fight()


def final_fight():
    """
    Determinds the main fight logic
    First it gives player to chose their option:
    - attack the dragon
    - use potion to refil their health
    After player makes a choise they get attacked by a dragon
    Repeats until someone dies
    """
    os.system('clear')
    print_pause(f'{player.name} is fighting the dragon')



def current_player_health():
    # Print player's health stats
    print_pause(f'Your current health is {player.current_health}')


def current_player_potion():
    # Print player's potion stats
    print_pause(f'Your current potion number is {player.potion}')


def current_player_armor():
    # Print player's armor stats
    print_pause(f'Your current armor is {player.armor}')


def current_player_attack():
    # Print player's attack stats
    print_pause(f'Current attack is {player.attack}')


def current_enemy_health():
    # Print dragon's health stats
    print_pause(f'Dragon current health is {enemy.current_health}')


"""
Create global variables to have access to Player character and Dragon enemy attributes
"""
character = Character()
dragon = Dragon()
global player
player = character
global enemy
enemy = dragon


dragon_lair()
