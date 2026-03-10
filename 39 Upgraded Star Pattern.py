import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")

t.speed()
h=0

for i in range(300):
    color=colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    t.forward(i)
    t.right(144)

    h+=0.005
turtle.done()