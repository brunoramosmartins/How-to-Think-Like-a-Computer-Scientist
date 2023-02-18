import turtle
import random

# Define as dimensões do quadrado
sq_size = 200

# Cria a janela gráfica
wn = turtle.Screen()
wn.setup(sq_size + 50, sq_size + 50)
wn.setworldcoordinates(-25, -25, sq_size + 25, sq_size + 25)

# Cria a caneta
t = turtle.Turtle()

# Desenha o quadrado
t.penup()
t.goto(0, 0)
t.pendown()
for i in range(4):
    t.forward(sq_size)
    t.left(90)

# Desenha o círculo
t.penup()
t.goto(sq_size/2, sq_size/2)
t.pendown()
t.circle(sq_size/2)

# Define o número de pontos a serem gerados
num_points = 1000

# Inicia a contagem de pontos dentro do círculo
count = 0

# Gera pontos aleatórios e conta quantos estão dentro do círculo
for i in range(num_points):
    x = random.uniform(0, sq_size)
    y = random.uniform(0, sq_size)
    dist = ((x - sq_size/2)**2 + (y - sq_size/2)**2)**0.5
    if dist < sq_size/2:
        count += 1
        t.penup()
        t.goto(x, y)
        t.dot()

# Calcula a aproximação para pi
approx_pi = 4 * count / num_points

print("Aproximação para pi:", approx_pi)

turtle.done()
