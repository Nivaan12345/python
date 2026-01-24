import random
import datetime
start=datetime.date(2026,1,1)
end=datetime.date(2026,12,31)
randays=random.randint(0,(end - start).days)
randate=start+datetime.timedelta(days=randays)
print("The random date is:",randate)