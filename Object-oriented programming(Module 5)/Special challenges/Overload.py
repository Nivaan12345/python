class operator:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        if self.x<other.x:
            return("ob<ob")
        else:
            return("ob>ob")
    def __eq__(self,other):
        if self.x==other.x:
            return("ob==ob")
        else:
            return("ob!=ob")
ob1=operator(40)
ob2=operator(60)
ob3=operator(5)
ob4=operator(40)
print(ob1<ob3)
print(ob1==ob4)