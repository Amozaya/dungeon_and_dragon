import random
import time
import os
import math


class Character:
    """
    Initialize player character
    """
    def __init__(self):
        self.name = "Hero"
        self.maxhealth = 30
        self.current_health = self.maxhealth
        self.attack = 7
        self.armor = 20
        self.potion = 2


class Dragon:
    """
    Initialize dragon enemy character
    """
    def __init__(self):
        self.name = "Dragon"
        self.current_health = 60
        self.attack = 10


def print_pause(message):
    """
    Print a message after a short delay
    to give enough time for a player to read the message
    """
    print(message)
    time.sleep(2)


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
    print('\n-----------------------------------------------------\n') 
    intro()


def intro():
    """
    Prints the message to welcome player to the game
    and set the environment of the world
    """    
    print_pause(f'Welcome, {player.name}!')
    print_pause("You find yourself at the entrance to the dungeon")
    print_pause("It full of dark secrets and treasurs")
    print_pause("But most important - it is a lair of the mighty dragon!")
    print_pause("Will you defeat it, or will you die just like countless heroes died before you?")
    print_pause("Are you ready to start?")
    print('\n-----------------------------------------------------\n') 
    player_start_selection()


def player_start_selection():
    """
    Take player input to start/close the game
    Gives a message if input doesnt match and ask the enter selection once more
    """
    player_choice = input('Press "Y" if ready, or "N" to exit:\n')

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
    print('\n-----------------------------------------------------\n')     
    print_pause('You enter the room to the right and trigger the trap')
    damage = random.randint(1, 5)
    print_pause(f'Trap deals {damage} damage')
    player.current_health -= damage
    current_player_health()
    print_pause('\n')
    print_pause('After escaping the trap you notice this coridor is a dead end.')
    print_pause('You have to return back to the firt room')
    print('\n-----------------------------------------------------\n') 
    first_room()


def second_room():
    """
    Gives player an option to open a chest
    Requires player's input
    If yes - player will attempt to open chest
    If no - player will skip the chest
    """
    print('\n-----------------------------------------------------\n') 
    print_pause('You proceed farther into the dungeon')
    print_pause('You find yourself in the large room')
    print_pause('In the middle of the room you see a chest')
    print_pause('You approach to the chest and see the following writing: \n')
    print_pause('"This chest is cursed. If you wish to open it you need to make a sacrifice."\n')

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
    print('\n-----------------------------------------------------\n')  
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

        player.armor += 20
        player.attack += 2
        print_pause('As a reward, you receive "+2" to Attack, and "+20" to Armor')
        current_player_attack()
        current_player_armor()
    dragon_lair()


def dragon_lair():
    """
    Final room where the dragon lives
    It will introduce player to the dragon and start the fight
    """
    print('\n-----------------------------------------------------\n')     
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
    os.system('clear')
    final_fight()


def final_fight():
    """
    Determinds the main fight logic
    First it gives player to chose their option:
    - attack the dragon
    - use potion to refil their health
    - run away to finish the game without fighting
    After player makes a choise they get attacked by a dragon
    Repeats until someone dies
    """
    #os.system('clear')
    print_pause(f'\n{player.name} is fighting the {enemy.name}')
    current_player_health()
    current_player_potion()
    current_player_armor()
    current_enemy_health()
    print('-----------------------------------------------------')
    print('You attack first')
    print('Chose your move: ')
    print('1 - Attack')
    print('2 - Use potion to restore health')
    print('3 - Try to run past the dragon to escape')
    print('"Running away has a very little chance of surviving"')
    print('-----------------------------------------------------')


    while True:
        move = input('>>> ')
        if move == '1':
            player_attack()
            return False
        
        elif move == '2':
            if player.potion > 0:
                use_potion()
                return False
            else:
                print('You are out of potions')
        elif move == '3':
            escape_fight()
            return False
        else:
            print('Invalid option. Please select the valid move!')


def player_attack():
    """
    Player attacks the gragon and causes damage
    Checks if dragon got any health left
    """
    print_pause(f'\n{player.name} attacks the {enemy.name}')
    print('-----------------------------------------------------')    
    damage = random.randint(round(player.attack / 2), player.attack)
    if random.randint(1, 10) == 1:
        print_pause('You missed your hit')
        print_pause(f'You deal no damage to {enemy.name}')
    else:    
        if random.randint(1, 5) == 1:
            damage = math.floor(damage * 1.5) 
            print_pause(f'You got Critical Hit and deal higher damage') 
            print_pause(f'You deal {damage} damage to {enemy.name}')
            enemy.current_health -= damage
        else:  
            print_pause(f'You deal {damage} damage to {enemy.name}')    
            enemy.current_health -= damage
    check_enemy_health()
    

def use_potion():
    """
    Player consumes 1 potion to restore health
    If restored health will be more than maxhealth
    it sets current health to maxhealth
    """
    print('-----------------------------------------------------')
    print_pause('You drink the potion')
    player.potion -= 1
    print_pause('You restore 20 health')
    player.current_health += 20
    if player.current_health > player.maxhealth:
        player.current_health = player.maxhealth
    current_player_health()
    enemy_attack()
    

def escape_fight():
    """
    Prints a message telling the player they need to roll the die
    to see if they can escape
    Takes player input (any key) to roll
    """
    print('-----------------------------------------------------')
    print_pause('You decided to try to run away')
    print_pause('Will you be lucky enough to escape?')
    print_pause('Roll a die to find out')
    print_pause('"Need 15 or higher to succseed"')
    print('-----------------------------------------------------')
    input('\nPress any key to roll...')
    roll_die()


def roll_die():
    """
    Gets a random int between 1 and 18
    If roll is >= 15, than player is lucky and survives
    If roll is < 15, than player dies
    """
    roll = random.randint(1, 18)

    if roll >= 15:
        print_pause(f'You rolled {roll}')
        print_pause('Luck is on your side')
        print_pause('You manage to escape the dragon and survive')
        print_pause('However, you earned no glory, nor treasurs')
        print_pause('Maybe next time you will be more brave...')
        close_game()
    else:
        print_pause(f'You rolled {roll}')
        print_pause('Luck has abandoned you')
        print_pause(f'{enemy.name} was quicker than you')
        print_pause('You got caught trying to escape and died!')
        print_pause('Better luck next time')
        close_game()


def enemy_attack():
    """
    Enemy attacks the player and causes damage
    Checks if player got any health left
    Checks if player got any armor left
    If player health <= 0 lose the game
    """
    print_pause(f'\n{enemy.name} attacks {player.name}')
    print('-----------------------------------------------------')
    if random.randint(0, 3) <= 2:
        print_pause(f'{enemy.name} attacks with Base Attack')
        damage = random.randint(round(enemy.attack / 2), enemy.attack)
        has_armor(damage)        
    else:
        print_pause(f'{enemy.name} attacks {player.name} with Fire Breath')        
        if player.armor > 0:
            print_pause('It melts your armor and burns your skin underneath')
            print_pause(f'{enemy.name} does 3 damage to {player.name}')
            has_armor(8)
            player.current_health -= 3
        else:
            print_pause('Fire Breath burns your skin')
            print_pause(f'{enemy.name} does 8 damage to {player.name}')
            player.current_health -= 8
    check_player_health()
    

def has_armor(damage):
    """
    Checks if player got any armor left
    If yes, reduces the armor    
    If no armor then damaged cause directly to health
    """
    if player.armor > 0:
        player.armor -= damage
        print(f'Armor reduced by {damage}')
        if player.armor <= 0:
            print('Your armor is destroyed')
            player.armor = 0
    else:
        player.current_health -= damage
        print_pause(f'{enemy.name} does {damage} damage to {player.name}')


def close_game():
    """
    Stops the game
    """
    print('\n-----------------------------------------------------\n')    
    print('The game is closing now!')
    print('\n-----------------------------------------------------\n')  

    
def check_player_health():
    """
    Checks if player got any health left
    If yes, carry on fight
    If no, stops the game
    """
    if player.current_health > 0:
        final_fight()
    else:
        player.current_health = 0
        current_player_armor()
        current_player_health()
        lose()


def check_enemy_health():
    """
    Checks enemy health
    If health is > 0, continue the fight
    If health is < 0, win the game
    """
    if enemy.current_health > 0:
        current_enemy_health()
        enemy_attack()
    else:
        print_pause(f'You defeated the {enemy.name}')
        time.sleep(2)
        win()


def win():
    """
    Notifies the player that they won the game
    Stops the game
    """
    print('\n-----------------------------------------------------\n') 
    print_pause(f'You managed to defeat the {enemy.name}')
    print_pause('You earned all the glory and treasurs')
    print_pause('And from now on')
    print_pause('Your name will be in legends forever...')
    print_pause(f'{player.name} - the {enemy.name} Slayer!')
    close_game()


def lose():
    """
    Notifies the player that they died and lose the game
    Stops the game
    """
    os.system('clear')
    print_pause(f'The {enemy.name} has defeated {player.name}')
    print_pause('Unfortunately, you have fallen')
    print_pause('Just as many heroes have fallen before you')
    print_pause('Who will be brave enough to try next?')    
    close_game()


def current_player_health():
    # Print player's health stats
    print(f'Your current health is {player.current_health}')


def current_player_potion():
    # Print player's potion stats
    print(f'Your current potion number is {player.potion}')


def current_player_armor():
    # Print player's armor stats
    print(f'Your current armor is {player.armor}')


def current_player_attack():
    # Print player's attack stats
    print(f'Current max attack is {player.attack}')


def current_enemy_health():
    # Print dragon's health stats
    print(f'Dragon current health is {enemy.current_health}')


"""
Create global variables to have access to Player character and Dragon enemy attributes
"""
character = Character()
dragon = Dragon()
global player
player = character
global enemy
enemy = dragon


start_game()
