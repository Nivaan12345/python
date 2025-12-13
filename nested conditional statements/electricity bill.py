units=int(input("Enter the number of units for your electricity bill"))
if(units<50):
    x=((units*2.60)+25)
elif(units>50 and units<100):
    x=((units*3.25)+35)
elif(units>100 and units<200):
    x=((units*5.26)+45)
else:
    x=((units*8.45)+75)
print("You have to pay rupees",x,"for your electricity bill if you have",units,"units")