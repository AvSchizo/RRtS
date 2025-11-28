class character:
    health = 1
    takeTurn = True

player = character()
player.name = "player"

enemy = character()
enemy.name = "enemy"

def printHealth(char):
    print(f"{char.name} health: {char.health}")
