import random

import Character_Object
player = Character_Object.player

import Gun_Object
gun = Gun_Object.gun


class itemClass():
    value = 0

coffee = itemClass()
coffee.name = "Coffee"
coffee.value = 0

gunpowder = itemClass()
gunpowder.name = "Gunpowder"
gunpowder.value = 0

item3 = itemClass()
item3.name = "item3"
item3.value = 0


# i dunno why but you gotta set them equal to the original items
player.coffee = coffee
player.gunpowder = gunpowder
player.item3 = item3


def itemListPrint(player):
    itemList = [player.coffee, player.gunpowder, player.item3]
    for i in range(len(itemList)):
        if itemList[i].value > 0:
            print(itemList[i].name)
            print(itemList[i].value)


def useCoffee(player, gun):
    if player.coffee.value > 0:
        player.coffee.value -= 1
        ind = random.randint(len(gun.cyl), 30)
        gun.cyl = gun.cyl[ind:] + gun.cyl[:ind]
    elif player.coffee.value <= 0:
        print("nuh uh, no more coffee")









########## showcase for importing into main file


# import Character_Object
# from Item_List import itemListPrint

# player = Character_Object.player
# itemListPrint(player)


## OR ##


# from Character_Object import player
# from Item_List import itemListPrint

# itemListPrint(player)
