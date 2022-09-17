import turtle
import time

score = 0
speed = 144
freq = 1 / speed
dx = 4
dy = 4
pause = True
direction = 0

wn = turtle.Screen()
wn.title("Atari Breakout")
wn.bgcolor("black")
wn.setup(width=1280, height=800)
wn.tracer(0)

player = turtle.Turtle()
player.shape("square")
player.color("white")
player.shapesize(stretch_wid=1, stretch_len=5)
player.penup()
player.goto(0, -350)

block = turtle.Turtle()
block.shape("square")
block.color("white")
block.shapesize(stretch_wid=1, stretch_len=5)
block.penup()
block.goto(0, 0)

ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, -100)

def player_right():
    global direction
    direction = "right"

def player_left():
    global direction
    direction = "left"

def pause_toggle():
    global pause
    if pause: pause = False
    else: pause = True

wn.listen()
wn.onkeypress(player_right, "d")
wn.onkeypress(player_left, "a")
wn.onkeypress(pause_toggle, "space")

while True:
    while pause:
        wn.update()
        time.sleep(freq)

    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    if direction:
        if direction == "right":
            x = player.xcor()
            x += 32
            player.setx(x)

        elif direction == "left":
            x = player.xcor()
            x -= 32
            player.setx(x)

    direction = 0

    if ball.ycor() > 390:
        ball.sety(390)
        dy *= -1

    elif ball.ycor() < -330:
        if player.xcor() + 50 > ball.xcor() > player.xcor() - 50:
            ball.sety(-330)
            dy *= -1
        else:
            ball.goto(0, -100)
            player.goto(0, -350)

    if ball.xcor() > 630:
        ball.setx(630)
        dx *= -1

    elif ball.xcor() < -620:
        ball.setx(-620)
        dx *= -1

    wn.update()
    time.sleep(freq)

wn.bye