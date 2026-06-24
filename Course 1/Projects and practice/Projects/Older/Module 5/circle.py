class circle:
    def __init__(self,r):
        self.r=r
    def area(self,r):
        pi=22/7
        area=2*r*pi
        print(f"The area of a circle with radius {r} cm's is {round(area,2)} square cm")
    def perimeter(self,r):
        pi=22/7
        r2=r*r
        circum=pi*r2
        print("The circumference of a circle with radius",r,"cm's is",round(circum,2),"cm's")
x=int(input("Enter the radius of a circle "))
circlex=circle(x)
print(circlex.area(x))
print(circlex.perimeter(x))