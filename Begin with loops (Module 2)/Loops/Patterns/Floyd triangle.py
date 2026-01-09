rows=int(input("Enter the number of rows you want the triangle to be "))
num=1
for i in range(1,rows+1,1):
    for j in range(1,i+1,1):
        print(num,end='')
        num=num+1
    print()
#end