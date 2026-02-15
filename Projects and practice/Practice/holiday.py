holiday=[19/2/2026,3/3/2026,]
x=(input("Enter the day you want to check is a holiday or not in the format of day/month/year: "))
for i in holiday:
    if x==i:
        print("The day",x,"is a holiday")
        break
    else:
        print("The day",x,"is not a holiday")