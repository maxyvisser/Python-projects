from math import sqrt
from time import time

while True:
    Number = int(input("Input a number: "))
    Root = int(sqrt(Number))
    Divider = 2
    Prime = 0

    start = time()

    while Divider <= Root:
        print(f"Checked {Divider}/{Root}")
        if Number % Divider == 0:
            Prime = 1
            break
        else:
            Divider += 1

    end = time()

    print(f"{Number}is{' NOT' * Prime} a prime!")
    print(f"Finished in {end - start} seconds")
