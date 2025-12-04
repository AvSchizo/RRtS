import random
import time

import Flip_Coin

import Gun_Object
from Gun_Object import revolve, fire, revPrint, gunInfo, reloadGun, checkReload

import Character_Object
from Character_Object import printHealth

from Start_Screen import startScreen

import Round_List

from Display_Info import displayInfo

#### SET UP OBJECTS ####

# set up gun
gun = Gun_Object.gun

# set up characters
player = Character_Object.player
enemy = Character_Object.enemy

# set up coin flip
def flipCoin():
    coinFlip = Flip_Coin.flipCoin()
    if coinFlip == 1:
        enemy.takeTurn = True
    else:
        enemy.takeTurn = False

#### DEF FUNC ####

def healthDown(char):
    char.health -= gun.damage

def setCharHealth(char1, char2, round):
    char1.health = round.maxHealth
    char2.health = round.maxHealth



###################### START SCREEN ######################
playTutorial = startScreen()
##########################################################
##########################################################

### Maybe have a mechanic where the play chooses how hard to spin the cylinder ###

if playTutorial == True:
    import RR_Tutorial

print("running back on russianroulette.py")