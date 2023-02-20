import turtle


def desenhaEstrela(t, tam, pontas):
    """Desenha uma estrela com lados tam e quantidades de pontas."""

    angle = (pontas -1)*180/pontas
    for i in range(pontas):
        t.forward(tam)
        t.left(angle)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

alex = turtle.Turtle()

desenhaEstrela(alex, 100, 5)

wn.exitonclick()
