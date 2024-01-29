from math import sqrt

#square windows.
def square_window(myTurtle, size, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("#FFFFFF")
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

#round window at the top of the house.  
def round_window(myTurtle, radius, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("#FFFFFF")
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
    
#doorknob helper function for the front door function below.
def doorknob(myTurtle, radius, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("#FFFF00")
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()

def front_door(myTurtle, length, width, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("#A52A2A")
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

#garage doors.
def garage_door(myTurtle, length, width, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("#C0C0C0")
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    for i in range(2):
        myTurtle.forward(width)
        myTurtle.left(90)
        myTurtle.forward(length)
        myTurtle.left(90)
    myTurtle.end_fill()

#draws the frame of the house.
def house_outline(myTurtle, length, width, x, y):
    myTurtle.setheading(0)
    myTurtle.penup()
    myTurtle.fillcolor("#FFC0CB")
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

#cloud code to be re-used multiple times for multiple clouds.
def cloud(myTurtle, radius, x, y):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.fillcolor("#808080")
    myTurtle.begin_fill()
    numcircles = 3
    angle = 360/numcircles
    for i in range(numcircles):
        myTurtle.circle(radius // 2) 
        myTurtle.left(angle)
    myTurtle.end_fill()

#tree to be reiterated in main
def tree(myTurtle, length, width, x, y):
    #trunk
    myTurtle.penup() 
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.fillcolor("#A52A2A")
    myTurtle.begin_fill()
    for _ in range(2):
        myTurtle.forward(width)  
        myTurtle.left(90)
        myTurtle.forward(length) 
        myTurtle.left(90)
    myTurtle.end_fill()

    #top of tree as one large triangle.
    myTurtle.penup()
    myTurtle.goto(x - width, y + length)
    myTurtle.pendown()
    myTurtle.fillcolor("#90EE90")
    myTurtle.begin_fill()
    treetop_side_length = width * 3  
    for _ in range(3):
        myTurtle.forward(treetop_side_length)  #triangle side length.
        myTurtle.left(120)
    myTurtle.end_fill() 

#code for sun in the top-left corner.
def sun(myTurtle, radius, x, y):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.setheading(0)
    myTurtle.fillcolor("#FFFF00")
    myTurtle.begin_fill()
    myTurtle.circle(radius, 90)
    myTurtle.setheading(180)
    myTurtle.forward(radius)
    myTurtle.setheading(270)
    myTurtle.forward(radius)
    myTurtle.end_fill()

