student={"Nivaan":96,"Bhadra":97,"Prithviraj":99,"Yurav":94,"Rivaan":85,"Jinaansh":90}
avg=0
for key,value in student.items():
    avg=avg+value
avg=avg/(len(student))
print(f"The maximum score someone has got is {max(student.values())} \n The minimum score someone has got is {min(student.values())}")
r=student.get("Bhadra")
print("Bhadra's score is",r)
x=input("Enter the name of someone you want to look up ")
try:
    l=student[x]
    print("Your persons score is",l)
except KeyError:
    print(x,"is not a registered student")