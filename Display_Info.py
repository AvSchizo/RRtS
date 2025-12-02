import Character_Object
from Character_Object import printHealth
player = Character_Object.player
enemy = Character_Object.enemy

import Gun_Object
gun = Gun_Object.gun

from Item_List import itemListPrint


def displayInfo(player, enemy, gun, char):
    Gun_Object.revPrint(gun)
    print()
    print(f"{char} TURN")
    print()
    printHealth(player)
    printHealth(enemy)
    print()