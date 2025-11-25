import random
import time

import Flip_Coin
import Gun_Object
from Gun_Object import revolve, fire, revPrint, gunInfo
import Character_Object

#### SET UP OBJECTS ####

# set up gun
gun = Gun_Object.gun

# set up characters
player = Character_Object.character()
enemy = Character_Object.character()

# set up coin flip
coinFlip = Flip_Coin.flipCoin()
if coinFlip == 1:
    enemy.takeTurn = True
else:
    enemy.takeTurn = False

#### DEF FUNC ####

def healthDown(character, gun):
    character.health -= gun.damage


################################ NO ITEMS ################################

### Maybe have a mechanic where the play chooses how hard to spin the cylinder ###

## round 1 Continue
r1C = 0

while r1C != 1:
    
    revolve(gun)
    revPrint(gun)


    if enemy.takeTurn == True:
        
        print()
        print("He shoots at himself")
        time.sleep(0.5)

        if gun.activeChamber == 1:
            
            fire(gun)
            
            r1C = 1
            
            print("It was a live round, he died")
            break


        else:
            
            fire(gun)
            print("It was an empty chamber")
            time.sleep(0.5)
            
            revolve(gun)
            revPrint(gun)
    
    # skipped enemy turn always if coinFlipV not set to 1
    else:
        enemy.takeTurn = True

    print()
    

    ## PLAYER TURN ##

    while True:
        player.target = input("Shoot yourself or him?\nme\nhim\nanswer: ")
        print()


        if player.target == "me":
            
            if gun.activeChamber == 1:
                fire(gun)
                
                r1C = 1
                
                exit()
                
            else:
                
                time.sleep(0.5)
                
                fire(gun)
                print("It was an empty chamber")
                time.sleep(0.5)
                
                break


        elif player.target == "him":
            
            
            if gun.activeChamber == 1:
                
                fire(gun)
                print("You did it, he's done for")
                
                r1C = 1
                
                break

                
            else:
                
                fire(gun)
                print()
                print("That's not how russian roulette works, he turns the gun to you and pulls the trigger continuously")
                time.sleep(1)
                
                while True:

                    revolve(gun)
                    
                    fire(gun)
                    if gun.activeChamber == 1:
                        
                        r1C = 1
                        
                        # if have trouble later not continue to next round look here
                        exit()



print("You win")
