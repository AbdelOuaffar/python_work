def LeapYear(year):
    if year % 400 == 0 or year % 100 == 0 or year % 4 == 0:
        print(year, True)
    else :
        print(year, False)
year = int(input("Enter a year  :"))
Answer = LeapYear(year)