while True:
    date = input("Please enter a date (dd/mm/yyyy): ")

    months = {
        "01": 0,
        "02": 3,
        "03": 3,
        "04": 6,
        "05": 1,
        "06": 4,
        "07": 6,
        "08": 2,
        "09": 5,
        "10": 0,
        "11": 3,
        "12": 5,}

    day = date[:2]
    month = date[3:5]
    year = date[6:10]

    def century():
        return ((int(year[:2]) % 4) * 5) % 7
  
    leap = 0
    if year % 4 == 0: leap = -1
    if year % 100 == 0: leap = 0
    if year % 400 == 0: leap = -1

    step1 = (int(day) + months[month]) % 7

    step2 = (int(year[2:]) % 28) + (int(int(year[2:]) / 4)) + leap

    step3 = (step2 + century() + step1) % 7

    result = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"}

    print(result[step3])