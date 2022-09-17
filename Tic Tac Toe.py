row1 = row3 = row5 = row7 = "+---+---+---+"
row21 = row22 = row23 = row41 = row42 = row43 = row61 = row62 = row63 = " "

turn = 1
endgame = 0
#alternates between X and O
def symbol():
    if turn % 2 == 0:
        return "O"
    else:
        return "X"
#prints the board at the start of the game
print(row1)
print("|", row21, "|", row22, "|", row23, "|")
print(row3)
print("|", row41, "|", row42, "|", row43, "|")
print(row5)
print("|", row61, "|", row62, "|", row63, "|")
print(row7)
#Loops to make multiple turns possible
while endgame != 1:
    print("Turn", turn)
    choise = "E"
    choose = input("Pick a cell (1-9): ")
#checks if the choise is a number
    try: choise = int(choose)
    except: 
        print("Error: please enter a NUMBER between 1 and 9")
        turn -= 1
#checks if the chosen cell is already occupied, and occupies it if it wasn't already
    if choise != "E":
        if choise == 7:
            if row21 != " ": 
                print("Error: already picked")
                turn -= 1
            else: row21 = symbol()
        elif choise == 8:
            if row22 != " ": 
                print("Error: already picked")
                turn -= 1
            else: row22 = symbol()
        elif choise == 9:
            if row23 != " ": 
                print("Error: already picked")
                turn -= 1
            else: row23 = symbol()
        elif choise == 4:
            if row41 != " ": 
                print("Error: already picked")
                turn -= 1
            else: row41 = symbol()
        elif choise == 5:
            if row42 != " ": 
                print("Error: already picked")
                turn -= 1
            else: row42 = symbol()
        elif choise == 6:
            if row43 != " ": 
                print("Error: already picked")
                turn -= 1
            else: row43 = symbol()
        elif choise == 1:
            if row61 != " ": 
                print("Error: already picked")
                turn -= 1
            else: row61 = symbol()
        elif choise == 2:
            if row62 != " ": 
                print("Error: already picked")
                turn -= 1
            else: row62 = symbol()
        elif choise == 3:
            if row63 != " ":
                print("Error: already picked")
                turn -= 1
            else: row63 = symbol()
        else: 
            turn -= 1
            print("Error: please enter a number BETWEEN 1 AND 9")
#checks if one of the players won this turn, and ends the game if one did or if there's a tie
    if row21 == row22 == row23 != " ":
        print("Player", symbol(), "won in", turn, "Turns!")
        endgame = 1
    elif row41 == row42 == row43 != " ":
        print("Player", symbol(), "won in", turn, "Turns!")
        endgame = 1
    elif row61 == row62 == row63 != " ":
        print("Player", symbol(), "won in", turn, "Turns!")
        endgame = 1
    elif row21 == row41 == row61 != " ":
        print("Player", symbol(), "won in", turn, "Turns!")
        endgame = 1
    elif row22 == row42 == row62 != " ":
        print("Player", symbol(), "won in", turn, "Turns!")
        endgame = 1
    elif row23 == row43 == row63 != " ":
        print("Player", symbol(), "won in", turn, "Turns!")
        endgame = 1
    elif row21 == row42 == row63 != " ":
        print("Player", symbol(), "won in", turn, "Turns!")
        endgame = 1
    elif row23 == row42 == row61 != " ":
        print("Player", symbol(), "won in", turn, "Turns!")
        endgame = 1
    elif turn == 9:
        endgame = 1
        print("Tie!")
#prints the acutal board
    print(row1)
    print("|", row21, "|", row22, "|", row23, "|")
    print(row3)
    print("|", row41, "|", row42, "|", row43, "|")
    print(row5)
    print("|", row61, "|", row62, "|", row63, "|")
    print(row7)

    turn += 1