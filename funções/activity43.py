import turtle

def desenhaPoli(t, numeroLados, tamanho):
    """Desenha um polígono regular com numeroLados lados, cada um com comprimento tamanho."""

    for i in range(numeroLados):
        t.forward(tamanho)
        t.left(360/numeroLados)     # ângulo externo

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()

desenhaPoli(tess, 8, 50)

wn.exitonclick()
