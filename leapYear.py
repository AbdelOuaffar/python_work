def leapYear(year):
    if year  % 400 == 0 or year % 100 == 0 or year %  4 == 0 :
        print(year," is a leap year")
    else :
        print( year," : is not a leap year")
year = int(input(" enter a year  :"))
leapYear(year)




