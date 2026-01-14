x=int(input("Enter the number you want to check if is a prime"))
y=2
for i in range(y,x):
    if x%y>0:
        y=y+1
print(i)