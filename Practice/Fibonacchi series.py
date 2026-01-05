x=int(input("Enter How many times the series should repeat "))
n=1
y=0
for i in range(x+1):
    s=n+y
    n=y
    y=s
    print(s)