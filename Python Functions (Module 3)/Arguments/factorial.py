num=int(input("Enter the number you need the factorial of "))
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
factorial(num)