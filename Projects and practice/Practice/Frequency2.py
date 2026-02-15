x=(input("Enter the string which you want to check the frequency of "))
y=(input("Enter the number or letter you want to find in the string "))
z=0
for i in x:
    if i==y:
        z=z+1
    else:
        continue
print("The frequency of",y,"in the string is",z)