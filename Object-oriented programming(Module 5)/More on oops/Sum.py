class number:
    x=(10,20,30,40,50,60,70)
    def __init__(self,x):
        for i in x:
            for j in x:
                if i+j==self:
                    print(f"index{enumerate[i]}+index{enumerate[j]}is ={self}")
                else:
                    continue
r=[]
r.append(input("Enter the number"))
for i in r:
    i=number((10,20,30,40,50,60,70))