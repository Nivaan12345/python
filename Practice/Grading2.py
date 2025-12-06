a=int(input("Give me your marks for English "))
b=int(input("Give me your marks for Maths "))
c=int(input("Give me your marks for Science "))
d=int(input("Give me your marks for History "))
e=int(input("Give me your marks for Geography "))
avg=((a+b+c+d+e)/5)
if(avg<=25):
    x=("D")
elif(avg<=50 and avg>=25):
    x=("C")
elif(avg<=75 and avg>=50):
    x=("B")
else:
    x=("A")
print("You have got grade",x,"with a percentage of",avg,"%")
#end