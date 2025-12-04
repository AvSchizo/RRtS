import Gun_Object
from Gun_Object import fire
gun = Gun_Object.gun

import Character_Object
player = Character_Object.player

class actionClass:
    usable = True

# ActionVariable_bangGun
AV_bangGun = actionClass()


class actionContainerClass:
    pass

actionContainer = actionContainerClass()
actionContainer.AV_bangGun = AV_bangGun

def resetAction(actionContainer):
    actionContainer.AV_bangGun.usable = True



def bangGun(actionContainer, gun, player):
    gun.reset = True
    gun.damage *= 2
    actionContainer.AV_bangGun.usable = False
    
    if gun.cyl[0] == 1:
        fire(gun)
        player.health -= gun.damage

