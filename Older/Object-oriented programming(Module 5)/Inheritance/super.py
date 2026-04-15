class dad:
    def __init__(self,name,):
        print("Dad constructor called")
        self.name=name

class mom:
    def __init__(self,name):
        print("Mom constructor called")
        self.name=name

class son(mom,dad):
    def __init__(self,age,name):
        print("Son contuctor called")
        self.age=age
        super().__init__(name)
    def display(self):
        print(self.name,self.age)
nivaan=son(11,"Nivaan")
nivaan.display()