import random
x=int(input("How many characters  should be in the password "))
y=(1,2)
a=""
r=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
   'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def  berry(x):
    g=random.choice(y)
    for i in range(x+1):
        if g==1:
            temp=random.randint(0,9)
        else:
            temp=random.choice(r)
    a=a+temp
while int is not  a:
    berry(x)
print(a)