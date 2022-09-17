import turtle, time, random

wn = turtle.Screen()
wn.screensize(1280, 800)
wn.bgcolor("black")
wn.tracer(0)

bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("red")
bullet.pu()
bullet.goto(-640, 0)
bullet.pd()

dx = 0
dy = 0
bulletx = 0
bullety = 0
land = []
bulletfly = False

for bulletx in range(-640, 640):
    bullety = random.randrange(bullety - 3, bullety + 4)
    land.append(bullety)
    bullet.goto(bulletx, bullety)

bullet.pu()
bullet.goto(0, 300)

wn.listen()

while True:
    while bullet.ycor() > land[bulletx]:
        bulletx = bullet.xcor()
        bullety = bullet.ycor()
        bulletx += dx
        bullety += dy
        bullet.goto(bulletx, bullety)
        dy -= 1
        wn.update()
        time.sleep(1/60)
    
    wn.update()
    time.sleep(1/60)