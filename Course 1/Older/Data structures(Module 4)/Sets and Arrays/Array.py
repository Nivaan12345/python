import array as arr
x=arr.array('i',[1,2,3,4,5])
for i in range(0,5):
    print(x[i])
x.insert(5,34)
print("\n")
for j in range(0,6):
    print(x[j])
x.reverse()
print("\n")
for l in range(0,6):
    print(x[l])
print("\n")
y=x.count(3)
print(y)