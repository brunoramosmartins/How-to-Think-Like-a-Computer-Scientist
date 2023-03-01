import turtle
from plotbar import desenhaBarra

alex = turtle.Turtle()

def seq3np1(n):
    """
    Print the 3n + 1 sequence from n, terminating when it reaches 1.
    Imprima a sequência 3n+1 de n, terminando quando atingir 1.
    """

    cont = 0
    while n != 1:

        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        cont += 1
    return(cont)

lista = []
for start in range(1, 51):
    lista.append(seq3np1)

for valor in lista:
    desenhaBarra(alex, valor)

alturamax = max(lista)
numbarras = len(lista)
moldura = 10

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.setworldcoordinates(0 - moldura, 0 - moldura, 40 * numbarras + moldura, alturamax + moldura)
wn.exitonclick()
