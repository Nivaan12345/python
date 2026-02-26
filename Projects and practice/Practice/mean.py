n=int(input("Enter the amount of numbers you want to add "))
x=[]
for m in range(n):
    temp=int(input(f"Enter number{m+1} "))
    x.append(temp)
y=0
for i in x:
    y=y+i
z=y/n
print("The mean of your numbers is",z.__round__(1))
#end