#checking divisiblity of one number
num=int(input("enter a numerator "))
den=int(input("enter a denominator "))
x=num%den
if(num%den==0):
    print(num,"is divisible by",den)
else:
    print(num,"is not divisible by",den,"with a remainder of",x)