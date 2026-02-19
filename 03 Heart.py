import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("For Someone Special ❤️")

# ---------------- MAIN HEART ---------------- #

heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)
heart.color("red", "pink")
heart.pensize(3)

def draw_heart(size):
    heart.clear()
    heart.penup()
    heart.goto(0, 0)
    heart.setheading(0)
    heart.pendown()
    heart.begin_fill()
    heart.left(140)
    heart.forward(size)

    for _ in range(200):
        heart.right(1)
        heart.forward(size/111.65)

    heart.left(120)

    for _ in range(200):
        heart.right(1)
        heart.forward(size/111.65)

    heart.forward(size)
    heart.end_fill()

# Pulsing animation
def pulse():
    for i in range(5):
        draw_heart(111.65 + i*5)
        screen.update()
        time.sleep(0.05)
    for i in range(5, 0, -1):
        draw_heart(111.65 + i*5)
        screen.update()
        time.sleep(0.05)

screen.tracer(0)
pulse()

# ---------------- TYPING TEXT ---------------- #

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("white")
text_turtle.goto(0, -80)

message = "Can you be my girlfriend?"

def type_writer(msg):
    displayed = ""
    for letter in msg:
        displayed += letter
        text_turtle.clear()
        text_turtle.write(displayed, align="center",
                          font=("Arial", 18, "bold"))
        time.sleep(0.1)

type_writer(message)


# ---------------- BUTTONS ---------------- #

yes_button = turtle.Turtle()
yes_button.hideturtle()
yes_button.penup()
yes_button.goto(-60, -130)
yes_button.color("white")
yes_button.write("YES ❤️", align="center",
                 font=("Arial", 16, "bold"))

no_button = turtle.Turtle()
no_button.hideturtle()
no_button.penup()
no_button.goto(60, -130)
no_button.color("white")
no_button.write("NO 💔", align="center",
                font=("Arial", 16, "bold"))

# YES click
def yes_clicked(x, y):
    if -120 < x < 0 and -150 < y < -110:
        text_turtle.clear()
        text_turtle.goto(0, -80)
        text_turtle.write("YAYYY ❤️❤️❤️",
                          align="center",
                          font=("Arial", 20, "bold"))

# NO click (runs away)
def no_clicked(x, y):
    if 0 < x < 120 and -150 < y < -110:
        new_x = random.randint(-200, 200)
        new_y = random.randint(-200, 0)
        no_button.clear()
        no_button.goto(new_x, new_y)
        no_button.write("NO 💔",
                        align="center",
                        font=("Arial", 16, "bold"))

screen.onclick(yes_clicked)
screen.onclick(no_clicked)

turtle.done()
