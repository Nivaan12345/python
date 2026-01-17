try:
    num1,num2=eval(input("Enter two numbers seperated by a comma "))
    res=num1/num2
    print(round(res,3))
except ZeroDivisionError:
    print("You cannot divide a number by 0")
except NameError:
    print("There should be a comma")
except SyntaxError:
    print("There should be a comma")
except ValueError:
    print("Invalid input")
finally:
    print("This will execute no matter what")