import random

class gunClass:
    revolution = 0
    cyl = [0,0,0,0,0]

gun = gunClass()

gun.bulletChamber = random.randint(1,5) % 5
gun.cyl[gun.bulletChamber] = 1
gun.activeChamber = gun.cyl[0]
