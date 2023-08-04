# Dungeon & Dragon

Dungeon & Dragon is a text based RPG fantasy game, which runs in the terminal on Heroku.

User plays as a brave hero exploring the dragon's lair. The aim of the game is to find the lair and defeat the dragon using your skills, and a bit of luck.

![Heading](assets/images/heading.JPG)

## Instructions how to play

The game is a text based, so it is important that user reads all the instructions in the terminal.

In order to act in the game, or chose the options, user has to type the command in the terminal and press `Enter`. Text is not case sensetive, so it won't matter if the user writes command in all lower or all capitilized characters. Possible commands will always be displayed in text instructions, so it is important to enter text identical to the options provided. If user enters incorrect command the program will give an eror message and ask user to enter the correct command.

All the lines where user's input required start with `>>>`.

There is only one type of attack available for the user, however, it got a chance of a critical attack which deals higher damage.

The game is turn based, so when user attacks the dragon the user's turn is over and then computer's turn starts.

User can also use `Potion` to restore the health, however, using the potion will end your turn, meaning you can't attack the same turn as you use the potion.

To win the game user has to defeat the dragon before it kills them. 

It is possible to try and `escape` the fight, but it got a low chance of succseeding.

## Features

### Existing Features

* Naming your character:

    - Player can name their character and game will use that name to address the player

    ![Character name selection](assets/images/name_selection.JPG)

    - Player can chose to skip the name selection and press `Enter`, then the game will use default name

    ![Default name](assets/images/default_name.JPG)

    - Game will also check to ensure that the name doesnt start with en empty character or a number

    ![Invalid name](assets/images/invalid_name.JPG)

* Chosing your path:

    - In a few occassions player will be given a choice to chose the direction or their next action

    ![Room choice](assets/images/room_choice.JPG)

    - Wrong choices can lead to negative concequences 

    ![Trap room](assets/images/trap_room.JPG)

* Treasure chest:

    - In the dungeon user can find a chest with treasuers. Opening it will grant some reward, however, player required to make a sacrifice

    - Depending on the sacrifice player choses to make, reward will be different

    ![Opening chest](assets/images/opening_chest.JPG)

* Player stats:

    - Health - the most important stat. If it goes down to `0` you lose the game. Base values is `30`, can be restored with potions.

    - Armor - protects the player from the attacks. If armor is `0` then all the damage goes to `health`. Base value is `20`, but can be increased by opening chest

    - Potion - player can drink potion to restore some of their health. Doesn't restore armor. Base value is `2`, but can be increased or decreased by opening the chest

    - Max attack - the maximum damage player can do with base attack. There is a small chance of `miss` and `critical damage` present. Base attack `7`, but can be increased by opening the chest

    ![Base stats](assets/images/base_stats.JPG)

* Dragon stats:

    - Health - base calue is `60`. Cannot be restored. If health goes to `0` then player wins the game

    - Max attack - the maximum damage dragon can do with base attack, and base value is `10`. The is no critical damage

* Fight:

    - Fight is turn based

    - Player got 3 options available:

    ![Fight options](assets/images/fight_options.JPG)

    - By chosing `1` player attacks the dragon. There is a small chance of `miss` and `critical damage`

        ![Player attack](assets/images/player_attack.JPG)


        ![Critical damage](assets/images/critical_attack.JPG)


        ![Missed attack](assets/images/missed_attack.JPG)

    - By chosing `2` player will drink the potion and restore some amount of their health

        ![Drink potion](assets/images/use_potion.JPG)

    - By chosing `3` player will end the fight, but there is a high chance of losing the game

        ![Die roll](assets/images/die_roll.JPG) 

        ![Unlucky die roll](assets/images/unlucky_die_roll.JPG)


* Dragon attacks:

    - Dragon has two types of attacks, which are random:

        - Base attack deals physical damage

        - If player got armor, it will first target the armor. If armor drops to `0` then it will be destroyed and dragon will deal the damage directly to health

        ![Destroyed armor](assets/images/destroy_armor.JPG)

        - "Fire Breath" deals fire damage

        - If player got armor, it deals high damage to the armor and small damage to health

        - If player got no armor then it deals high damage to health

        ![Fire Breath](assets/images/fire_breath_attack.JPG)

* Winning the game:

    - To win the game player has to drop Dragon's health to `0`

    ![Win game](assets/images/wint_the_game.JPG)

* Losing the game:

    - To lose the game player has to lose all the health

    ![Lose game](assets/images/game_over.JPG)


### Feature Features

* Allow user to distribute stats instead of hardcoding them

* Add an extra attack or spell for player to use in a fight

* Increase the size of the dungeon

* Add more traps, chest, enemies

* Make random paths


## Data Model

For this game I used Character and Dragon class for game characters. It allowed me to store and modify the attributes, such as name, health, attack, armor, and potion.

I created functions that would access those attributes and print them out for a user, so user is always aware what the stats are for their character and for the enemy. 

I also created attack functions that would access the `Maxattack` attribute from the class and ue it in the formula to calculate the damage of the attack.

### Libraries

I imported and used the following libraries:

- `random` - used to create a randomize damage from attacks and trap, as well as the chance of critical damage and missed attack. Also, it used when rolling a die to see if escape is succssesful

- `os` - used to run a command ```os.system(\`clear\`)``` to clear the screen when th fight starts. Helps to keep the console cleaner for the user

- `math` - used `math.floor` and `math.round` when calculating the damage

-`time` - used `time.sleep(1.5)` to reduce the time that instructions appear with, allowing more time for a user to read all of the instructions







    





## Testing

In this section I did some of the automated and manual tests in order to ensure that project is working correctly.










## Deployment




## Credits

**Content**






