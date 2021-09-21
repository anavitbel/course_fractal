import turtle
from datetime import datetime
from conv import *
from palette_names import *


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def fold(direction):
    if direction == 0:
        p.right(90)
    else:
        p.left(90)


def next(chain):
    chain.append(1)
    length = len(chain)
    for i in range(0, length - 1):
        chain.append(chain[i])
    if chain[length - 1 + int(length / 2)] == 0:
        chain[length - 1 + int(length / 2)] = 1
    else:
        chain[length - 1 + int(length / 2)] = 0
    return chain


def draw(chain):
    turtle.tracer(100)
    p.hideturtle()
    for i in chain:
        p.forward(2)
        fold(i)
    p.forward(2)
    turtle.update()


def find_iteration(n):
    chain = [1]
    for i in range(1, n):
        chain = next(chain)
    return chain


def set_pos(pos):
    p.penup()
    p.goto(pos)
    p.pendown()

palette = palette_selection(20)

def draw_background(a_turtle):
    """Draw a background rectangle."""
    ts = a_turtle.getscreen()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    a_turtle.penup()
    a_turtle.speed(0)  # fastest
    a_turtle.goto(-width/2-2, -height/2+3)
    a_turtle.fillcolor(rgb_to_hex(palette[0]))
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(width)
    a_turtle.setheading(90)
    a_turtle.forward(height)
    a_turtle.setheading(180)
    a_turtle.forward(width)
    a_turtle.setheading(270)
    a_turtle.forward(height)
    a_turtle.end_fill()
    a_turtle.hideturtle()


t = turtle.Turtle()

draw_background(t)
ts = t.getscreen()
canvas = ts.getcanvas()

it_b = 16
it_s = 12
p = turtle.Pen()

for i in range(1, 9, 2):
    n_c = i * 2 - 1
    p.color(rgb_to_hex(palette[i]))
    draw(find_iteration(it_b))
    """
    pos_mem = tuple(p.pos())
    p.left(90)
    for _ in range(2):
        n_c += 1
        p.color(rgb_to_hex(palette[n_c]))
        draw(find_iteration(it_s))
        set_pos(pos_mem)
    # it_b -= 1
    set_pos((0, 0))
    p.left(180)
    """
    p.right(90)
    p.color(rgb_to_hex(palette[i + 1]))
    draw(find_iteration(it_b))
    set_pos((0, 0))
    p.left(180)
    it_b -= 1






now = datetime.now()
file_name = now.strftime("%d-%m-%Y %H.%M.%S") + '.eps'


canvas.postscript(file=file_name)
conv_from_eps_to_img(file_name)
