# try camel case

import random
import time
import Flip_Coin

class gunClass:
    revolution = 0
    cyl = [0,0,0,0,0]

gun = gunClass()


## load

gun.bulletChamber = random.randint(1,5) % 5
gun.cyl[gun.bulletChamber] = 1

gun.activeChamber = gun.cyl[0]


def revolve(gun):
    gun.cyl = gun.cyl[1:] + gun.cyl[:1]
    if gun.bulletChamber == 0:
       gun.bulletChamber = (len(gun.cyl)) - 1
    else:
       gun.bulletChamber -= 1
    gun.activeChamber = gun.cyl[0]
    gun.revolution += 1


def fire(gun):
    if gun.activeChamber == 1:
        print("BANG")
    else:
        print("click")

def gunInfo(gun):
    print(f"CYLINDER {gun.cyl}")
    print(f"EASY BC : {(gun.bulletChamber + 1)}")
    print(f"RAW BULLETCHAMBER : {gun.bulletChamber}")
    print()

def revPrint(gun):
    print()
    print(f"REVOLUTION {gun.revolution}")


##############################

## Flip_Coin.py coin flip
coinFlipV = Flip_Coin.flipCoin()

### Maybe have a mechanic where the play chooses how hard to spin the cylinder ###

## round 1 Continue
r1C = 0

while r1C != 1:
    
    revolve(gun)
    revPrint(gun)
    time.sleep(1)


    if coinFlipV == 1:
        
        print()
        print("He shoots")
        time.sleep(0.5)
        if gun.activeChamber == 1:
            
            fire(gun)
            
            r1c = 1
            Continue = 1
            
            print("It was a live round, he died")
            # if have trouble later not continue to next round look here
            exit()


        else:
            
            fire(gun)
            print("It was an empty chamber")
            time.sleep(0.5)
            
            revolve(gun)
            revPrint(gun)
            time.sleep(1)
    
    # skipped E turn always if coinFlipV not set to 1
    else:
        coinFlipV = 1

    print()

    ################################ NO ITEMS ################################
    
    # I don't like 
    Continue = 0
    while Continue != 1:
        Target = input("Shoot yourself or him?\n\"me\"\n\"him\"\n")
        print()


        if Target == "me":
            
            if gun.activeChamber == 1:
                fire(gun)
                
                r1c = 1
                Continue = 1
                
                exit()
                
            else:
                
                time.sleep(0.5)
                
                fire(gun)
                print("It was a blank round")
                time.sleep(0.5)
                
                Continue = 1


        elif Target == "him":
            
            if gun.activeChamber == 1:
                
                fire(gun)
                print("You did it, he's done for")
                
                r1c = 1
                Continue = 1
                # if have trouble later not continue to next round look here
                exit()
                
            else:
                
                fire(gun)
                print()
                print("Ooh, that's now how the game's played, they turn the gun to you and pull the trigger continuously")
                time.sleep(1)
                
                while True:
                    
                    fire(gun)
                    if gun.activeChamber == 1:
                        exit()
                    
                    revolve(gun)


print("You win")
