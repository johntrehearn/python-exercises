# Castle Walker

### John Trehearn

This has been updated to include Project 5 tasks.

# Install

## System Requirements

- Python installed
- Python extension installed (if you want to run within VSCode)

## Library Used

- No additional Libraries are needed.

### Please run game.py in the project folder

## Game Idea

- This is a castle adventure game.
- The aim is to explore the castle and collect items.
- The exit door requires certain items to open it.


# Objective

This is an adventure and discovery game based in a castle.

You are arthurian knight of the realm.

The objective is to explore the castle and collect items.

In order to exit the final door, the knight's inventory must contain the potion key and paper sword

The game is structured as follows:

- `game.py` is the main file where the game is run from.
- Game classes are contain in `game_classes.py`.
- Intro is sourced from `intro.txt`
- Instructions are pulled from `instructions.txt`
- Menu items are contained in `menu.py`

The game can be saved and loaded from the game menu. The save information is stored in `save.json`.

# Operating principles

- There is a game loop
- Text is displayed on the screen
- Input is processed
- Game state is updated (location, items)

# Functionalities

- There are text movement controls
- Player has a choice to pick up an item
- Movement controls do not necessarily take you back one room (it is randomised)
- The game can be saved from the game menu
- Player can checked their carbon dioxide emissions

# Sustainable development goal

- The player at any point can check the carbon emissions of their inventory.
- When the player escapes they are told their inventory's carbon dioxide emissions.