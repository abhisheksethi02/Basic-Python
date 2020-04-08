import turtle
wn=turtle.Screen()
wn.bgcolor("red")
alex=turtle.Turtle()
alex.speed(1)
x=10
y=10
for _ in range(10):
    alex.goto(x,y)
    x=x+5
    y=y+10
    alex.goto(y,x)
    x=x+10
    y=y+5
