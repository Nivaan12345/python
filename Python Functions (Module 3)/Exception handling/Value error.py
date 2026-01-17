try :
    x=int(input("Enter a number "))
except ValueError as ex:
    print("Invalid input",ex)
