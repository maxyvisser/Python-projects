from time import sleep
from os import system

system("cls")



while True:
    system("cls")
    
    for i in range(0, 17):
        if i % 2 == 0: print("+---+---+---+---+---+---+---+---+")
        else: print("|   |   |   |   |   |   |   |   |")
    
    sleep(0.1)

input()

print("Sarah Wuz hier")