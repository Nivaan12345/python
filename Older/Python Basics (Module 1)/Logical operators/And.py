a=int(input("Enter your first number"))
b=int(input("Enter your second number"))
if(a>0 and b>0):
    print("Both the numbers are positive")
elif(a>0 and b<0):
    print(a,"is positive")
elif(a<0 and b>0):
    print(b,"is positive")
else:
    print("Both",a,"and",b,"are negative")
#end