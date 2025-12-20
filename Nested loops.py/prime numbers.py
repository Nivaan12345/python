higher=int(input("Enter the highest number till which you want prime numbers "))
lower=int(input("Enter the lowest number till which you want prime numbers "))
for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
            if((num%i)==0):
                break
        else:
            print(num)