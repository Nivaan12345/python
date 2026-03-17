import random
x="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
y=''
for i in range(9):
    y=y+random.choice(x)
print(y)