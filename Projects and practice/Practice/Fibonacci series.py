x=int(input("Enter How many times the series should go on till "))
n=1
y=0
print(y)
for i in range(x):
    s=n+y
    print(s)
    n=y
    y=s
#end