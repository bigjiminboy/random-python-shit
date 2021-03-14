print("\nWelcome to Restricted Rock Paper Scissors\n")
print("RULES:\n 1: You can only use each move 4 times\n 2: Once you\'ve used a move 4 times, you cannot use it again (kind of obvious)\n 3: Unlike AdaptiveRPS, draws will use up moves\n 4: Also unlike Adaptive RPS, there are only 12 rounds per game, no exceptions")
#setting move pools
movePool = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
aiPool = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
round = 0
playerPoints = 0
aiPoints = 0
gameActive = True
#starting game loop
while gameActive == True:
	print ("\n---------------------------------")
	round = round + 1
	if round == 12:
		gameActive = False
	print ("\nRound", round)
#displaying player's options
	print ("\nYou have:\n", movePool.count(1), "Rocks\n", movePool.count(2), "Papers\n", 	movePool.count(3), "Scissors\n")
	cont = False
#player choice check
	while cont == False:
		choice = input ("Rock (1), Paper (2), Scissors (3)\n")
		choice = int(choice)
		for n in movePool:
			if n == choice:
				cont = True
		if cont == False:
			print("Please input a valid number")
	movePool.remove(choice)
#computer choice
	import random
	aiChoice = random.choice(aiPool)
	aiChoice = int(aiChoice)
	aiPool.remove(aiChoice)
#win/loss detection done the boring way
	if choice == 1:
		if aiChoice == 1:
			print ("\nIt\'s a Draw\n")
		if aiChoice == 2:
			print ("\nYou Lost\n")
			aiPoints = aiPoints + 1
		if aiChoice == 3:
			print ("\nYou Won\n")
			playerPoints = playerPoints + 1
	if choice == 2:
		if aiChoice == 1:
			print ("\nYou Won\n")
			playerPoints = playerPoints + 1
		if aiChoice == 2:
			print ("\nIt\'s a Draw\n")
		if aiChoice == 3:
			print ("\nYou Lost\n")
			aiPoints = aiPoints + 1
	if choice == 3:
		if aiChoice == 1:
			print ("\nYou Lost\n")
			aiPoints = aiPoints + 1
		if aiChoice == 2:
			print ("\nYou Won\n")
			playerPoints = playerPoints + 1
		if aiChoice == 3:
			print ("\nIt\'s a Draw\n")
#displaying points funkily	
	if playerPoints > aiPoints:
		print ("You\'re Currently Winning", playerPoints, "to", aiPoints)
	if playerPoints < aiPoints:
		print ("You\'re Currently Losing", aiPoints, "to", playerPoints)
	if playerPoints == aiPoints:
		print ("You\'re Currently Tied", playerPoints, "to", aiPoints)
#endgame messages
print ("\nThe Game Has Now Concluded")
print ("\nFinal Scores:\n Player Points -", playerPoints, "\n Computer Points -", aiPoints)
print ("\nPlease Play Again!")