import random

# coin flipped
def flipCoin():
    coinFlipV = random.randint(0,1)

    coinFlipW = input("A coin is flipped\nheads\ntails\n")

    if coinFlipW == "heads" or coinFlipW == "tails":

        if coinFlipW == "heads":
            pass

        elif coinFlipW == "tails":
            pass

    else:
        coinFlipLoop = 0
        
        while coinFlipLoop != 1:
            print("Sorry, I don't understand,")
            
            coinFlipW = input("A coin is flipped\nheads\ntails\n")
            
            if coinFlipW == "heads" or coinFlipW == "tails":
                coinFlipLoop = 1

    return coinFlipV
