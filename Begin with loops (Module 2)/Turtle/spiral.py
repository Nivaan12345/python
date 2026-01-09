import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(300,400)
spiral=turtle.Turtle()
size=0
while True:
    for i in range(4):
        spiral.forward(size+1)
        spiral.left(90)
        size=size-5
    size=size+1