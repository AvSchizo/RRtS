import Gun_Object
from Gun_Object import fire
gun = Gun_Object.gun

import Character_Object
player = Character_Object.player
enemy = Character_Object.enemy

class actionClass:
    usable = True

# ActionVariable_bangGun
AV_bangGun = actionClass()
AV_breathe = actionClass()


class actionContainerClass:
    pass

actionContainer = actionContainerClass()
actionContainer.AV_bangGun = AV_bangGun
actionContainer.AV_breathe = AV_breathe

def resetAction(actionContainer):
    actionContainer.AV_bangGun.usable = True



def bangGun(actionContainer, gun, player):
    gun.reset = True
    gun.damage *= 2
    actionContainer.AV_bangGun.usable = False
    
    if gun.cyl[0] == 1:
        fire(gun)
        player.health -= gun.damage


def breathe(actionContainer, gun, player, enemy):
    player.health += 1
