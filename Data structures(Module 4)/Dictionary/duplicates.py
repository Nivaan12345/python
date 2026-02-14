x={'id1':{'name':['Nivaan'],'class':[6],'age':[11],'subject':['math,science,history']}
,'id2':{'name':['Naman'],'class':[6],'age':[11],'subject':['math,science,history']}
,'id3':{'name':['Purahan'],'class':[6],'age':[11],'subject':['math,science,history']}
,'id4':{'name':['Advik'],'class':[5],'age':[11],'subject':['math,science,history']}
,'id5':{'name':['Nivaan'],'class':[6],'age':[11],'subject':['math,science,history']}}
y={}
for key,value in x.items():
    if value not in y.values():
        y[key]=value
print(y)