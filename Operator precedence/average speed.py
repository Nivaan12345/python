p1=int(input("Enter the speed of the first cyclist "))
p2=int(input("Enter the speed of the second cyclist "))
p3=int(input("Enter the speed of the third cyclist "))
avg=(p1+p2+p3)/3
if(p1<avg):
    print("Cyclist 1 is slower than the average speed")
if(p2<avg):
    print("Cyclist 2 is slower than the average speed")
if(p3<avg):
    print("Cyclist 3 is slower than the average speed")
#end