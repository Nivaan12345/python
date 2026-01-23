x=int(input("Enter the number you want to check if is a prime"))
if x%2==0 or x%3==0 or x%5==0 or x%7==0 or x<1:
    print(x," is not a prime number")
else:
    print(x,"is a prime number")