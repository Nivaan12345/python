student={"Nivaan":96,"Bhadra":97,"Prithviraj":99,"Yurav":94,"Rivaan":85,"Jinaansh":90}
avg=0
while True:
    z=input("Do you want to register a name?(Y/N) ")
    if z=="N":
        break
    elif z=="Y":
        new=input("Enter the  new student's name ")
        new2=int(input("Enter his scores out of 100 "))
        student[str(new)]=new2
    else:
        print("Please State yes or no with a capital Y or N")
        exit()
for key,value in student.items():
    avg=avg+value
avg=avg/(len(student))
print(f"The maximum score someone has got is {max(student.values())}")
print(f"The minimum score someone has got is {min(student.values())}")
print("The average score is",round(avg,2))
x=input("Enter the name of someone you want to look up ")
try:
    l=student[x]
    print("Your person's score is",l)
except KeyError:
    print(x,"is not a registered student")