while True:
    Dec = int(input("Please enter an integer greater than 0: "))
    eDec = Dec
    Counter = 0
    Counter2 = 0

    while Counter2 <= Dec:
        Counter += 1
        Counter2 = 2 ** Counter

    Counter -= 1
    Counter2 = 2 ** Counter
    eDec -= Counter2
    Bin = "1"

    while Counter > 0:
        Counter -= 1
        Counter2 = 2 ** Counter
        if Counter2 <= eDec:
            eDec -= Counter2
            Bin += "1"
        else:
            Bin += "0"
    print(Bin)