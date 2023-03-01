import turtle
from plotbar import desenhaBarra

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

for start in range(1, 51):
    desenhaBarra(alex, seq3np1(start))

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.setworldcoordinates(-10, -10, 40 * 50 + 10, 110)

alex = turtle.Turtle()

wn.exitonclick()
