x=int(input("Enter the number that the series should go on till"))
n=1
y=0
for i in range(x+1):
    s=n+y
    print(s)
    n=n+1
    y=s