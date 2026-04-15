class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(f"({self.x},{self.y})")
    def __add__(self,other):
        print(self.x+other.x)
        print(self.y+other.y)


pointer=point(90,86)
pointer2=point(43,25)
print(pointer+pointer2)