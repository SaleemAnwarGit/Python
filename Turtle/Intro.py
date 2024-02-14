import turtle
import random


def CreateWindow(title, bgcolor):
    Screen = turtle.Screen()      #creates a graphics window as win
    Screen.title(title)   #giving the title as 'Hello World'
    Screen.bgcolor()
    Screen.bgcolor(bgcolor)  #Assign the light blue colour to window

    turta = turtle.Turtle()   #I gave the name turta for my turtle
    
    return turta

def DrawH(Screen, Xpos, Ypos, Size):
    Screen.color("black")      # make turta black (default color)
    Screen.pensize(4)          # set the width of turta as 4
    Screen.speed(10)           # The speed is set to 10
    # Draw H
    Screen.left(90)    # turn anti clockwise by 90 degrees
    Screen.forward(Size*10) # go up by 70 units
    Screen.penup()     # take the pen up
    Screen.goto(Xpos, Ypos) # go to the place of (0,35) from the beginning
    Screen.down()      # put the pen down to start drawing
    Screen.right(Size*10)   # turn clockwise by 90 degrees
    Screen.color("green")      # make turta black (default color)
    Screen.pensize(4)          # set the width of turta as 4
    Screen.speed(10)           # The speed is set to 10
    Screen.forward(30) # go to rightside by 30 units
    Screen.penup()     # take the pen up
    Screen.goto(30, 70)# go to the place of (30,70) from the beginning
    Screen.pendown()   # put the pen down to start drawing
    Screen.right(90)   # turn clockwise by 90 degrees
    Screen.forward(70) # go down and you can see letter 'H'

def DrawI(Screen):
    Screen.color("black")      # make turta black (default color)
    Screen.pensize(4)          # set the width of turta as 4
    Screen.speed(10)           # The speed is set to 10
    # Draw H
    Screen.left(90)    # turn anti clockwise by 90 degrees
    Screen.forward(70) # go up by 70 units
    Screen.penup()     # take the pen up
    Screen.goto(0, 35) # go to the place of (0,35) from the beginning
    Screen.down()      # put the pen down to start drawing
    Screen.right(90)   # turn clockwise by 90 degrees
    Screen.color("green")      # make turta black (default color)
    Screen.pensize(4)          # set the width of turta as 4
    Screen.speed(10)           # The speed is set to 10
    Screen.forward(30) # go to rightside by 30 units
    Screen.penup()     # take the pen up
    Screen.goto(30, 70)# go to the place of (30,70) from the beginning
    Screen.pendown()   # put the pen down to start drawing
    Screen.right(90)   # turn clockwise by 90 degrees
    Screen.forward(70) # go down and you can see letter 'H'

def DrawSomething(Screen):
    #Screen.speed(1)
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            Screen.color(c)
            Screen.forward(steps)
            Screen.right(30)


def DrawLeaf():
    screen = turtle.Screen()
    screen.title('Barnsley\'s Fern Chaos Game with Python Turtle')
    screen.setup(1000,1000)
    screen.setworldcoordinates(-6,-1,6,11)
    screen.tracer(0,0)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.up()
    n = 100000 # number of points to draw
    p = (0,0) 
    t = turtle.Turtle()
    t.up()
    t.hideturtle()
    for i in range(n):
        t.goto(p)
        t.dot(2,'green') 
        r = random.uniform(0,1)
        if r < 0.01:
            p = (0,0.16*p[1])
        elif r < 0.86:
            p = (0.85*p[0] + 0.04*p[1], -0.04*p[0] + 0.85*p[1] + 1.6)
        elif r < 0.93:
            p = (0.2*p[0] - 0.26*p[1], 0.23*p[0] + 0.22*p[1] + 1.6)
        else:
            p = (-0.15*p[0] + 0.28*p[1], 0.26*p[0] + 0.24*p[1] + 0.44)
            
        if i % 1000 == 0: # update for every 1000 moves, this part is for performance reason only
            t = turtle.Turtle() # use new turutle
            t.up()
            t.hideturtle()
            screen.update()


def Shape1(arrow):
    arrow.penup()  # take the pen up
    arrow.goto(-100, 100) # go to the place of (0,35) from the beginning
    arrow.down() 
    arrow.speed(10) 
    arrow.right(90) #down
    arrow.forward(100)
    arrow.left(45) #lover begin
    arrow.forward(75)
    arrow.left(90) # v
    arrow.forward(75)
    arrow.left(45) # lower end
    arrow.forward(100)
    arrow.left(135)
    arrow.forward(75)
    arrow.right(90)
    arrow.forward(75)



Screen = CreateWindow("Hello World","light blue")
DrawH(Screen, -100,100, 9)
#Shape1(Screen)
#DrawSomething(Screen)
#DrawLeaf()
#DrawHouse(Screen)
turtle.done()
