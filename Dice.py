import random

list = {
1: """|     |
|  x  |
|     |""",
2: """|x    |
|     |
|    x|""",
3: """|x    |
|  x  |
|    x|""",
4: """|x   x|
|     |
|x   x|""",
5: """|x   x|
|  x  |
|x   x|""",
6: """|x   x|
|x   x|
|x   x|"""}

while True:
    Dice = random.randrange(1, 7)
    print("+-----+")
    print(list[Dice])
    print("+-----+")
    input("Press enter to reroll")