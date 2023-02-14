import turtle

def drawpolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    t.penup()
    t.left(90)
    t.forward(sideLength)
    t.right(90)
    t.pendown()
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawcircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawpolygon(anyTurtle, sideLength, 360)


wn = turtle.Screen()
wheel = turtle.Turtle()

drawcircle(wheel,20)

wn.exitonclick()
