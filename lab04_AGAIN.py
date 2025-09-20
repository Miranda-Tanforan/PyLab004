import turtle

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
        t.left(90)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    #t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    t.penup()
    t.goto(x + (radius//5)//2 ,y + radius*2)
    t.pendown()
    t.fillcolor("green")
    #t.begin_fill()
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
    #t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    #t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()


t = turtle.Turtle()

t.speed(10)  # 1 is slow, 10 is fast, 0 is instant

screen = turtle.Screen()
screen.bgcolor("white")

screen.setup(width=600, height=600)
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

draw_axis()

x = 0
y = -100
r = 100
s= .33 * r
#draw_pumpkin(t, x, y, r)
#        (t,x,y,size)
#draw_eye(t, x - (.33 * r) * 1.5, y + r + r*.25,s)
#draw_eye(t, x + (.33 * r) * 0.5  , y + r + r * 0.25, 35)
#draw_mouth(t, x - r * 0.5 , y + r * 0.75, r)


def draw_jack(t,x,y,r):
    s = .33 * r
    draw_pumpkin(t, x, y, r)
    draw_eye(t, x - (.33 * r) * 1.5, y + r + r *.25, s)
    draw_eye(t, x + (.33 * r) * 0.5  , y + r + r * 0.25, 35)
    #draw_eye(t,x,y,35)
    draw_mouth(t, x - r * 0.5 , y + r * 0.75, r)

draw_jack(t,0,-100,100)
turtle.exitonclick()