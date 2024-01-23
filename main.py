if __name__ == "__main__":
    #import necessary librarires
    import turtle
    from shapes import *

    #screen
    myTurtle = turtle.Turtle()
    myTurtle.speed(100)
    screen = turtle.Screen()
    screen.setup(width=1600, height=1600)   
    screen.bgcolor('lightblue')

    #executes all of the functions from shapes.py following import. 
    myTurtle.penup()
    myTurtle.goto(-1000, -400)
    myTurtle.pendown()
    myTurtle.forward(2000)
    house_outline(myTurtle, 300, 600, -600, -400)
    garage_door(myTurtle, 100, 175, -550, -400)
    garage_door(myTurtle, 100, 175, -325, -400)
    front_door(myTurtle, 75, 50, -100, -400)
    square_window(myTurtle, 50, -525, -175)
    square_window(myTurtle, 50, -325, -175)
    square_window(myTurtle, 50, -125, -175)
    round_window(myTurtle, 25, -300, -75)
    tree(myTurtle, 25, 75, 150, -400)
    tree(myTurtle, 25, 75, 450, -400)
    cloud(myTurtle, 100, -400, 300)
    cloud(myTurtle, 100, 0, 300)
    sun(myTurtle, 200, -screen.window_width()/2, screen.window_height()/2-200)
    turtle.done()