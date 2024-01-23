from math import sqrt

def square_window(myTurtle, size, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("white")
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
    myTurtle.end_fill()
    myTurtle.penup()
    myTurtle.forward(size/2)
    myTurtle.left(270)
    myTurtle.pendown()
    myTurtle.forward(size)
    myTurtle.penup()
    myTurtle.goto(x, y - size/2)
    myTurtle.setheading(0)
    myTurtle.pendown()
    myTurtle.forward(size)
    
def round_window(myTurtle, radius, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("white")
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()
    myTurtle.right(270)
    myTurtle.forward(2*radius)
    myTurtle.penup()
    myTurtle.setheading(180)
    myTurtle.circle(radius, 90)
    myTurtle.setheading(0)
    myTurtle.pendown()
    myTurtle.forward(2*radius)
    

def doorknob(myTurtle, radius, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("yellow")
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()

def front_door(myTurtle, length, width, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("brown")
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    for i in range(2):
        myTurtle.forward(width)
        myTurtle.left(90)
        myTurtle.forward(length)
        myTurtle.left(90)
    myTurtle.end_fill()
    doorknob(myTurtle, length/16, x + (3*width)/4, y + length/2)

def garage_door(myTurtle, length, width, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("silver")
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    for i in range(2):
        myTurtle.forward(width)
        myTurtle.left(90)
        myTurtle.forward(length)
        myTurtle.left(90)
    myTurtle.end_fill()

def house_outline(myTurtle, length, width, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("pink")
    myTurtle.goto(x, y)
    myTurtle.pendown()
    for i in range(2):
        myTurtle.begin_fill()
        myTurtle.forward(width)
        myTurtle.left(90)
        myTurtle.forward(length)
        myTurtle.left(90)
        myTurtle.end_fill()
    myTurtle.begin_fill()
    myTurtle.penup()
    myTurtle.goto(x, y+length)
    myTurtle.setheading(30)
    myTurtle.pendown()
    myTurtle.forward(width/sqrt(3))
    myTurtle.right(60)
    myTurtle.forward(width/sqrt(3))
    myTurtle.right(150)
    myTurtle.forward(width)
    myTurtle.end_fill()

def cloud(myTurtle, length, width, x, y):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.fillcolor("grey")
    myTurtle.begin_fill()
    numcircles = 3
    angle = 360/numcircles
    for i in range(numcircles):
        myTurtle.circle(width // 2) 
        myTurtle.left(angle)
    myTurtle.end_fill()

def tree(myTurtle, length, width, x, y):
    #trunk
    myTurtle.penup() 
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.fillcolor("brown")
    myTurtle.begin_fill()
    for _ in range(2):
        myTurtle.forward(width)  # Width of the trunk
        myTurtle.left(90)
        myTurtle.forward(length)  # Height of the trunk
        myTurtle.left(90)
    myTurtle.end_fill()

    #top of tree as one large triangle.
    myTurtle.penup()
    myTurtle.goto(x - width, y + length)
    myTurtle.pendown()
    myTurtle.fillcolor("lightgreen")
    myTurtle.begin_fill()
    treetop_side_length = width * 3  # relative to width.
    for _ in range(3):
        myTurtle.forward(treetop_side_length)  #triangle side length.
        myTurtle.left(120)
    myTurtle.end_fill() 

def sun(myTurtle, radius, x, y):
    myTurtle.penup()
    myTurtle.goto(x - radius, y)
    myTurtle.setheading(0)
    myTurtle.fillcolor("yellow")
    myTurtle.begin_fill()
    myTurtle.circle(radius, 90)
    myTurtle.goto(x, y)
    myTurtle.goto(x - radius, y)
    myTurtle.end_fill()
