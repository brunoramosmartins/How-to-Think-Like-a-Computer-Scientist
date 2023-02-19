import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

alex = turtle.Turtle()
dist = 2
for i in range(160):
    alex.forward(dist)
    alex.right(89)
    dist += 2

wn.exitonclick()
