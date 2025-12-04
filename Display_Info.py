import time
import Character_Object
from Character_Object import printHealth
player = Character_Object.player
enemy = Character_Object.enemy

import Gun_Object
gun = Gun_Object.gun

from Item_List import itemListPrint


def displayInfo(char):
    Gun_Object.revPrint(gun)
    time.sleep(1)
    print()
    print(f"{char} TURN")
    time.sleep(1)
    print()
    printHealth(player)
    time.sleep(1)
    printHealth(enemy)
    time.sleep(1)
    print()