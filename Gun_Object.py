import random

class gunClass:
    revolution = 0
    cyl = [0,0,0,0,0]

gun = gunClass()

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
