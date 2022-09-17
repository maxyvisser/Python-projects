import random

DaWay = input("Do you want to input you own number? y or n: ")
if DaWay == "y": Number = int(input("Enter a number: "))
elif DaWay == "n": Number = random.randrange(-pow(2, 31)+1, pow(2, 31)-1)
else: print("Error: you must input y or n")
Counter = 0

print(Counter, Number)

while abs(Number) != 1:
    if Number % 2 == 0:
        Number = int(Number / 2)
    else:
        Number = int(Number * 3)
        if Number > 0:
            Number += 1
        else:
            Number -= 1
    Counter += 1
    print(Counter, Number)