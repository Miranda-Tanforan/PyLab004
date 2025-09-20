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

def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.right(90)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

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




def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    t.penup()
    t.goto(x + (radius//5)//2 ,y + radius*2)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()


def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_nose(t,x,y,size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

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
    t.left(60)
    t.forward(200)


def draw_smile(t, x, y, width):
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
    t.right(80)
    t.end_fill()

def draw_jack_o_lantern(t,x,y,r):
    s = 0.33 * r
    n = 0.20 * r
    draw_pumpkin(t, x, y, r)
    draw_eye(t, x - (.33 * r) * 1.5, y + r + r *.25, s)
    draw_eye(t, x + (.33 * r) * 0.5  , y + r + r * 0.25, s)
    draw_nose(t, x - (0.5 * n) , y + r - (0.5 * n), n)
    draw_smile(t, x - r * 0.5 , y + r * 0.75, r)

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
        x = random.randint(0, 300)
        y = random.randint(150, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def draw_ground(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    draw_square(t,600)
    t.end_fill()

def draw_army_large(t, num_jacks):
    for _ in range(num_jacks):
        x = random.randint(-100, 300)
        y = -120
        #y = random.randint(-300, -200)
        size = random.randint(80, 100)
        draw_jack_o_lantern(t, x, y, size)

def draw_army_small(t, num_jacks):
    for _ in range(num_jacks):
        x = random.randint(-100, 300)
        y = random.randint(-250, -150)
        #y = random.randint(-300, -200)
        size = random.randint(30, 50)
        draw_jack_o_lantern(t, x, y, size)

t = turtle.Turtle()

t.speed(0)  # 1 is slow, 10 is fast, 0 is instant

t.shape("turtle")
screen = turtle.Screen()
screen.bgcolor("darkblue")

screen.setup(width=600, height=600)
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

#draw_axis()

draw_ground(-300,-100)
draw_jack_o_lantern(t,-300, -200,300)
draw_army_large(t,4)
draw_army_small(t,10)
draw_sky(t,20)

turtle.exitonclick()