def startScreen():
    while True:
        userStartOption = input("Russian Roulette The Sequal\n1]start\n2]exit\n3]cheats\nanswer: ")
        if userStartOption == "exit" or userStartOption == "2":
            exit()
        elif userStartOption == "start" or userStartOption == "1":
            print()
            print("Oh, that's-a baseball")
            break
        elif userStartOption == "cheats" or userStartOption == "3":
            print()
            print("Sorry, feature not in game yet, stay tuned")
            print()
        else:
            print()
            print("Sorry, I don't understand,")
            print()