import turtle
import colorsys

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor('black')
screen.tracer(0)  # Disable auto-rendering for speed

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

h = 0

for i in range(30):          # More iterations = denser pattern
    for j in range(25):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.color(c)
        h += 0.003            # Smaller step = smoother gradient

        t.rt(90)
        t.circle(160 - j * 5, 90)
        t.lt(90)
        t.circle(160 - j * 5, 90)
        t.rt(180)
        t.circle(50, 24)

    screen.update()           # Update once per outer loop = faster render

turtle.done()