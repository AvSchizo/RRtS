import random

class roundClass:
    useItems = False
    cont = False
    maxHealth = 2
    gunDmg = 1

round1 = roundClass()
round2 = roundClass()
round3 = roundClass()

roundI = 0
roundList = [round1, round2, round3]

round1.maxHealth = 2

round2.maxHealth = 4

round3.maxHealth = 6

def currentRoundReset(round):
    round.maxHealth = random.randint(2,6)
    print(f"Max health: {round.maxHealth}")
    round.cont = False
    if random.randint(0,10) == 0:
        print("No item round")
        round.useItems = False
    else:
        round.useItems = True