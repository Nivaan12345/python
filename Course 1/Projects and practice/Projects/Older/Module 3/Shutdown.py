def shutdown():
    x=(input("Have you saved any files(Y for yes and N for no) "))
    if x=='Y':
        y=(input("Have you shut all other applications(Y for yes and N for no) "))
        if y=='Y':
            print("Shutting down")
        elif y=='N':
            print("Abort shutdown")
        else:
            print("Invalid answer,Please try again")
    elif x=='N':
        print("Abort shutdown")
    else:
        print("Invalid answer,Please try again")
shutdown()
#end