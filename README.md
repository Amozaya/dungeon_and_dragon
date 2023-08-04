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

    - Player got 3 options available

    ![Fight options](assets/images/fight_options.JPG)

    - By chosing `1` player attacks the dragon. There is a small chance of `miss` and `critical damage`

    



    





## Testing

In this section I did some of the automated and manual tests in order to ensure that project is working correctly.










## Deployment




## Credits

**Content**






