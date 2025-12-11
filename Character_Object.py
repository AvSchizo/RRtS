class character:
    health = 1
    takeTurn = True
    target = None
    forceTakeTurn = None
    forceTarget = None
    endTurn = False
    choiceInput = None
    actionInput = None

player = character()
player.name = "player"

enemy = character()
enemy.name = "enemy"


def resetChar(char):
    char.forceTakeTurn = None
    char.forceTarget = None
    char.endTurn = False


def printHealth(char):
    print(f"{char.name} health: {char.health}")
