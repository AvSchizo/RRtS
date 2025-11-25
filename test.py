class characterClass:
    pass

player = characterClass()
enemy = characterClass()

class itemClass:
    player.value = 0
    enemy.value = 1

item1 = itemClass()
item1.name = "fish"

item2 = itemClass()
item2.name = "chocolate"

item3 = itemClass()
item3.name = "trash"


itemList = [item1, item2, item3]

print(item1.player.value)

for i in range(len(itemList)):
    if itemList[i].enemy.value > 0:
        print(itemList[i].name)