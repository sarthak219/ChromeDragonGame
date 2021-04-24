import random
import time
import turtle
import os

d = 18
delay = 0.01
r = 0
score = 0
high_score = 0
counter = 0
k = 10

obstacles = ["cactus", "many_cactus", "bird", "low bird"]

# Screen Setup
wn = turtle.Screen()
wn.title("Chrome Dragon Game")
wn.setup(width=800, height=600)
wn.bgcolor("white")
wn.tracer(0)

# Registering Shapes
wn.register_shape("./venv/images/dragon.gif")
wn.register_shape("./venv/images/cactus.gif")
wn.register_shape("./venv/images/many_cactus.gif")
wn.register_shape("./venv/images/bird.gif")
wn.register_shape("./venv/images/sleeping_dragon.gif")

# Dragon
dragon = turtle.Turtle()
dragon.color("black")
dragon.shape("./venv/images/dragon.gif")
# dragon.shape("square")
dragon.shapesize(stretch_wid=5, stretch_len=2)
dragon.penup()
dragon.speed(0)
dragon.goto(-250, 0)
dragon.jumping = "deactivated"
dragon.crouch = "deactivated"

# Cactus
cactus = turtle.Turtle()
cactus.color("black")
cactus.shape("./venv/images/cactus.gif")
cactus.shapesize(stretch_wid=5, stretch_len=2)
cactus.penup()
cactus.goto(500, 0)

# Many_Cactus
many_cactus = turtle.Turtle()
many_cactus.color("black")
many_cactus.shape("./venv/images/many_cactus.gif")
many_cactus.penup()
many_cactus.goto(500, -10)

# bird
bird = turtle.Turtle()
bird.color("black")
bird.shape("./venv/images/bird.gif")
bird.penup()
bird.goto(500, 50)

# low bird
low_bird = turtle.Turtle()
low_bird.color("black")
low_bird.shape("./venv/images/bird.gif")
low_bird.penup()
low_bird.goto(500, -10)


# Drawing Tool
drawing_tool = turtle.Turtle()
drawing_tool.hideturtle()
drawing_tool.penup()
drawing_tool.goto(-400, -50)
drawing_tool.speed(0)
drawing_tool.pendown()
drawing_tool.goto(400, -50)

# Scoring pen
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.clear()
pen.goto(100, 250)
pen.write("Score: {}\tHigh Score: {}".format(score, high_score), font=("Courrier", 18, "normal"))


# Functions
def enable_jump():
    if dragon.ycor() <= 0:
        os.system("afplay ./venv/sounds/jump.wav&")
    dragon.jumping = "active"


def enable_crouch():
    dragon.crouch = "activated"


def jump():
    dragon.shape("./venv/images/dragon.gif")
    dragon.shapesize(stretch_wid=5, stretch_len=2)
    if dragon.ycor() == -30:
        dragon.sety(0)
    global d
    # while dragon.ycor() >= 0:
    y = dragon.ycor()
    y += d
    d -= 1
    dragon.sety(y)
    if y <= 0:
        dragon.jumping = "Deactivated"
        d = 18


def crouch():
    dragon.shape("./venv/images/sleeping_dragon.gif")
    dragon.shapesize(stretch_len=5, stretch_wid=2)
    dragon.sety(-30)
    dragon.crouch = "deactivated"
    # dragon.shape("./venv/images/sleeping_dragon.gif")


# Obstacle_functions
def cactus_obstacle():
    global k
    x = cactus.xcor()
    x -= k
    cactus.setx(x)


def many_cactus_obstacle():
    global k
    x = many_cactus.xcor()
    x -= k
    many_cactus.setx(x)


def bird_obstacle():
    global k
    x = bird.xcor()
    x -= k
    bird.setx(x)


def low_bird_obstacle():
    global k
    x = low_bird.xcor()
    x -= k
    low_bird.setx(x)


# def set_shape_to_normal():
#     dragon.shape("./venv/images/dragon.gif")


# Keyboard Bindings
wn.listen()
wn.onkeypress(enable_jump, "Up")
wn.onkeypress(enable_jump, "space")
wn.onkeypress(enable_crouch, "Down")

# Main Game Loop
while True:
    wn.update()

    # When Obstacles Exit the Screen
    if cactus.xcor() < -380:
        cactus.setx(500)
        r = random.randint(0, len(obstacles) - 1)

    if many_cactus.xcor() <= -380:
        many_cactus.setx(500)
        r = random.randint(0, len(obstacles) - 1)

    if bird.xcor() <= -380:
        bird.setx(500)
        r = random.randint(0, len(obstacles) - 1)

    if low_bird.xcor() <= -380:
        low_bird.setx(500)
        r = random.randint(0, len(obstacles) - 1)

    # Movements
    if dragon.jumping == "active":
        jump()

    if dragon.crouch == "activated" and dragon.ycor() == 0:
        crouch()

    # Random Obstacle
    if obstacles[r] == "cactus":
        cactus_obstacle()

    if obstacles[r] == "many_cactus":
        many_cactus_obstacle()

    if obstacles[r] == "bird":
        bird_obstacle()

    if obstacles[r] == "low bird":
        low_bird_obstacle()

    # collision
    if dragon.distance(cactus) < 70:
        dragon.jumping = "deactivated"
        os.system("afplay ./venv/sounds/beep-10.m4a&")
        time.sleep(1)
        dragon.goto(-250, 0)
        dragon.shapesize(stretch_len=2, stretch_wid=5)
        dragon.shape("./venv/images/dragon.gif")
        cactus.goto(500, 0)
        d = 18
        r = 0
        score = 0
        counter = 0
        k = 10

    if dragon.distance(many_cactus) < 100:
        dragon.jumping = "deactivated"
        os.system("afplay ./venv/sounds/beep-10.m4a&")
        time.sleep(1)
        dragon.goto(-250, 0)
        dragon.shapesize(stretch_len=2, stretch_wid=5)
        dragon.shape("./venv/images/dragon.gif")
        many_cactus.goto(500, -10)
        d = 18
        r = 0
        score = 0
        counter = 0
        k = 10

    if dragon.distance(bird) < 80:
        dragon.jumping = "deactivated"
        os.system("afplay ./venv/sounds/beep-10.m4a&")
        time.sleep(1)
        dragon.goto(-250, 0)
        dragon.shapesize(stretch_len=2, stretch_wid=5)
        dragon.shape("./venv/images/dragon.gif")
        bird.goto(500, 50)
        d = 18
        r = 0
        score = 0
        counter = 0
        k = 10

    if dragon.distance(low_bird) < 80:
        dragon.jumping = "deactivated"
        os.system("afplay ./venv/sounds/beep-10.m4a&")
        time.sleep(1)
        dragon.goto(-250, 0)
        dragon.shapesize(stretch_len=2, stretch_wid=5)
        dragon.shape("./venv/images/dragon.gif")
        low_bird.goto(500, -10)
        d = 18
        r = 0
        score = 0
        counter = 0
        k = 10

    counter += 1

    # Incrementing Score
    if counter % 10 == 0 and counter != 0:
        score += 1

        if score > high_score:
            high_score = score

        # Display Score
        pen.clear()
        pen.write("Score: {}\tHigh Score: {}".format(score, high_score), font=("Courrier", 18, "normal"))

    if score % 100 == 0 and score != 0:
        os.system("afplay ./venv/sounds/bonus.mp3&")

    if counter == 1001:
        counter = 1
        k += 1

    time.sleep(delay)
# wn.mainloop()
