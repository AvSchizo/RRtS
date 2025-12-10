class character:
    health = 1
    takeTurn = True
    target = None
    forceTakeTurn = None
    forceTarget = None

player = character()
player.name = "player"

enemy = character()
enemy.name = "enemy"


def resetChar(char):
    char.forceTakeTurn = None
    char.forceTarget = None


def printHealth(char):
    print(f"{char.name} health: {char.health}")
