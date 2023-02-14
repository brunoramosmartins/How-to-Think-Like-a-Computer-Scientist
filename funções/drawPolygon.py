import turtle

def drawpolygon(t, sideLength, numSides):
    """Faz uma tartaruga t desenhar um Poligono de numSides lados de tamanho sideLength."""

    for i in range(numSides):
        t.forward(sideLength)
        t.left(360/numSides)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()

drawpolygon(tess, 1, 120)

wn.exitonclick()
