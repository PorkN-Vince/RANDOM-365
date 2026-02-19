Explanation for 03 Hearts and it works

IMPORTS
import turtle
import random
import time


turtle → used for graphics and drawing shapes.

random → used to generate random positions (for the running NO button).

time → used for delays (sleep) to create animation effects.


Screen Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("For Someone Special ❤️")


turtle.Screen() creates the drawing window.

bgcolor("black") sets the background color.

title() sets the window title at the top.

So this prepares your “stage”.


Main Heart Turtle Setup
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)
heart.color("red", "pink")
heart.pensize(3)


Turtle() creates a drawing object.

hideturtle() hides the arrow cursor.

speed(0) makes it draw instantly (fastest speed).

color("red", "pink")

red = outline color

pink = fill color

pensize(3) sets line thickness.

This turtle is responsible for drawing the big heart.


draw_heart(size) Function
def draw_heart(size):


This function draws a heart shape based on a given size.

Reset Position
heart.clear()
heart.penup()
heart.goto(0, 0)
heart.setheading(0)
heart.pendown()


clear() removes previous drawing (important for pulsing animation).

penup() lifts pen (so it doesn’t draw while moving).

goto(0,0) moves to center.

setheading(0) resets direction.

pendown() starts drawing again.

Drawing the Heart
heart.begin_fill()
heart.left(140)
heart.forward(size)


begin_fill() starts filling the shape.

left(140) rotates turtle.

forward(size) draws first straight line.

First Curve
for _ in range(200):
    heart.right(1)
    heart.forward(size/111.65)


Loop runs 200 times.

Each time:

turn right 1 degree

move forward a tiny amount

This creates a smooth curved arc.

Second Curve
heart.left(120)

for _ in range(200):
    heart.right(1)
    heart.forward(size/111.65)


This creates the other half of the heart curve.

Finish Shape
heart.forward(size)
heart.end_fill()


Completes the bottom point of the heart.

end_fill() fills it with pink.


Pulsing Animation
def pulse():


This makes the heart look like it’s beating.

Growing
for i in range(5):
    draw_heart(111.65 + i*5)


Each loop increases the size slightly.

Heart grows bigger.

Shrinking
for i in range(5, 0, -1):
    draw_heart(111.65 + i*5)


Loops backward.

Heart shrinks again.

Important Line
screen.tracer(0)


This turns off automatic animation updates.

Instead of drawing every tiny movement, the screen updates only when:

screen.update()


This makes animation smoother.


Typing Effect
def type_writer(msg):


This creates the romantic typing animation.

displayed = ""


Stores letters that have already appeared.

for letter in msg:
    displayed += letter


Adds one letter at a time.

text_turtle.clear()
text_turtle.write(displayed, ...)
time.sleep(0.1)


Clears previous text

Rewrites updated text

Waits 0.1 seconds before next letter

This creates the letter-by-letter effect.


YES and NO Buttons

These are just text positioned on the screen.

yes_button.goto(-60, -130)
no_button.goto(60, -130)


Left side = YES
Right side = NO


Click Detection

When you click the screen:

screen.onclick(yes_clicked)
screen.onclick(no_clicked)


⚠ Important:

Only the last onclick works because it overrides the first one.

So currently only no_clicked is active.

If you want both to work, you should combine them into ONE function.


YES Button Logic
if -120 < x < 0 and -150 < y < -110:


This checks if the mouse click is inside a rectangular area around the YES text.

If true:

Clears message

Writes “YAYYY ❤️❤️❤️”

So you manually created a clickable area using coordinates.


NO Button Logic (Runs Away 😂)
new_x = random.randint(-200, 200)
new_y = random.randint(-200, 0)


Generates random position.

no_button.clear()
no_button.goto(new_x, new_y)


Moves the NO button somewhere else.

That’s why it runs away when clicked.


Programming Concepts You Used

You actually used:

Functions

Parameters (size)

For loops

Range with reverse counting

Animation timing

Screen optimization (tracer)

Event handling (mouse clicks)

Random number generation

Coordinate-based collision detection

This is NOT beginner level anymore. This is early intermediate 👏
