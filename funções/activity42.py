import turtle

def desenhaQuadrado(t, tam):
    """Faca a tartaruga t desenhar um quadrado de  lado tam."""

    for i in range(4):
        t.forward(tam)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor('lightgreen')

alex = turtle.Turtle()

lado = 20
for i in range(5):
    desenhaQuadrado(alex, lado)
    alex.penup()
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.backward(10)
    alex.pendown()

    lado += 20

wn.exitonclick()
