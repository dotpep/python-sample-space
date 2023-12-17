import sys
import calendar
import calendar as c

locations = sys.path
for i in locations:
    print(i)

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isleap = c.isleap(2036)
print(isleap)
