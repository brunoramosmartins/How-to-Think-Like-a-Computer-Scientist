import turtle as tu

roo = tu.Turtle() # Turtle Object
wn = tu.Screen() # Screen Object
wn.bgcolor("black")
wn.title("Fractal Tree Pattern")
roo.left(90)
roo.speed(20)

def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")
        roo.forward(l)
        roo.left(30)
        draw(3*1/4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)

draw(20)

roo.right(90)
roo.speed(20000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta") #magenta
        roo.forward(l)
        roo.left(30)
        draw(3*l/4)
        roo.right(60)
        draw(3*l/4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw (20)


roo.left(270)
roo.speed(20000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("red") #red
        roo.forward(l)
        roo.left(30)
        draw(3*l/4)
        roo.right(60)
        draw(3*l/4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw (20)

roo.right(90)
roo.speed(200000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC') #white
        roo.forward(l)
        roo.left(30)
        draw(3*l/4)
        roo.right(60)
        draw(3*l/4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(20)
########################################################

def  draw(l):
    if(l<10):
        return
    else:

        roo.pensize(3)
        roo.pencolor("lightgreen") #lightgreen
        roo.forward(l)
        roo.left(30)
        draw(4*l/5)
        roo.right(60)
        draw(4*l/5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)

draw (40)

roo.right(90)
roo.speed(200000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("red") #red
        roo.forward(l)
        roo.left(30)
        draw(4*l/5)
        roo.right(60)
        draw(4*l/5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)

draw (40)


roo.left(270)
roo.speed(200000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("yellow") #yellow
        roo.forward(l)
        roo.left(30)
        draw(4*l/5)
        roo.right(60)
        draw(4*l/5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)

draw (40)

roo.right(90)
roo.speed(200000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(3)
        roo.pencolor('#FFF8DC') #white
        roo.forward(l)
        roo.left(30)
        draw(4*l/5)
        roo.right(60)
        draw(4*l/5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)

draw (40)

########################################################
def  draw(l):
    if(l<10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("cyan") #cyan
        roo.forward(l)
        roo.left(30)
        draw(6*l/7)
        roo.right(60)
        draw(6*l/7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw (60)

roo.right(90)
roo.speed(200000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow") #yellow
        roo.forward(l)
        roo.left(30)
        draw(6*l/7)
        roo.right(60)
        draw(6*l/7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw (60)


roo.left(270)
roo.speed(200000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta") #magenta
        roo.forward(l)
        roo.left(30)
        draw(6*l/7)
        roo.right(60)
        draw(6*l/7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw (60)

roo.right(90)
roo.speed(200000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC') #white
        roo.forward(l)
        roo.left(30)
        draw(6*l/7)
        roo.right(60)
        draw(6*l/7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)
draw(60)
wn.exitonclick()
