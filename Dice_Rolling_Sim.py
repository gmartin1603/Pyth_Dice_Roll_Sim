'''
Name:
  Dice_Rolling_Sim

Purpose:
  make a program to replace the dice in a board game

  the user should be able to input how many die and how many sides are on each dice

  the returned value should be a random value that would be possible with
  real dice

Interface:
    Terminal

Use:
    Enter how many dice.
    Enter the number of sides each dice has.
    "Enter" to roll again or "n" to terminate.

'''
__verion__ = 0.2

import random

#type = input('Do the die have words or numbers? ')
    #validate that either 'words' or 'numbers' was typed
dice = int(input('How many dice are there? '))

if dice == 1:
    side = int(input('How many sides does it have? '))
else:
    side = int(input('How many sides do they have? '))

again = '\n'

while again != 'n':
    def roll(sides,die):
        result = 0
        sides = side
        die = dice
        for rolls in range(die):
            result += random.randint(1,sides)
        return result
    print(roll(side,dice))
    again = input('Roll again? ^/n ')
    continue
