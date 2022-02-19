from turtle import *

speed(10)

# These two variables call two turtles.
turtle_1 = Turtle()
turtle_2 = Turtle()

def callback_1(x,y):
    color("black")
    shape("turtle")
    
def callback_2(x,y):
    color("brown")
    shape("triangle")
    circle(100, steps=3)

# These two lines of code choose color of turtles.
turtle_1.color("black")
turtle_2.color("brown")

# These two lines of code choose shape of turtles.
turtle_1.shape("turtle")
turtle_2.shape("triangle")

# This function makes turtle_1 draw a square.
def draw_square_1():
    turtle_1.setheading(270)
    turtle_1.circle(100,steps=4)

# This function makes turtle_2 draw a hexagon.
def draw_hexagon_2():
    turtle_2.setheading(90)
    turtle_2.circle(150,steps=6)

# This function moves turtle_2 to a new location.
def move_turtle_2():
    turtle_2.penup()
    turtle_2.goto(-200,200)
    turtle_2.pendown()

# This function defines turtles location after reset.
def place_turtles():
    turtle_1.color("black")
    turtle_1.shape("turtle")
    turtle_1.penup()
    turtle_1.goto(0,0)
    turtle_1.pendown()
    turtle_2.color("brown")
    turtle_2.shape("triangle")
    turtle_2.penup()
    turtle_2.goto(0,0)
    turtle_2.pendown()
    
# This function resets screen.
def start_over():
    resetscreen()
    place_turtles()

def stop():
    stop()
        
listen()

# The functions below moves the turtles or draws a shape when certain keys are pressed.
onkey(draw_square_1, "s")
onkey(move_turtle_2,"m")
onkey(draw_hexagon_2, "h")
onkey(bye,"Escape")
onkey(start_over,"space")
onkey(stop,"Home")

place_turtles()
