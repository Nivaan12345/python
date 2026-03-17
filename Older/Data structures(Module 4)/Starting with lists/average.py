marks=[100,89,92,77]
sum=0
for i in marks:
    sum=sum+i
avg=sum/(len(marks))
print(avg)
marks.sort()
print(marks[0])
print(marks[3])