l=int(input("Enter the amount of numbers you want to add "))
x=[]
for m in range(l):
    temp=int(input("Enter num",m," "))
    x.append(temp)
y=0
for i in x:
    y=y+i
z=y/l
print("The mean of your numbers is",z)
#end