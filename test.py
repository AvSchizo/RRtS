import Character_Object

player = Character_Object.character()

enemy = Character_Object.character()

def addItem(player, enemy):
    player.itemCount += 1
    enemy.itemCount += 1

print(f"player item count {player.itemCount}")
print(f"enemy item count {enemy.itemCount}")

addItem(player, enemy)

print()
print(f"player item count {player.itemCount}")
print(f"enemy item count {enemy.itemCount}")