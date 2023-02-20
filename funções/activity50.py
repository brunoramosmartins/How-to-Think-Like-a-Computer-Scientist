import turtle


def desenhaEstrela(t, tam, pontas):
    """Desenha uma estrela com lados tam e quantidades de pontas."""

    angle = (pontas -1)*180/pontas
    for i in range(pontas):
        t.forward(tam)
        t.right(angle)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

alex = turtle.Turtle()
for i in range(5):
    desenhaEstrela(alex, 100, 5)
    alex.penup()
    alex.forward(350)
    alex.right(144)
    alex.pendown()

wn.exitonclick()
