def startScreen():
    playTutorial = False
    while True:
        print("Russian Roulette The Sequal")
        print("1] start")
        print("2] exit")
        print("3] cheats")
        print("4] play tutorial")
        userStartOption = input("answer: ")
        print()
        if userStartOption == "exit" or userStartOption == "2":
            exit()
        elif userStartOption == "start" or userStartOption == "1":
            print("Oh, that's-a baseball")
            break
        elif userStartOption == "cheats" or userStartOption == "3":
            print("Sorry, feature not in game yet, stay tuned")
            print()
        elif userStartOption == "tutorial" or userStartOption == "4":
            playTutorial = True
            print("tutorial will play")
            print()
        else:
            print("Sorry, I don't understand,")
            print()
    return playTutorial