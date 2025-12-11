import random
import time

import Flip_Coin

import Gun_Object
from Gun_Object import revolve, fire, revPrint, gunInfo, reloadGun, checkReload

import Character_Object
from Character_Object import printHealth

from Start_Screen import startScreen

import Round_List

from Display_Info import displayInfo

from Action_List import actionContainer, resetAction, bangGun, breathe, forceLoad

#### SET UP OBJECTS ####

# set up gun
gun = Gun_Object.gun

# set up characters
player = Character_Object.player
enemy = Character_Object.enemy

# set up coin flip
def flipCoin():
	coinFlip = Flip_Coin.flipCoin()
	if coinFlip == 1:
		enemy.takeTurn = True
	else:
		enemy.takeTurn = False

#### DEF FUNC ####

def healthDown(char):
	char.health -= gun.damage

def setCharHealth(char1, char2, round):
	char1.health = round.maxHealth
	char2.health = round.maxHealth

def sorryMes():
	print()
	print("Sorry, I don't understand,")
	print()



#########################################################
######################## ROUND 1 ########################
#########################################################

# Round setup
print()
i = Round_List.roundI
print(f"ROUND {(i+1)}")
time.sleep(2)

print()
print()
flipCoin()
currentRound = Round_List.roundList[i]
setCharHealth(player, enemy, currentRound)


while currentRound.cont != True:


	######### ENEMY TURN #########
	##############################
	charTurn = "ENEMY"


	if enemy.takeTurn == True:
		revolve(gun)

		print()
		print()
		displayInfo(charTurn)

		print("He shoots at himself")
		time.sleep(1)

		if gun.activeChamber == 1:
			
			fire(gun)
			time.sleep(0.5)
			healthDown(enemy)
			print("It's a live round")
			
			## ENEMY DIES ##
			if enemy.health == 0:
				currentRound.cont = True
				continue
			


		## EMPTY CHAMBER ##
		else:
			
			fire(gun)
			time.sleep(0.5)
			print("It was an empty chamber")
			
		time.sleep(1)

	# skipped enemy turn always if not set to 1
	else:
		enemy.takeTurn = True

	checkReload(gun, False)

	######### PLAYER TURN #########
	###############################
	# remember to put "if player.takeTurn == True:" and indent

	charTurn = "PLAYER"
	revolve(gun)


	### DISPLAY INFO ###
	print()
	print()
	displayInfo(charTurn)


	while True:
		print("Shoot yourself or him?")
		print("1] me")
		print("2] him")
		player.targetInput = input("answer: ")
		print()



		##### PLAYER TARGET "ME" #####
		if player.targetInput == "me" or player.targetInput == "1":
			player.target = player
			

			## BULLET ##
			if gun.activeChamber == 1:
				
				fire(gun)
				time.sleep(0.5)
				healthDown(player)
				
				## PLAYER DIES ##
				if player.health == 0:
					currentRound.cont = True
					print("player death, exit now")
					exit()
			
			
				


			## EMPTY CHAMBER ##                
			else:
				
				fire(gun)
				time.sleep(0.5)
				print("It was an empty chamber")
				time.sleep(1)

				# player choice to skip enemy turn
				while True:
					
					print()
					print("would you like to skip the enemy's turn?")
					print("1] yes")
					print("2] no")
					hisTurnAgain = input("answer: ")

					if hisTurnAgain == "1" or hisTurnAgain == "yes":
						enemy.takeTurn = False
						# skip enemy turn question break
						break
					elif hisTurnAgain == "2" or hisTurnAgain == "no":
						# skip enemy turn question break
						break
					else:
						sorryMes()
			
			checkReload(gun, False)
			
			# player turn loop break
			break



		##### PLAYER TARGET "HIM" #####
		elif player.targetInput == "him" or player.targetInput == "2":
			player.target = enemy
			
			
			## BULLET ##
			if gun.activeChamber == 1:
				
				fire(gun)
				time.sleep(0.5)
				healthDown(enemy)
				print("It's a live round")
				
				## ENEMY DIES ##
				if enemy.health == 0:
					currentRound.cont = True
				

				

			## EMPTY CHAMBER ##
			else:
				
				fire(gun)
				print("It was an empty chamber")
			
			time.sleep(1)
				
			# player turn loop break
			break
		
						
		else:
			sorryMes()

	checkReload(gun, False)


#########################################################
######################## ACTIONS ########################
#########################################################

print()

while True:

	displayInfo(player)

	print("Options")
	print("1] action")
	player.choiceInput = input("answer: ")


	if player.choiceInput == "1" or player.choiceInput == "action":
		print("Actions:")
		print("1] breathe")
		print("2] bang gun on table")
		print("3] force load the gun")
		player.actionInput = input("answer: ")


		if player.actionInput == "1" or player.actionInput == "breathe":
			breathe(actionContainer, gun, player, enemy)
		
		elif player.actionInput == "2" or "bang gun" in player.actionInput:
			bangGun(actionContainer, gun, player)
		
		elif player.actionInput == "3" or "force load" in  player.actionInput:
			forceLoad(actionContainer, gun, player)


