'''Write a Python program to calculate the number of days between two dates.
Sample dates : (20200702), (20200711)'''

# using datetime module for solution
from datetime import date

def numberofdays(date1, date2):
    # date1,date2 shold be taken as date(year: int, month: int, day: int)
    days = date1-date2
    return days

    
date1 = date(2020, 7, 2)
date2 = date(2020, 7, 11)

print(numberofdays(date1,date2))