import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightblue')

andy = turtle.Turtle()
bruno = turtle.Turtle()

andy.color("red")
bruno.color("green")

andy.shape("turtle")
bruno.shape("turtle")

andy.up()
bruno.up()

andy.goto(-100, 20)
bruno.goto(-100, -20)

wn.exitonclick()
