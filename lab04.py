import turtle
import math
import random
"""PUT YOUR FUNCTIONS HERE"""
def draw_axis():
    t.penup()
    t.goto(0, 300)
    t.pendown()
    t.right(90)
    t.forward(600)
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.left(90)
    t.forward(600)

def draw_square(t,length, angle):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(angle)


def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
def draw_ground(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    draw_square(t,600,-90)
    t.end_fill()



def draw_eye(t, x, y, length):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, length)
    t.end_fill()

def draw_pumpkin(t, x, y, radius, length):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    #t.fillcolor("orange")
    #t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem#
    #t.fillcolor("green")
    #t.begin_fill()
    t.penup()
    base = radius // 5
    side = radius // 2
    t.goto(x+base//2,y+radius*2)
    t.pendown()
    t.left(90)  # Point upwards
    t.forward(side)
    t.left(90)
    t.forward(base)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(base)
    t.end_fill()
    #x= 0
    #y= -100
    #r= 100
    #l= 35
    #           0-100, -100+(2*100)-(100/1.5), L
    draw_eye(t, x-radius//2, y+(2*radius)-(radius//1.3), length)
    draw_eye(t, (x +radius//2) - length, y +(2*radius)-(radius//1.3), length)
    #nose
    draw_eye(t, x - length/2, y+radius-length//2, length)
    draw_mouth(t, x - radius//2, y + radius*.65, radius)

def draw_polyline(n, length, angle):  # This is really generalized and flexible now.
     for i in range(n):
        t.forward(length)
        t.right(angle)

def draw_arc(radius, angle):  # Similar to circle, but can do fractional circles.
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    draw_polyline(n, length, step_angle)

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.right(30)
    draw_arc(width//2, 190)
    t.left(10)
    t.end_fill()

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(50, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def draw_jack(x,y,r):
    #x=-200
    #y=-100
    #r = 80
    l= .33 * r
    draw_pumpkin(t,x,y,r,l)

#t = turtle.Turtle()

#t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
#t.color('black')
#t.shape('turtle')


#screen = turtle.Screen()
#screen.bgcolor("white")
#screen.setup(width=600, height=600)

#t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
#draw_axis()

#draw_ground(-300,-100)

# Example usage
#draw_star(t, -100, 150, 30)  # Star in the sky
#draw_star(t, 100, 180, 20)



#draw_sky(t, 10)  # Draw 20 stars

#draw_mouth(t, 0, 0,200)
#draw_jack(-200,-100,100)
#draw_jack(-200,-100,100)
#x=-200
#y=-100
#r = 80
#l= .33 * r
#draw_pumpkin(t,x,y,r,l)



#draw_eye(t,x-50,y+125,35)
#draw_eye(t,x+15, y+125,35)
#draw_nose = draw_eye(t,x-17,y+85,35)
#draw_mouth(t,x-50,y+75,100)

#draw_pumpkin(t,x+200,y,100)






turtle.exitonclick()