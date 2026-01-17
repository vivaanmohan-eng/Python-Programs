import random as ran
import turtle as turt
import time

sc = turt.Screen()
sc.bgcolor("white")
sc.setup(800, 800)
sc.tracer(0)

TOTAL_TIME = ran.randint(15, 20)
start_time = time.time()

timer = turt.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0, 350)
timer.color("black")

circles = []
spawn_interval = 1.5
last_spawn_time = time.time()
running = True

def spawn_circle():
    circ = turt.Turtle()
    circ.hideturtle()
    circ.penup()
    circ.speed(0)

    size = ran.randint(10, 50)
    circ.shape("circle")
    circ.shapesize(size / 10)
    circ.color(ran.choice(["green", "black", "blue", "red"]))

    x = ran.randint(-380, 380)
    y = ran.randint(-380, 380)
    circ.goto(x, y)
    circ.showturtle()

    circles.append((circ, time.time()))

def update_timer():
    remaining = max(0, int(TOTAL_TIME - (time.time() - start_time)))
    timer.clear()
    timer.write(f"Time left: {remaining}s", align="center",
                font=("Arial", 20, "bold"))
    return remaining

while running:
    sc.update()
    current_time = time.time()

    if current_time - last_spawn_time > spawn_interval:
        spawn_circle()
        last_spawn_time = current_time
        spawn_interval = max(0.2, spawn_interval * 0.95)

    for circ, birth in circles[:]:
        if current_time - birth > 1:
            circ.clear()
            circ.hideturtle()
            circ.goto(1000, 1000)
            circles.remove((circ, birth))

    if update_timer() <= 0:
        running = False

timer.clear()
timer.goto(0, 0)
timer.write(
    f"Finished!\nTotal time: {TOTAL_TIME} seconds",
    align="center",
    font=("Arial", 28, "bold")
)

sc.update()
time.sleep(4)
sc.bye()
