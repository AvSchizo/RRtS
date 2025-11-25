class itemClass():
    pass

item1 = itemClass()
item1.name = "fish"
item1.value = 0

item2 = itemClass()
item2.name = "chocolate"
item2.value = 0

item3 = itemClass()
item3.name = "trash"
item3.value = 0

class characterClass:
    pass

player = characterClass()
# i dunno why but you gotta set them equal to the original items
player.item1 = item1
player.item2 = item2
player.item3 = item3


player.item1.value = 1

def itemListPrint(player):
    itemList = [player.item1, player.item2, player.item3]
    for i in range(len(itemList)):
        if itemList[i].value > 0:
            print(itemList[i].name)
            print(itemList[i].value)
itemListPrint(player)
