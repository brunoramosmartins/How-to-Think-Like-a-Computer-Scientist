import turtle
from turtle import *

def starDraw(t, tam, n):
    """
    Desenha uma estrela de lado tam e n pontas.
    """
    angle = 180 - 180/(2*n)
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(angle)
        if abs(pos()) < 1:
            break
    end_fill()

wn = turtle.Screen()
wn.bgcolor('lightgreen')

alex = turtle.Turtle()

starDraw(alex, 100, 6)

wn.exitonclick()
