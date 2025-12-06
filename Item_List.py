import random

import Character_Object
player = Character_Object.player

import Gun_Object
gun = Gun_Object.gun


class itemClass():
    value = 0

Coffee = itemClass()
Coffee.name = "Coffee"
Coffee.value = 0

Gunpowder = itemClass()
Gunpowder.name = "Gunpowder"
Gunpowder.value = 0

item3 = itemClass()
item3.name = "item3"
item3.value = 0


# i dunno why but you gotta set them equal to the original items
player.Coffee = Coffee
player.Gunpowder = Gunpowder
player.item3 = item3


tutorialItemGiveList = [Coffee, Gunpowder, item3]





def itemListPrint(player):
    itemList = [player.Coffee, player.Gunpowder, player.item3]
    for i in range(len(itemList)):
        if itemList[i].value > 0:
            print(itemList[i].name)
            print(itemList[i].value)


def useCoffee(player, gun):
    # valid amount of item
    if player.Coffee.value > 0:
        player.Coffee.value -= 1
        ind = random.randint(len(gun.cyl), 30)
        gun.cyl = gun.cyl[ind:] + gun.cyl[:ind]
    
    # invalid amount of item
    elif player.Coffee.value <= 0:
        print("nuh uh, no more Coffee")









########## showcase for importing into main file


# import Character_Object
# from Item_List import itemListPrint

# player = Character_Object.player
# itemListPrint(player)


## OR ##


# from Character_Object import player
# from Item_List import itemListPrint

# itemListPrint(player)
