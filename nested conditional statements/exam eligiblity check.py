medical=str(input("Do you have a medical cause('Y' for yes and 'N' for no) "))
if(medical=='N'):
    attend=int(input("How much is your attendance "))
    if(attend<=75):
        print("you are not allowed in the exam")
    else:
        print("You are allowed in the exam")
else:
    print("You are allowed in the exam")
#end