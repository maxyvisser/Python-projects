import turtle, keyboard, time

wn = turtle.Screen()
wn.title("TurtleTest")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
Floor = turtle.Turtle()
Floor.shape("square")
Floor.shapesize(stretch_wid = 1, stretch_len = 10)
Floor.sety(-17)
Floor.color("blue")
turtle.color("white")
turtle.left(90)
turtle.penup()
turtle.shape("triangle")
Yvel = 0
Xvel = 0

while True:
    if turtle.ycor() > 0:
        y = turtle.ycor()
        y += Yvel
        turtle.sety(y)
        Yvel -= 1
    elif Yvel == 10:
        y = turtle.ycor()
        y += Yvel
        turtle.sety(y)
        Yvel -= 1
    if Xvel > 0:
        x = turtle.xcor()
        x += Xvel
        turtle.setx(x)
        Xvel -= 1
    elif Xvel < 0:
        x = turtle.xcor()
        x += Xvel
        turtle.setx(x)
        Xvel += 1
    if keyboard.is_pressed ("w") and turtle.ycor() == 0:
        Yvel = 10
    if keyboard.is_pressed("a"):
        Xvel = -3
    if keyboard.is_pressed("d"):
        Xvel = 3
    wn.update()
    time.sleep(0.01)