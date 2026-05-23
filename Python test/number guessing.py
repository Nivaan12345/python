import random
x=random.randint(1,50)
attempts=5
while attempts>0:
    y=int(input("Enter the number you are going to guess "))
    if y==x:
        print("Correct answer!\n ------You win------")
        break
    else:
        t=x-y
        r=y-x
        if x>y and t<=5 or y>x and r<=5:
            temp=("🔥 hot")
        elif x>y and t<=10 or y>x and r<=10:
            temp=("🌡️ warm,")
        elif x>y and t<=20 or y>x and r<=20:
            temp=("🥶 cold,")
        else:
            temp=("🧊 ice cold")
        print("Wrong guess try again")
        print(f"Your hint is {temp}")
        attempts=attempts-1
        print(f"You have {attempts} attempts left")

for i in range(attempts):
   print("❤️")
if attempts!=0:
    print("Those were your remaining attempts")
if attempts==0:
    print(f"The correct answer was {x}")