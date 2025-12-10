import Gun_Object
from Gun_Object import fire
gun = Gun_Object.gun

import Character_Object
player = Character_Object.player
enemy = Character_Object.enemy

class actionClass:
	usable = True

# ActionVariable_bangGun


class actionContainerClass:
	pass

actionContainer = actionContainerClass()
actionContainer.AV_bangGun = actionClass()
actionContainer.AV_breathe = actionClass()

def resetAction(actionContainer):
	actionContainer.AV_bangGun.usable = True
	actionContainer.AV_breathe.usable = True
	actionContainer.AV_forceLoad.usable = True



def bangGun(actionContainer, gun, player):
	gun.damage *= 2
	actionContainer.AV_bangGun.usable = False

	if gun.cyl[0] == 1:
		fire(gun)
		player.health -= gun.damage


def breathe(actionContainer, gun, player, enemy):
	actionContainer.AV_breathe.usable = False
	player.health += 1
	gun.damage += 1
	enemy.forceTarget = player


def forceLoad(actionContainer, gun, player):
	actionContainer.AV_forceLoad.usable = False
	if gun.cyl[0] == 0:
		gun.cyl[0] = 1
	elif gun.cyl[0] == 1:
		player.target.health -= gun.damage
		player.endTurn = True


