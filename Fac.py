from time import time

while True:
    word = input("Please input a number: ")
    try: inp = int(word)
    except:
        print("A NUMBER")
        continue
    
    stepword = input("Please enter the amount of !'s: ")
    try: step = int(stepword)
    except:
        print("Enter a number")
        continue
    
    start = time()
    out = 1
    for i in range(inp, 0, -step):
        out *= i
        print(f"{i}/{inp}")
    
    outword = str(out)
    
    if len(outword) > 10: print(f"{outword[0]}.{outword[1:10]}*10^{len(outword)-1}")
    else: print(out)
    
    end = time()
    
    print(f"Finished in {end - start} seconds.")
    
    input("Press enter to try again.")