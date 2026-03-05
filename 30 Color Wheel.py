import turtle, time, math, random
screen = turtle.Screen()
screen.bgcolor('black')
t=turtle.Turtle()
t.speed(0)
t.hideturtle()

color = ['red', 'pink', 'yellow', 'orange', 'purple', 'cyan']

for step in range(36):
        t.color(random.choice(color))
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.begin_fill()
        for i in range(2):
            t.circle(50,60)
            t.left(120)
        t.end_fill()

        t.left(10)
        time.sleep(0.1)


t.penup()
t.goto(0,-200)
t.pendown()
t.color('lime')
t.write('Flower Bloomed ', align='center', font=('Arial', 24, 'bold'))

turtle.done()