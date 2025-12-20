num=int(input("Enter the number you want to check "))
ans=0
temp=num
while temp>0:
    temp=temp//10
    ans=ans+1
print(num,"has",ans,"digits")