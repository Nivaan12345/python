a=int(input("Give me your marks for English "))
b=int(input("Give me your marks for Maths "))
c=int(input("Give me your marks for Science "))
d=int(input("Give me your marks for History "))
e=int(input("Give me your marks for Geography "))
avg=((a+b+c+d+e)/5)
per=avg
if(avg<=25):
    print("You have got D grade with a percentage of",int(per),"%")
elif(avg<=50 and avg>=25):
    print("You have got C grade with a percentage of",int(per),"%")
elif(avg<=75 and avg>=50):
    print("You have got B grade with a percentage of",int(per),"%")
else:
    print("You have got A grade with a percentage of",int(per),"%")