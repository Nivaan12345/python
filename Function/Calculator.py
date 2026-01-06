def add(num1,num2):
    x=num1+num2
    return x
def subtract(num1,num2):
    x=num1-num2
    return x
def multiply(num1,num2):
    x=num1*num2
    return x
def divide(num1,num2):
    x=num1/num2
    return x

print("Please select the operation")
print("1.)Add")
print("2.)Subtract")
print("3.)Multiply")
print("4.)Divide")
choice=(input("Your choice is "))
num1=int(input("Enter your first number "))
num2=int(input("Enter your second number "))
r='='

if choice=='1':
    res=add(num1,num2)
    m="+"
elif choice=='2':
    res=subtract(num1,num2)
    m="-"
elif choice=='3':
    res=multiply(num1,num2)
    m="*"
elif choice=='4':
    res=divide(num1,num2)
    m="/"
else:
    print("invalid choice, please try again")

print(num1,m,num2,r,res)