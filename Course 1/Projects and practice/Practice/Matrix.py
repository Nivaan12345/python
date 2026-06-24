import turtle
turtle.Screen().bgcolor("Orange")
turtle.Screen().setup(300,400)
matrix=turtle.Turtle()
def x():
    matrix.forward(33)
    matrix.left(90)
def y():
    matrix.forward(99)
    matrix.left(90)
def n():
    x()
    y()
for i in range(4):
    y()
n()
for i in range(3):
    x()
    n()
matrix.penup
turtle.done()
#end