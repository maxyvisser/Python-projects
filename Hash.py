nums = {
"a" : "01",
"b" : "02",
"c" : "03",
"d" : "04",
"e" : "05",
"f" : "06",
"g" : "07",
"h" : "08",
"i" : "09",
"j" : "10",
"k" : "11",
"l" : "12",
"m" : "13",
"n" : "14",
"o" : "15",
"p" : "16",
"q" : "17",
"r" : "18",
"s" : "19",
"t" : "20",
"u" : "21",
"v" : "22",
"w" : "23",
"x" : "24",
"y" : "25",
"z" : "26"}

inWord = input("Please input something: ")
outWord = ""

if not inWord:
    print("Error: please input something!")

try: outWord = int(inWord)
except:
    try: outWord = float(inWord)
    except:
        inWord
        for i in inWord:
            try: outWord += nums[i]
            except: outWord += i

outWord = str(outWord)

print(outWord)

length = len(outWord) + 5

try: Hash = int(outWord)
except: Hash = float(outWord)

for i in range(0, 5):
    Hash = str(int(Hash) ** 3)
    if len(Hash) > length:
        Hash = Hash[:length]
        
print(Hash)