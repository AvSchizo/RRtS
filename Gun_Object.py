import random
import time
import Round_List
from Round_List import roundList, roundI

class gunClass:
    revolution = 0
    cyl = [0,0,0,0,0,0]
    damage = 1
    reset = True

gun = gunClass()
gun.startCyl = gun.cyl

ind = random.randint(1,(len(gun.cyl)))
gun.bulletChamber = ind % (len(gun.cyl))
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
    print(f"REVOLUTION {gun.revolution}")
    time.sleep(1.5)


def loadGun(gun):
    ind = random.randint(1,(len(gun.cyl))) % (len(gun.cyl))
    if gun.cyl[ind] == 0:
        gun.cyl[ind] = 1

# doesn't check for bullet already in the chamber
def altLoadGun(gun):
    gun.cyl[random.randint(1,(len(gun.cyl))) % (len(gun.cyl))] = 1

    
def reloadGun(gun, bool1, bool2):
    print()
    print("RELOADED")
    time.sleep(1.5)
    gun.cyl = gun.startCyl
    loadGun(gun)
    gun.activeChamber = gun.cyl[0]

    if bool1 == True:
        gun.revolution = 0
    
    if bool2 == True:
        revolve(gun)
    

def checkReload(gun, bool2):
    # either >= and have revolve after check, or > and have revolve before check
    if gun.revolution >= len(gun.cyl):
        reloadGun(gun, True, bool2)


def checkGunReset(gun):
    if gun.reset == True:
        gun.damage = 1

