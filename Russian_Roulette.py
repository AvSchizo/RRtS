# try camel case for variables and functions
# try pascal case for objects

import random
import time


revolution = 0
cyl = [0,0,0,0,0]


## load

bulletChamber = random.randint(1,5) % 5
cyl[bulletChamber] = 1


activeChamber = cyl[0]


def revolve():
   global cyl, bulletChamber, activeChamber, revolution
   cyl = cyl[1:] + cyl[:1]
   if bulletChamber == 0:
       bulletChamber = (len(cyl)) - 1
   else:
       bulletChamber -= 1
   activeChamber = cyl[0]
   revolution += 1


def fire():
    global activeChamber
    if activeChamber == 1:
        print("BANG")
    else:
        print("click")


##############################

coinFlipW = input("A coin is flipped\nheads\ntails\n")

if coinFlipW == "heads" or coinFlipW == "tails":

    if coinFlipW == "heads":
        coinFlipV = 0

    elif coinFlipW == "tails":
        coinFlipV = 1

else:
    coinFlipLoop = 0
    
    while coinFlipLoop != 1:
        print("Sorry, I don't understand,")
        
        coinFlipW = input("A coin is flipped\nheads\ntails\n")
        
        if coinFlipW == "heads" or coinFlipW == "tails":
            coinFlipLoop = 1

### Maybe have a mechanic where the play chooses how hard to spin the cylinder ###

## round 1 Continue
r1C = 0
while r1C != 1:
    revolve()
    print()
    print(f"REVOLUTION {(revolution)}")
    time.sleep(1)


    print()

    if coinFlipV == 1:
        print()
        print("He shoots")
        time.sleep(0.5)
        if activeChamber == 1:
            fire()
            r1c = 1
            Continue = 1
            print("It was a live round, he died")
            exit()


        else:
            fire()
            print("It was an empty chamber")
            time.sleep(0.5)
            revolve()
            print()
            print(f"REVOLUTION {(revolution)}")
            time.sleep(1)
    
    # skipped E turn always if coinFlipV not set to one
    else:
        coinFlipV = 1

    print()

    ################################NO ITEMS ################################
    
    # I don't like 
    Continue = 0
    while Continue != 1:
        Target = input("Shoot yourself or him?\n\"me\"\n\"him\"\n")
        print()


        if Target == "me":
            if activeChamber == 1:
                fire()
                exit()
            else:
                time.sleep(0.5)
                fire()
                print("It was a blank round")
                time.sleep(0.5)
                Continue = 1


        elif Target == "him":
            if activeChamber == 1:
                fire()
                print("You did it, he's done for")
                r1c = 1
                Continue = 1
            else:
                fire()
                print()
                print("Ooh, that's now how the game's played, they turn the gun to you and pull the trigger continuously")
                time.sleep(1)
                while True:
                    fire()
                    if activeChamber == 1:
                        exit()
                    revolve()


print("You win")
