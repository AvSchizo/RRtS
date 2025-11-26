def startScreen():
    while True:
        userStartOption = input("Russian Roulette The Sequal\n|start\n|exit\n|cheats\nanswer: ")
        if userStartOption == "exit":
            exit()
        elif userStartOption == "start":
            print()
            print("Oh, that's-a baseball")
            print()
            break
        elif userStartOption == "cheats":
            print()
            print("Sorry, feature not in game yet, stay tuned")
            print()
        else:
            print()
            print("Sorry, I don't understand")
            print()
    
    print("Game has started : test")
