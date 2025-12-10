p=str(input("what is the password to open this encrypted file "))
if(p==str("love you" or "Love you")):
    turf=int(input("enter the price for turf per sq.ft "))
    sq=int(input("Enter the amount of sq.ft you want to turf "))
    tusq=(turf*sq)
    ext=int(input("Add the amount of any extra charges per sq.ft "))
    esqt=(ext*sq)
    tsqe=(tusq+esqt)
    gst=int(input("Enter the percentage of gst applied "))
    gtqe=((gst/100)*tsqe)
    rtge=(tsqe-gtqe)
    print("Your Quotatation should be of Rupees",rtge)
else:
    print("Incorrect password ,please try again later")
#end