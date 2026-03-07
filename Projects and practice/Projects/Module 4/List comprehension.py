a=int(input("Enter a number "))
x=[1,3,5,7,9,11,13,15,17,19,21]
temp=[]
for i in range(a):
    if i in x:
        temp.append(i)
    else:
        continue
print(x)
print(temp)
x=[]
for j in temp:
    x.append(j)


f=['apple','banana','orange','grape','pear','mango','pomogranate','litchi']
for i in f:
    str.upper(i[0])
print(f)