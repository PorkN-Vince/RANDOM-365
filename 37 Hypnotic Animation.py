import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")

t.speed(0)
h=0
for i in range(360):
    color=colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    t.circle(i)
    t.right(5)

    h+=0.01

turtle.done()