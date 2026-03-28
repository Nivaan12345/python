x=input("Enter the string ")
x=x[::-1]
y=[]


def func(x):
    temp=""
    for i in x:
        while i!=" ":
            temp=temp+i
    temp.append(y)

while x!="":
    func(x)


for j in y:
    print(j)