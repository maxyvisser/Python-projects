import turtle
import time
import random

speed = 10
debug = False

while True:
    if speed == "stop": break
    try: freq = 1 / int(speed)
    except:
        if debug: print("Error: please enter a number.")
    
    score = 0
    direction = "up"
    tempdirection = "up"
    snekx = [0]
    sneky = [0]
    x = 0
    y = 0
    pause = True
    stop = False
    
    #The window, does basically nothing
    wn = turtle.Screen()
    wn.reset()
    wn.title("Snake")
    wn.bgcolor("black")
    wn.setup(width = 1280, height = 800)
    wn.tracer(0)
    
    #The head of the snake, invisible
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
    player.goto(0, 0)
    player.ht()
    
    #The snake-drawer, itself invisible.
    snake = turtle.Turtle()
    snake.ht()
    snake.pendown()
    snake.pensize(15)
    snake.pencolor("white")
    
    #The fruit
    fruit = turtle.Turtle()
    fruit.shape("square")
    fruit.color("red")
    fruit.penup()
    fruitx = 200
    fruity = 200
    fruit.goto(200, 200)

    def player_up():
        global tempdirection, pause
        tempdirection = "up"
        pause = False
        if debug: print("Up")
    
    def player_left():
        global tempdirection, pause
        tempdirection = "left"
        pause = False
        if debug: print("Left")
    
    def player_down():
        global tempdirection, pause
        tempdirection = "down"
        pause = False
        if debug: print("Down")
    
    def player_right():
        global tempdirection, pause
        tempdirection = "right"
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

    while not stop:
        while pause:
            wn.update()
            time.sleep(freq)

        if tempdirection == "up" and direction != "down": direction = "up"
        if tempdirection == "left" and direction != "right": direction = "left"
        if tempdirection == "down" and direction != "up": direction = "down"
        if tempdirection == "right" and direction != "left": direction = "right"

        #player movement
        if direction == "up":
            y = player.ycor()
            y += 20
            player.sety(y)

        elif direction == "left":
            x = player.xcor()
            x -= 20
            player.setx(x)

        elif direction == "down":
            y = player.ycor()
            y -= 20
            player.sety(y)

        elif direction == "right":
            x = player.xcor()
            x += 20
            player.setx(x)

        #snake drawing
        snekx.append(x)
        sneky.append(y)

        if fruitx == x and fruity == y:
            score += 1
            fruitx = 20 * random.randrange(-30, 30)
            fruity = 20 * random.randrange(-18, 18)

            while fruitx in snekx and fruity in sneky:
                fruitx = 20 * random.randrange(-30, 30)
                fruity = 20 * random.randrange(-18, 18)

            fruit.goto(fruitx, fruity)

        else:
            snekx.pop(0)
            sneky.pop(0)

        for i in range(-len(snekx), -1):
            if x == snekx[i] and y == sneky[i]:
                print("You just died (crash into self). Try again?")
                stop = True

        if x > 640 or x < -640 or y > 400 or y < -400:
            if debug: print("You just died (crash into wall). Try again?")
            stop = True

        snake.clear()
        snake.penup()
        snake.setposition(snekx[0], sneky[0])
        snake.pendown()

        try:
            for i in range(0, len(snekx)):
                snake.setpos(snekx[i], sneky[i])
        except:
            if debug: print("Error: something went wrong!")

        if debug:
            print(direction)
            print(snekx, sneky)

        wn.update()
        time.sleep(freq)

    speed = wn.textinput("You died!", """You died!
Press ok to try again.
Input a number for a new speed.
Input 'stop' to stop the program.""")

wn.bye()