import turtle
import time
x=time.time()
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
angle=360/6
for i in range(1,7,1):
    polygon.forward(50)
    time.sleep(2)
    polygon.right(angle)
turtle.done()