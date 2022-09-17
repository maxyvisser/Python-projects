while True:
    Bin = input("Please enter a binary number (consisting of only 1 and 0): ")
    Counter = 0
    Dec = 0

    while Counter < len(Bin):
        Dec += int(Bin[-(Counter + 1)]) * 2 ** Counter
        Counter += 1
        print(Counter, "/", len(Bin))

    print(f"The result is {Dec}!")