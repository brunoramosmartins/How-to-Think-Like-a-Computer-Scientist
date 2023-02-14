import turtle

def desenhaQuadrado(t, tam):
    """Faça a tartaruga t desenhar um quadrado de lado tam."""

    for i in range(4):
        t.forward(tam)
        t.left(90)

wn = turtle.Screen()        # Inicia a janela e seus atributos
wn.bgcolor('lightgreen')    # Define a cor

alex = turtle.Turtle()      # cria uma tartaruga chamada Alex
desenhaQuadrado(alex, 50)   # chama a função para desenhar um quadrado

wn.exitonclick()
