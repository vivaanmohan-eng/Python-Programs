import turtle as turt
import time
import random as ran
sc = turt.Screen()
sc.bgcolor("White")
sc.setup(800,800)
sc.tracer(0)

#Player Setup
p = turt.Turtle()
p.shape("triangle")
p.color("red")
p.up()
p.goto(0,-250)
p.setheading(90)

#Score
score = 0
sco_dis = turt.Turtle()
sco_dis.hideturtle()
sco_dis.up()
sco_dis.goto(-300,300)
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

#Key bindings
sc.listen()
sc.onkey(move_left, 'a')
sc.onkey(move_right, 'd')

#Gameplay
while running:
    sc.update()
    current_time = time.time()
    if current_time - last_spawn_time > spawn_int:
        spawn_balloon()
        last_spawn_time = current_time
    for balloon in balloons[:]:
        balloon.sety(balloon.ycor() - balloon.speed)
        if balloon.ycor() < -399:
            balloons.remove(balloon)
            balloon.hideturtle()
        #Check for collision
        if p.distance(balloon) < 15:
            if balloon.is_bomb == True:
                game_over()
            else:
                score_upd(5)
            balloons.remove(balloon)
            balloon.hideturtle()
    game_speed = max(0.005, game_speed - dif_inc)
    spawn_int = max(0.5, spawn_int - 0.0005)
    time.sleep(game_speed)
