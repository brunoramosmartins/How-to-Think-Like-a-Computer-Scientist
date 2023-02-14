import turtle

def drawtriangle(t, sz):
    """Faz uma tartaruga t desenhar um triangulo de lado sz."""

    for i in range(3):
        t.forward(sz)
        t.left(120)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()

drawtriangle(tess, 50)

wn.exitonclick()
