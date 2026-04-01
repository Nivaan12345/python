from abc import ABC,abstractmethod
class shape:
    def __init__(self,sides):
        self.sides=sides
        print(self.sides)
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,l,b,sides):
        print("this is a rectangle")
        self.l=l
        self.b=b
        shape.__init__(self,sides)
    def area(self):
        return self.l*self.b

class square(shape):
    def __init__(self,l,sides):
        print("this is a square")
        self.l=l
        shape.__init__(self,sides)
    def area(self):
        return self.l**2

sq=square(20,4)
rec=rectangle(15,6,4)
print(f"The area of the rectangle is {rec.area()} cm")
print(f"The area of the square is {sq.area()} cm")