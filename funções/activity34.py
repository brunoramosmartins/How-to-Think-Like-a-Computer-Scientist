import turtle

def desenhaRetangulo(t, w, h):
    """Faca a tartaruga t desenhar um retangulo de largura w e altura h."""

    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def desenhaQuadrado(tx, tam):
    """Uma nova versao de desenhaQuadrado."""
    desenhaRetangulo(tx, tam, tam)

wn = turtle.Screen()                              # Inicializa a janela
wn.bgcolor('lightgreen')

tess = turtle.Turtle()

desenhaQuadrado(tess, 50)

wn.exitonclick()
