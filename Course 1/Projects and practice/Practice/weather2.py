import random
v=int(input("Enter the weather 1 days ago "))
w=int(input("Enter the weather 2 days ago "))
x=int(input("Enter the weather 3 days ago "))
y=int(input("Enter the weather 4 days ago "))
z=int(input("Enter the weather 5 days ago "))
a=0
b=0
d=0
f=[1,2]
tuplex=(v,w,x,y,z)
c=random.choice(f)
if c==1:
     for i in tuplex:
         if i>=31:
             a=a+1
         else:
             b=b+1
     if a>b:
         print("It is going to be hot tomorrow")
     else:
         print("It is going to be normal temprature tomorrow")
else:
    for i in tuplex:
        d=d+i
    e=d/5
    if e>=31:
        print("It is going to be hot tomorrow")
    else:
        print("It is going to be cold tomorrow")
#end