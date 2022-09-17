import turtle
import time
import random

debug = False
speed = 144
freq = 1/speed

wn = turtle.Screen()
wn.reset()
wn.title("Dodge")
wn.bgcolor("black")
wn.setup(width = 1280, height = 800)
wn.tracer(0)

player = turtle.Turtle()
player.shape("square")
player.pencolor("white")
player.pensize(15)
player.penup()
player.goto(-660, -420)
player.pendown()
player.goto(660, -420)
player.goto(660, 420)
player.goto(-660, 420)
player.goto(-660, -420)
player.penup()
player.goto(0, -200)

def player_up():
    global pause
    y = player.ycor()
    y += 20
    player.sety(y)
    pause = False
    if debug: print("Up")

def player_left():
    global pause
    x = player.xcor()
    x -= 20
    player.setx(x)
    pause = False
    if debug: print("Left")
    
def player_down():
    global pause
    y = player.ycor()
    y -= 20
    player.sety(y)
    pause = False
    if debug: print("Down")
   
def player_right():
    global pause
    x = player.xcor()
    x += 20
    player.setx(x)
    pause = False
    if debug: print("Right")

def pause_toggle():
    global pause
    if pause: pause = False
    else: pause = True
    if debug: print(f"pause = {pause}")

   
wn.listen()
wn.onkeypress(player_up, "w")
wn.onkeypress(player_left, "a")
wn.onkeypress(player_down, "s")
wn.onkeypress(player_right, "d")
wn.onkeypress(pause_toggle, "space")


while True:
    wn.update()
    time.sleep(freq)

wn.bye()