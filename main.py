### Import statements cus I need those
import math as m
import turtle as trtl
import re
### Imports End

### Personalization Start
# Colors (use words or hex code)
whiteboard_color = 'black'
axis_color = 'white'
graph_color = 'red'
# Scale for ticks (number of turtle units between ticks)
# Recommended value: 50
scale_factor = 50
# Width of each tick
# Recommended value: 10
tick_size = 10
# Constants for turtle window
# Recommended values: +/- 1000 +/- 800
right_bound = 1000
left_bound = -1000
top_bound = 800
bottom_bound = -800
graph_width = right_bound - left_bound
# Resolution (points plotted)
# Recommened value: 200 (range 1-1000)
resolution = 200
# Initializing values for graphing
x = left_bound
### Personalization End

### Lists for filter
filter_list = [r'(sine|sin)\(?', r'(cosine|cos)\(?', r'(tangent|tan)\(?', r'e\^\(?']
replace_list = ['m.sin(', 'm.cos(', 'm.tan(', 'm.exp(']
### End Lists

### Defining functions
# Regex to replace text
def re_replace(equation):
    # Run through list of filters and replaces them accordingly
    for filter_id in range(len(filter_list)):
        neweq = re.sub(filter_list[filter_id], replace_list[filter_id], equation)
    return neweq

# Set-up axis for graph
def draw_axis():
    global pen
    # Lines for the axis
    pen.penup()
    pen.goto(0, bottom_bound)
    pen.pendown()
    pen.goto(0, top_bound)
    pen.penup()
    pen.goto(left_bound, 0)
    pen.pendown()
    pen.goto(right_bound, 0)

# draw_tick() ends with the pen up and heading 0
def draw_tick():
    global pen, tick_size
    pen.pendown()
    for side in range(4):
        pen.forward(tick_size)
        pen.right(180)
        pen.forward(tick_size)
        pen.left(90)
    pen.penup()
    pen.setheading(0)

'''
Proposed new draw tick to increase eff
Need to adj draw_tick_marks() to use properly
def draw_tick():
    global pen, tick_size
    pen.pendown()
    pen.left(90)
    pen.forward(tick_size)
    pen.left(180)
    pen.forward(tick_size*2)
    pen.penup()
    pen.setheading(0)
'''

# Ends with pen up (as result of draw_tick())
def draw_tick_marks():
    global pen, scale_factor
    pen.penup()
    pen.goto(0, 0)
    for tick in range(int(right_bound/scale_factor)):
        if tick == 0:
            draw_tick()
        elif tick <= 10:
            pen.penup()
            pen.goto(scale_factor*tick, 0)
            draw_tick()
            pen.goto(0, scale_factor*tick)
            draw_tick()
            pen.goto(scale_factor*tick*-1, 0)
            draw_tick()
            pen.goto(0, scale_factor*tick*-1)
            draw_tick()
        else:
            pen.penup()
            pen.goto(scale_factor*tick, 0)
            draw_tick()
            pen.goto(scale_factor*tick*-1, 0)
            draw_tick()

'''
editing above function for later use
global pen, scale_factor
pen.penup()
pen.goto(0, 0)
for tick in range(int(1000/scale_factor)):
    if tick == 0:
        draw_tick()
    elif tick <= 10:
        pen.penup()
        pen.goto(scale_factor*tick, 0)
        draw_tick()
        pen.goto(0, scale_factor*tick)
        draw_tick()
        pen.goto(scale_factor*tick*-1, 0)
        draw_tick()
        pen.goto(0, scale_factor*tick*-1)
        draw_tick()
    else:
        pen.penup()
        pen.goto(scale_factor*tick, 0)
        draw_tick()
        pen.goto(scale_factor*tick*-1, 0)
        draw_tick()
'''

# Ends with pen up (as result of draw_tick_marks())
def setup_graph():
    draw_axis()
    draw_tick_marks()

def graph_rect_function(eq):
    global pen, scale_factor, x, y, graph_width
    x /= scale_factor
    y = eval(eq)
    pen.color(graph_color)
    pen.penup()
    x *= scale_factor
    y *= scale_factor
    pen.goto(x, y)
    pen.pendown()
    for x_value in range(resolution):
        x/= scale_factor
        y = eval(eq)
        x *= scale_factor
        y *= scale_factor
        pen.goto(x, y)
        x += graph_width/resolution

def graph_parametric_function(xeq, yeq, t_min, t_max):
    global pen, scale_factor, x, y, graph_width
    t = t_min
    for t in (t_max-t_min):
        x = eval(xeq)
        y = eval(yeq)
        pen.goto(x, y)



def start(eq_type):
    if eq_type == 'R' or 'r':
        equation = input('(in terms of x) y=')
        euqation = re_replace(equation)
        graph_rect_function(equation)
    if eq_type == 'P' or 'p':
        x_equation = input('(in terms of t) x=')
        x_equation = re_replace(x_equation)
        y_equation = input('(in terms of t) y=')
        y_equation = re_replace(y_equation)
        print('What is your range (in terms of t)')
        t_minimum = int(input('Minimum Range: '))
        t_maximum = int(input('Maximum Range: '))
        graph_parametric_function(x_equation, y_equation, t_minimum, t_maximum)

### End function defining

### Set-Up Turtle Program
## Pen Set-Up
pen = trtl.Turtle()
pen.color(axis_color)
pen.speed(0)

## Window Set-Up
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgcolor(whiteboard_color)

### End turtle Set-Up

print('What type of equation would you like to graph? Rectangular (y=...) or Parametric (x=...; y=...)')
eq_type = input('R/P: ')
start(eq_type)

wn.mainloop()