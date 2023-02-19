import turtle

def desenhaQuadrado(t, tam):
    """Desenha um quadrado de lado tam."""

    for i in range(4):
        t.forward(tam)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor('lightgreen')

alex = turtle.Turtle()

for i in range(18):
    desenhaQuadrado(alex, 100)
    alex.left(20)

wn.exitonclick()
