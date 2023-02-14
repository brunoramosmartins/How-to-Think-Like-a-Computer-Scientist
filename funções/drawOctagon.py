import turtle

def drawoctagon(t, sz):
    """Faz uma tartaruga t desenhar um octogono de lado sz."""

    for i in range(8):
        t.forward(sz)
        t.left(45)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()

drawoctagon(tess, 50)

wn.exitonclick()
