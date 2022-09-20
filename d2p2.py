
def checkleapyr(year):
    if year%400==0 or year%4==0:
        print(year," is leap year")
    else:
        checkleapyr(year-1)


try:
    yr = int(input("Enter the year: "))
    if yr > 0:
        checkleapyr(yr)
    else:
        print("Year can't be negative...! or Zero...!")
except :
    print("Wrong value")

