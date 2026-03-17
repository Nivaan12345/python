import random
Choice=['Rock','Paper','Scissors']
x=input("Choose between Rock Paper and Scissors \n")
y=random.choice(Choice)
print("You chose",x)
print("The computer chose",y)

if x==y:
    print("Its a tie")
elif x=='Rock' and y=='Scissors':
    print("Rock slashes scissors")
    print("You won the game")
elif x=='Paper' and y=='Rock':
    print("Paper covers rock")
    print("You won the game")
elif x=='Scissor' and y=='Paper':
    print("Scissor cuts paper")
    print("You won the game")
else:
    print("You lose")
#end