import turtle


def desenhaBarra(t, altura):
    """Faca a tartaruga t desenhar uma barra, de altura `altura`."""

    t.begin_fill()      # comece preenchendo o perfil
    t.left(90)
    t.forward(altura)
    t.write(' ' + str(altura))
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.end_fill()        # pare de preencher o perfil


xs = [48, 117, 200, 240, 160, 260, 220]
alturamax = max(xs)
numbarras = len(xs)
moldura = 10

tess = turtle.Turtle()
tess.color('blue')
tess.fillcolor('red')
tess.pensize(3)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.setworldcoordinates(0-moldura, 0-moldura, 40 * numbarras + moldura, alturamax + moldura)

for a in xs:
    desenhaBarra(tess, a)

wn.exitonclick()
