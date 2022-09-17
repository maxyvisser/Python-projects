from turtle import *
t = Turtle()

Counter = 0
t.left(90)
t.forward(57)
t.right(90)

while Counter <= 360:
    t.forward(1)
    t.right(1)
    Counter += 1

t.done()