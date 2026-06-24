print("You can go by the following modes of transport         1.car     2.bike")
choice=int(input("Which would you want to go by(1 or 2) "))
if(choice==1):
    print("You have selected car")
    car=int(input("Would you want a SUV or a MUV(1 for SUV and 2 for MUV) "))
    if(car==1):
        print("We have arranged an SUV for your ride")
    elif(car==2):
        print("we have arranged an MUV for your ride")
    else:
        print("Invalid choice, please try again")
elif(choice==2):
    print("You have selected bike")
    bike=int(input("Would you want a Scooter or a Scootie(1 for scootie and 2 for scooter) "))
    if(bike==1):
        print("We have arranged a scootie for your ride")
    elif(bike==2):
        print("we have arranged a scooter for your ride")
    else:
        print("Invalid choice, please try again")
else:
    print("Invalid choice, please try again")
#end