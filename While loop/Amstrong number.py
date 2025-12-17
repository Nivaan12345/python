num=int(input("Enter the number you want to check "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if(sum==num):
    print("This is an amstrong number")
else:
    print("This is not an amstrong number")