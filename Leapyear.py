while True:
    year = int(input("Enter a year: "))

    leap = 1
    if year % 4 == 0: leap = 0
    if year % 100 == 0: leap = 1
    if year % 400 == 0: leap = 0

    print(year, "is", "NOT" * leap, "a leapyear!")