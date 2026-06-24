class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)
class employee(person):
    def __init__(self,name,id,salary,post):
        self.salary=salary
        self.post=post

        person.__init__(self,name,id)
Naman=employee("Naman","R2Y789",123456,"CEO")
Naman.display()