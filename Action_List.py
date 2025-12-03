import Gun_Object
gun = Gun_Object.gun

import Character_Object
player = Character_Object.player

class actionClass:
    usable = True

# AV stands for ActionVariable
AV_bangGun = actionClass()

def bangGun(AV_bangGun, gun, player):
    gun.reset = True
    gun.damage *= 2
    AV_bangGun = False
    
    if gun.cyl[0] == 1:
        player.health -= gun.damage