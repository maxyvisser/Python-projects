import time

Wait = int(input("Input the wait time in seconds: "))
Time = Wait / 33
Counter = 0
def Even():
    if Counter % 2 == 0:
        return "C+"
    else:
        return "c"

while Counter < 32:
    print("-" * Counter + str(Even()) + " +" * int(((31 - Counter) / 2)))
    Counter += 1
    time.sleep(Time)