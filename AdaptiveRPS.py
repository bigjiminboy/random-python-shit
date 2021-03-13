#Introduction to the game
print ("Welcome to spicy Rock Paper Scissors!")
long = input("How many rounds would you like the game to be?(must be an integer)\n")
long = int(long)
rounds = 0
x_pt = 0
y_pt = 0
z = [1, 2, 3]
#Bigboi gameplay loop
while rounds != long:
#Lookin for player input
    print("\nRound", rounds + 1, "of", long)
    x = input("Rock (1), Paper (2) or Scissors (3)?\n")
    x = int(x)
#Computer input
    import random
    y = random.choice(z)
#Adaptive rock, paper, scissors technology jargon
    if x == 1:
        z.append (2)
    if x == 2:
        z.append (3)
    if x == 3:
        z.append (1)
#Figuring out who wins
    if x == 1:
        if y == 1:
            print("It\'s a Tie!\n")
        if y == 2:
            print("You Lost!\n")
            y_pt = y_pt + 1
        if y == 3:
            print("You Won!\n")
            x_pt = x_pt + 1
    if x == 2:
        if y == 1:
            print("You Won!\n")
            x_pt = x_pt + 1
        if y == 2:
            print("It\'s a Tie!\n")
        if y == 3:
            print("You Lost!\n")
            y_pt = y_pt + 1
    if x == 3:
        if y == 1:
            print("You Lost!\n")
            y_pt = y_pt + 1
        if y == 2:
            print("You Won!\n")
            x_pt = x_pt + 1
        if y == 3:
            print("It\'s a Tie\n")
#Figuring out if the player inputs something wrong
    if x > 3 or x < 1:
        print("You done goofed up!\n")
        break
#Printing out who wins (also changing the rounds)
    if x != y:
        rounds = rounds + 1
    print("Player Points =", x_pt)
    print("Computer Points =", y_pt)
print("Game is Over!")
if x > 3 or x < 1:
    print("Please input the right number next time")
else:
    if x_pt > y_pt:
        print("You Won!")
    if x_pt < y_pt:
        print("You Lost!")
    if x_pt == y_pt:
        print("It was a Tie!")
