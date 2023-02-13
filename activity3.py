import turtle

def desenhaQuadradoMulticolorido(t, tam):
    """Faça a tartaruga t desenhar um quadrado multicolorido de lado tam."""
    for i in ['red', 'purple', 'hotpink', 'blue']:
        t.color(i)
        t.forward(tam)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.pensize(3)

tamanho = 20            # Tamanho do menor quadrado
for i in range(15):
    desenhaQuadradoMulticolorido(tess, tamanho)
    tamanho = tamanho + 10
    tess.forward(10)
    tess.right(18)

wn.exitonclick()
