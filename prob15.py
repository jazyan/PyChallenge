import calendar
import datetime


# years that are 1xx6
candidates = [1000 + i * 100 + j * 10 + 6 for i in range(10) for j in range(10)]
# only keep ones that are leap years and jan 1 is a thursday 
filtered = [y for y in candidates if calendar.isleap(y) and datetime.datetime(y, 1, 1).weekday() == 3]
# not the youngest, second youngest
print(filtered[-2])