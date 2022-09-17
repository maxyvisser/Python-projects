import time

start = time.time()

Number1 = Number2 = 0
Number3 = Counter = 1

Limit = int(input("Enter a limit: "))

print(Counter, Number3)

while Counter < Limit:
    Number1 = Number2
    Number2 = Number3
    Number3 = Number1 + Number2
    Counter += 1
#    print(Counter, Number3)

end = time.time()

#print("Done!")
print(f"Calculated {Number3} in {end - start} seconds!")