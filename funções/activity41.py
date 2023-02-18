import turtle

def desenhaQuadrado(t, tam):
    """Faca a tartaruga t desenhar um quadrado de  lado tam."""

    for i in range(4):
        t.forward(tam)
        t.left(90)


wn = turtle.Screen()        # Inicializa a janela e seus atributos.
wn.bgcolor('lightgreen')

alex = turtle.Turtle()

for quantidade in range(5):
    desenhaQuadrado(alex, 20)
    alex.penup()
    alex.forward(40)
    alex.pendown()

wn.exitonclick()
