import turtle as turt
import time
import random as ran
sc = turt.Screen("white")
sc.setup(800,800)
sc.tracer(0)

#Player Setup
p = turt.Turtle()
p.shape("triangle")
p.color("red")
p.up()
p.goto(0,-400)
p.setheading(90)

#Score
score = 0
sco_dis = turt.Turtle()
sco_dis.hideturtle()
sco_dis.up()
sco_dis.goto(-400,400)
sco_dis.color("blue")
sco_dis.write(f"Score: {score}", font=("Arial", 20, "italic"))

#balloons
balloons = []
game_speed = 0.02
dif_inc = 0.001
spawn_int = 2
last_spawn_time = time.time()
running = True

#Functions
def move_left():
    x = p.xcor() - 20
    if x > -380:
        p.setx(x)

def move_right():
    x = p.xcor() + 20
    if x < 380:
        p.setx(x)

def spawn_balloon():
    balloon = turt.Turtle()
    balloon.up()
    balloon.shape("circle")
    balloon.color(ran.choice(["green" , "blue" , "red"]))
    balloon.goto(ran.randint(-400, 400) , 400)
    balloon.speed = ran.uniform(1,3)
    if ran.random()<0.2:
        #20% chance
        balloon.color("black")
        balloon.is_bomb = True
    else:
        balloon.is_bomb = False
    balloons.append(balloon)

def score_upd(points):
    global score
    score += points
    sco_dis.clear()
    sco_dis.write(f"Score: {score}", font=("Arial", 20, "italic"))

def game_over():
    global running
    running = False
    game_over_dis = turt.Turtle()
    game_over_dis.hideturtle()
    game_over_dis.color("red")
    game_over_dis.write("GAME OVER" , align = 'center' , font=("Arial" , 35 , "bold"))
    sc.update()
    time.sleep(4)
    sc.bye()
