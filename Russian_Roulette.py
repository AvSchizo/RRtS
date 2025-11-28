import random
import time

import Flip_Coin

import Gun_Object
from Gun_Object import revolve, fire, revPrint, gunInfo

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
def flipCoin(enemy):
    coinFlip = Flip_Coin.flipCoin()
    if coinFlip == 1:
        enemy.takeTurn = True
    else:
        enemy.takeTurn = False

#### DEF FUNC ####

def healthDown(char, gun):
    char.health -= gun.damage

def setCharHealth(char1, char2, round):
    char1.health = round.maxHealth
    char2.health = round.maxHealth



################## START SCREEN ##################
startScreen()
##################################################

### Maybe have a mechanic where the play chooses how hard to spin the cylinder ###

# Round setup 1
flipCoin(enemy)
i = Round_List.i
currentRound = Round_List.roundList[i]
setCharHealth(player, enemy, currentRound)

print(f"ROUND {(i + 1)}")

while currentRound.cont != True:
    
    revolve(gun)
    displayInfo(player, enemy, gun)
    time.sleep(1)

    ## ENEMY TURN ##
    if enemy.takeTurn == True:
        
        print("He shoots at himself")
        time.sleep(0.5)

        ## BULLET ##
        if gun.activeChamber == 1:
            
            fire(gun)
            healthDown(enemy, gun)
            printHealth(enemy)

            if enemy.health == 0:
                currentRound.cont = True
                print("he dead")
            
            print("It was a live round")
            break


        ## EMPTY CHAMBER ##
        else:
            
            fire(gun)
            print("It was an empty chamber")
            time.sleep(0.5)
            
            revolve(gun)
    
    # skipped enemy turn always if not set to 1
    else:
        enemy.takeTurn = True


    print()
    

    ## PLAYER TURN ##


    ### DISPLAY INFO ###
    displayInfo(player, enemy, gun)


    while True:
        player.target = input("Shoot yourself or him?\n1]me\n2]him\nanswer: ")
        print()


        ##### PLAYER TARGET "ME" #####
        if player.target == "me" or player.target == "1":
            

            ## BULLET ##
            if gun.activeChamber == 1:
                
                fire(gun)
                healthDown(player, gun)
                printHealth(player)
                
                ## PLAYER DIES ##
                if player.health == 0:
                    currentRound.cont = True
                    exit()
                

            ## EMPTY CHAMBER ##                
            else:
                
                fire(gun)
                print("It was an empty chamber")
                time.sleep(1)
                
                break


        ##### PLAYER TARGET "HIM" #####
        elif player.target == "him" or player.target == "2":
            
            ## BULLET ##
            if gun.activeChamber == 1:
                
                fire(gun)
                healthDown(enemy, gun)
                print("It's a live round")
                printHealth(enemy)
                
                ## ENEMY DIES ##
                if enemy.health == 0:
                    currentRound.cont = True
                
                break

            ## EMPTY CHAMBER ##
            else:
                
                fire(gun)
                print("It was an empty chamber")
                time.sleep(1)
                
                break
                        
        else:
            print("Sorry, I don't understand")


##########################################################


# Round setup
flipCoin(enemy)
i += 1
currentRound = Round_List.roundList[i]
setCharHealth(player, enemy, currentRound)

print(f"ROUND {(i + 1)}")

while currentRound.cont != True:
    
    revolve(gun)
    displayInfo(player, enemy, gun)
    time.sleep(1)

    ## ENEMY TURN ##
    if enemy.takeTurn == True:
        
        print()
        print("He shoots at himself")
        time.sleep(0.5)

        ## BULLET ##
        if gun.activeChamber == 1:
            
            fire(gun)
            healthDown(enemy, gun)
            printHealth(enemy)

            if enemy.health == 0:
                currentRound.cont = True
            
            print("It was a live round")
            break


        ## EMPTY CHAMBER ##
        else:
            
            fire(gun)
            print("It was an empty chamber")
            time.sleep(0.5)
            
            revolve(gun)
            revPrint(gun)
    
    # skipped enemy turn always if not set to 1
    else:
        enemy.takeTurn = True


    print()
    

    ## PLAYER TURN ##


    ### DISPLAY INFO ###
    


    while True:
        player.target = input("Shoot yourself or him?\n1]me\n2]him\nanswer: ")
        print()


        ##### PLAYER TARGET "ME" #####
        if player.target == "me" or player.target == "1":
            

            ## BULLET ##
            if gun.activeChamber == 1:
                
                fire(gun)
                healthDown(player, gun)
                printHealth(player)
                
                ## PLAYER DIES ##
                if player.health == 0:
                    currentRound.cont = True
                    exit()
                

            ## EMPTY CHAMBER ##                
            else:
                

                fire(gun)
                print("It was an empty chamber")
                time.sleep(1)
                
                break


        ##### PLAYER TARGET "HIM" #####
        elif player.target == "him" or player.target == "2":
            
            ## BULLET ##
            if gun.activeChamber == 1:
                
                fire(gun)
                healthDown(enemy, gun)
                print("It's a live round")
                printHealth(enemy)
                
                ## ENEMY DIES ##
                if enemy.health == 0:
                    currentRound.cont = True
                
                break

            ## EMPTY CHAMBER ##
            else:
                
                fire(gun)
                print()
                print("That's not how russian roulette works, he turns the gun to you and pulls the trigger continuously")
                time.sleep(1)
                
                while True:

                    revolve(gun)
                    
                    fire(gun)
                    if gun.activeChamber == 1:
                        
                        healthDown(player, gun)
                        printHealth(player)

                        if player.health == 0:
                            currentRound.cont = True
                        
                        break
                
                break
        
        else:
            print("Sorry, I don't understand")