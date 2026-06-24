class employee:
    def __init__(self,name,doj):
        self.name=name
        self.doj=doj
    def __del__(self):
        print(self.name,"is erased")
Neil=employee('Neil',"29-06-2001")
del Neil