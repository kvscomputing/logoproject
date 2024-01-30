#import necessary librarires
import turtle
from shapes import *
from PIL import Image

CANVAS_SIZE = (1000, 1000)

if __name__=='__main__':
    # #screen
    myTurtle = turtle.Turtle()
    myTurtle.speed(100)
    screen = turtle.Screen()
    screen.setup(width=CANVAS_SIZE[0], height=CANVAS_SIZE[1])   
    screen.bgcolor('lightblue')

    #executes all of the functions from shapes.py following import. 
    # myTurtle.penup()
    # myTurtle.goto(-1000, -400)
    # myTurtle.pendown()
    # myTurtle.forward(2000)
    house_outline(myTurtle, 3*screen.window_height()/16, 3*screen.window_width()/8, -3*screen.window_width()/8, -screen.window_height()/4)
    garage_door(myTurtle, screen.window_height()/16, 7*screen.window_width()/64, -11*screen.window_width()/32, -screen.window_height()/4)
    garage_door(myTurtle, screen.window_height()/16, 7*screen.window_width()/64, -13*screen.window_width()/64, -screen.window_height()/4)
    front_door(myTurtle, 3*screen.window_height()/64, screen.window_width()/32, -screen.window_width()/16, -screen.window_height()/4)
    square_window(myTurtle, screen.window_width()/32, -21*screen.window_width()/64, -7*screen.window_height()/64)
    square_window(myTurtle, screen.window_width()/32, -13*screen.window_width()/64, -7*screen.window_height()/64)
    square_window(myTurtle, screen.window_width()/32, -5*screen.window_width()/64, -7*screen.window_height()/64)
    round_window(myTurtle, screen.window_width()/64, -3*screen.window_width()/16, -3*screen.window_height()/64)
    tree(myTurtle, screen.window_height()/64, 3*screen.window_width()/64, 3*screen.window_width()/32, -screen.window_height()/4)
    tree(myTurtle, screen.window_height()/64, 3*screen.window_width()/64, 9*screen.window_width()/32, -screen.window_height()/4)
    cloud(myTurtle, screen.window_width()/16, -screen.window_width()/4, 3*screen.window_height()/16)
    cloud(myTurtle, screen.window_width()/16, 0, 3*screen.window_height()/16)
    sun(myTurtle, screen.window_height()/8, -screen.window_width()/2, 3*screen.window_height()/8)

# save turtle image
canvas = myTurtle.getscreen().getcanvas()
canvas.postscript(file= 'House_final.ps')


# Open the PS file
ps_file_path = r'./House_final.ps'
img = Image.open(ps_file_path)

# Save as PNG with a different name
png_file_path = r'./House_final.png'
img.save(png_file_path, 'PNG')