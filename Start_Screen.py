import time
def startScreen():
    cheatsEnabledCheck = " "
    playTutorialCheck = " "
    playTutorial = False
    while True:
        print("Russian Roulette The Sequal")
        time.sleep(0.2)
        print("1] start")
        time.sleep(0.2)
        print("2] exit")
        time.sleep(0.2)
        print(f"3] cheats [{cheatsEnabledCheck}]")
        time.sleep(0.2)
        print(f"4] play tutorial [{playTutorialCheck}]")
        time.sleep(0.2)
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

            if playTutorial == False:
                playTutorial = True
                playTutorialCheck = "+"
                print("tutorial will play")

            elif playTutorial == True:
                playTutorial = False
                playTutorialCheck = " "
                print("tutorial won't play")

            print()
        else:
            print("Sorry, I don't understand,")
            print()
    return playTutorial