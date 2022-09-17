import random

AIChoice = random.randrange(1, 4)
PlayerChoice = int(input("""
Choose a move
1: Rock
2: Paper
3: Scissors
Your move: """))

if AIChoice == PlayerChoice:
    print("Tie!")
elif AIChoice == 1 and PlayerChoice == 2 or AIChoice == 2 and PlayerChoice == 3 or AIChoice == 3 and PlayerChoice == 1:
    print("You win!")
else:
    print("You lose!")