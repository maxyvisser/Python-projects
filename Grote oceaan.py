import matplotlib.pyplot as plt
from math import sqrt
from time import time
import numpy as np

start_time = time.time()

water = 4985200000000
Counter = 0
xcords = []
ycords = []

xcords.append(Counter)
ycords.append(water)

while water > 0:
    Uitstroom = 0.04*sqrt(water)
    water -= Uitstroom
    Counter += 1
    if Counter % 1000000 == 0:
        print(Counter)
        xcords.append(Counter)
        ycords.append(water)

xcords.append(Counter)
ycords.append(water)

plt.plot(xcords, ycords)

end_time = time.time()
print(f"Done in {end_time-start_time} seconds!")