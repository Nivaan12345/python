
n=int(input("Enter the number "))
p=int(input("Enter to what power you have to calculate it "))
res=1
for i in range(1,p+1):
    res=res*n
print(res)