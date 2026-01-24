from datetime import datetime
import calendar
x=int(input("Enter the year for which you want the calendar for"))
y=int(input("Enter the month for which you want the calendar for"))
print(datetime.now())
print(calendar(x,y))