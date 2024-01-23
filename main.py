if __name__ == "__main__":
    #import necessary librarires
    import turtle
    from shapes import *

    WIDTH=1600
    HEIGHT=1600
    #screen
    myTurtle = turtle.Turtle()
    myTurtle.speed(100)
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT) 
    WIDTH = screen.window_width()
    HEIGHT = screen.window_height()
    print(screen.window_height())  
    screen.bgcolor('lightblue')

    #executes all of the functions from shapes.py following import. 
    myTurtle.penup()
    myTurtle.goto(-0.6*WIDTH, -0.25*HEIGHT)
    myTurtle.pendown()
    myTurtle.forward(1.25*WIDTH)
    print(screen.window_height())
    house_outline(myTurtle, (3/16)*HEIGHT, (3/8)*WIDTH, -(3/8)*WIDTH, -(1/4)*HEIGHT)
    garage_door(myTurtle, (1/16)*HEIGHT, (7/64)*WIDTH, -(11/32)*WIDTH, -(1/4)*HEIGHT)
    garage_door(myTurtle, (1/16)*HEIGHT, (7/64)*WIDTH, -(13/64)*WIDTH, -(1/4)*HEIGHT)
    front_door(myTurtle, (3/64)*HEIGHT, (1/32)*WIDTH, -(1/16)*WIDTH, -(1/4)*HEIGHT)
    square_window(myTurtle, (1/32)*HEIGHT, -(21/64)*WIDTH, -(7/64)*HEIGHT)
    square_window(myTurtle, (1/32)*HEIGHT, -(13/64)*WIDTH, -(7/64)*HEIGHT)
    square_window(myTurtle, (1/32)*HEIGHT, -(5/64)*WIDTH, -(7/64)*HEIGHT)
    round_window(myTurtle, (1/64)*HEIGHT, -(3/16)*WIDTH, -(3/64)*HEIGHT)
    tree(myTurtle, (1/64)*HEIGHT, (3/64)*WIDTH, (3/32)*WIDTH, -(1/4)*HEIGHT)
    tree(myTurtle, (1/64)*HEIGHT, (3/64)*WIDTH, (9/32)*WIDTH, -(1/4)*HEIGHT)
    cloud(myTurtle, (1/16)*HEIGHT, -(1/4)*WIDTH, (3/16)*HEIGHT)
    cloud(myTurtle, (1/16)*HEIGHT, 0, (3/16)*HEIGHT)
    sun(myTurtle, (1/8)*HEIGHT, -WIDTH/2, (3/8)*HEIGHT)
    turtle.done()