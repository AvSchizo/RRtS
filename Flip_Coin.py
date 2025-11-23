import random

# coin flipped
def flipCoin():
    coinFlipV = random.randint(0,1)

    while True:
        coinFlipWord = input("A coin is flipped\nheads\ntails\nanswer: ")

        if coinFlipWord == "heads" or coinFlipWord == "tails":
            break

        print()
        print("Sorry, I don't understand, ")

    return coinFlipV
