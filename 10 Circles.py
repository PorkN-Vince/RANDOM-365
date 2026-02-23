import turtle
import random 
screen=turtle.Screen()
screen.bgcolor("black")

turtle.colormode(255)

t=turtle.Turtle()
t.speed(0)
t.width(2)

for i in range(300):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.color(r,g,b)

    t.forward(i)
    t.left(random.randint(10, 60))
    t.circle(random.randint(5, 40))
turtle.done()