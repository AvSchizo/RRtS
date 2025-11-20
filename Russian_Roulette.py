import random
import time


revolution = 0
Cyl = [0,0,0,0,0]


#load
ind = random.randint(1,5)
bulletChamber = ind % 5
Cyl[bulletChamber] = 1


activeChamber = Cyl[0]


def revolve():
   global Cyl, bulletChamber, activeChamber, revolution
   Cyl = Cyl[1:] + Cyl[:1]
   if bulletChamber == 0:
       bulletChamber = (len(Cyl)) - 1
   else:
       bulletChamber -= 1
   activeChamber = Cyl[0]
   revolution += 1


def Fire():
    global activeChamber
    if activeChamber == 1:
        print("BANG")
    else:
        print("click")


##############################

coinFlip = input("A coin is flipped\nheads\ntails\n")
if coinFlip == "heads" or coinFlip == "tails":
    if coinFlip == "heads":
        coinFlipV = 0
    elif coinFlip == "tails":
        coinFlipV = 1
else:
    coinFlipLoop = 0
    while coinFlipLoop != 1:
        print("Sorry, I don't understand,")
        coinFlip = input("A coin is flipped\nheads\ntails\n")
        if coinFlip == "heads" or coinFlip == "tails":
            coinFlipLoop = 1

### Maybe have a mechanic where the play chooses how hard to spin the cylinder ###
r1c = 0
while r1c != 1:
    revolve()
    print()
    print(f"REVOLUTION {(revolution)}")
    time.sleep(1)


    print()

    if coinFlip == 1:
        print()
        print("He shoots")
        time.sleep(0.5)
        if activeChamber == 1:
            Fire()
            r1c = 1
            Continue = 1
            print("It was a live round, he died")
            exit()


        else:
            Fire()
            print("It was an empty chamber")
            time.sleep(0.5)
            revolve()
            print()
            print(f"REVOLUTION {(revolution)}")
            time.sleep(1)


    print()

    ################################NO ITEMS ################################
    
    Continue = 0
    while Continue != 1:
        Target = input("Shoot yourself or him?\n\"me\"\n\"him\"\n")
        print()


        if Target == "me":
            if activeChamber == 1:
                Fire()
                exit()
            else:
                time.sleep(0.5)
                Fire()
                print("It was a blank round")
                time.sleep(0.5)
                Continue = 1


        elif Target == "him":
            if activeChamber == 1:
                Fire()
                print("You did it, he's done for")
                r1c = 1
                Continue = 1
            else:
                Fire()
                print()
                print("Ooh, that's now how the game's played, they turn the gun to you and pull the trigger continuously")
                time.sleep(1)
                while True:
                    Fire()
                    if activeChamber == 1:
                        exit()
                    revolve()


print("You win")
print("or did you?????")

