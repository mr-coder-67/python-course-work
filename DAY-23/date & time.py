# Date and time examples using Python's datetime module.
# This script shows how to get the current date, validate fixed dates and times,
# read individual date/time parts, format output, and work with time differences.

from datetime import date

t = date.today()
print(t)  # expected output: today's date, e.g. 2026-06-24
print("Year:", t.year)  # expected output: current year, e.g. 2026
print("month:", t.month)  # expected output: current month number, e.g. 6
print("Day:", t.day)  # expected output: current day number, e.g. 24
print("weekday from 0:", t.weekday())
# weekday() returns 0 for Monday through 6 for Sunday.
print("weekday from 1:", t.isoweekday())
# isoweekday() returns 1 for Monday through 7 for Sunday.


# date() lets you create and validate a specific calendar date.
from datetime import date

t = date(2010, 10, 14)
print(t)  # expected output: 2010-10-14


# time() lets you create a valid time value.
from datetime import time

t = time(23, 59, 0)
print(t)  # expected output: 23:59:00


# datetime.now() gives the current date and time.
from datetime import date, time, datetime
n = datetime.now()
print(n)  # expected output: current date and time, e.g. 2026-06-24 14:30:15.123456
print("Year:", n.year)
print("month:", n.month)
print("Day:", n.day)
print("Hour:", n.hour)
print("minute:", n.minute)
print("Second:", n.second)


# formatting date and time strings with strftime.
from datetime import date, time, datetime
n = datetime.now()
print(n.strftime('%d/%m/%y'))
# expected output: day/month/year, e.g. 24/06/26
print(n.strftime('%d/%m/%y %H:%M:%S'))
# expected output: 24/06/26 14:30:15
print(n.strftime('%d/%m/%y %I:%H:%M:%S %p'))
# expected output: 24/06/26 02:30:15 PM
print(n.strftime('%d %b %y %I:%M:%S %p'))
# expected output: 24 Jun 26 02:30:15 PM
print(n.strftime('%d %B %y %I:%M:%S %p'))
# expected output: 24 June 26 02:30:15 PM
print(n.strftime('%a, %d %B, %y %I:%H:%M:%S %p'))
# expected output: Wed, 24 June, 26 02:30:15 PM
print(n.strftime('%A, %d %B, %y %I:%H:%M:%S %p'))
# expected output: Wednesday, 24 June, 26 02:30:15 PM


# timedelta lets you add or subtract time intervals.
from datetime import date, time, datetime, timedelta
n = datetime.now()
n15 = n + timedelta(minutes=15)
n2 = n + timedelta(days=2)
n7 = n + timedelta(days=7)
print(n15, n2, n7, sep='\n')
# expected output: the current time plus 15 minutes, plus 2 days, and plus 7 days

