pi=22/7
r=int(input("enter the diameter of the circle in cm "))
r=r/2
def circum(radius):
    x=2*pi*r
    return x
res=circum(r)
print("The circumference of the circle is",int(res),"cms(",res,")cms")