import turtle

def desenhaQuadrado(t, tam):
    """Faça a tartaruga desenhar um quadrado de lado tam."""

    for i in range(4):
        t.forward(tam)
        t.left(90)

wn = turtle.Screen()            # Inicializa a janela e seus atributos
wn.bgcolor('lightgreen')

alex = turtle.Turtle()          # Cria a tartaruga Alex
desenhaQuadrado(alex, 50)       # Chama a função e desenha um quadrado

alex.penup()
alex.goto(100, 100)
alex.pendown()

desenhaQuadrado(alex, 75)       # Chama a função e desenha outro quadrado

wn.exitonclick()
