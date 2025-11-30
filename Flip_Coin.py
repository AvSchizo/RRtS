import random

# coin flipped
def flipCoin():
    coinFlipV = random.randint(0,1)

    while True:
        print()
        coinFlipWord = input("A coin is flipped\n1] heads\n2] tails\nanswer: ")

        if coinFlipWord == "heads" or coinFlipWord == "tails" or coinFlipWord == "1" or coinFlipWord == "2":
            if coinFlipWord == "heads" or coinFlipWord == "1":
                print("it's heads")
            elif coinFlipWord == "tails" or coinFlipWord == "2":
                print("it's tails")
            break

        print()
        print("Sorry, I don't understand, ")

    return coinFlipV