print("Welcome to the calculator\n These are your options")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
choice=int(input("Enter the number of the operation you want to complete "))
def add():
    x=float(input("Enter the number you want to add "))
    y=float(input("Enter the next number you want to add "))
    return ("The sum of your two numbers is",(x+y))

def subtract():
    x=float(input("Enter the number you want to subtract "))
    y=float(input("Enter the number you want to subtract from "))
    return ("The difference of your two numbers is",(y-x))

def multiply():
    x=float(input("Enter the number you want to multiply "))
    y=float(input("Enter the next number you want to multiply "))
    return ("The product of your two number is",(x*y))

def divide():
    x=float(input("Enter the number you want to divide(numerator/dividend) "))
    y=float(input("Enter the number you want to subtract from(denominator/divisor) "))
    return ("The subtraction of your two number is",(x/y))

if choice==1:
    add()
elif choice==2:
    subtract
elif choice==3:
    multiply
elif choice==4:
    divide
except ZeroDivisionError:
    print("You cannot divide with a zero Try again")
except ValueError:
print("Enter a number, not a letter or symbol")