x=int(input("Which number do you want to start from "))
y=int(input("Which number do you want to end from "))
list1=[]
even=[]
odd=[]
temp1=''
def square(x,y,temp1,list1):
    for i in range(x,y+1):
        temp1=x*x
        list.insert(list1,i+1,temp1)
    for j in list1:
        if j%2==0:
            list.insert(even,0,j)
        else:
            list.insert(odd,0,j)
    list.sort(odd)
    list.sort(even)
    print("the odd squares are",odd)
    print("The even squares are",even)
square(x,y,temp1,list1)
#end