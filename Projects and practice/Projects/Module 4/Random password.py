import random
x=int(input("How many characters  should be in the password "))
f=''
lower='qwertyuiopasdfghjklzxcvbnm'
upper='QWERTYUIOPASDFGHJKLZXCVBNM'
num='1234567890'
def berry(x,f,):
    for v in range(x+1):
        v=random.choice(lower,upper,num)
        f=f+v
y=berry(x,f)
if int in y:
    if (str.upper) in y:
        if (str.lower) in y:
            print(f)
        else:
            f=''
            y
    else:
        f=''
        y
else:
    f=''
    y