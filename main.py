### Import statements cus I need those
import math as m
import turtle as trtl
import re
### Imports End

### Personalization Start
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
# Recommended values: +/- 500 +/- 400
right_bound = 500
left_bound = -500
top_bound = 400
bottom_bound = -400
### Personalization End

### Lists for filter
filter_list = [r'(sine|sin)\(?', r'(cosine|cos)\(?', r'(tangent|tan)\(?', r'e\^\(?']
replace_list = ['m.sin(', 'm.cos(', 'm.tan(', 'm.exp(']
### End Lists

# Ask for input equations
equation_input = input('Input equation: ')


### Defining functions
# Regex to replace text
def re_replace():
    global equation_input
    # Run through list of filters and replaces them accordingly
    for filter_id in range(len(filter_list)):
        equation_input = re.sub(filter_list[filter_id], replace_list[filter_id], equation_input)

# Set-up axis for graph
def draw_axis():
    global pen, wn, scale_factor, tick_size
    # Lines for the axis
    pen.penup()
    pen.goto(0, bottom_bound)
    pen.pendown()
    pen.goto(0, top_bound)
    pen.penup()
    pen.goto(left_bound, 0)
    pen.pendown()
    pen.goto(right_bound, 0)

# draw_tick() ends with the pen up
def draw_tick():
    global pen, scale_factor, tick_size
    pen.pendown()
    for side in range(4):
        pen.forward(tick_size)
        pen.right(180)
        pen.forward(tick_size)
        pen.left(90)
    pen.penup()

# Ends with pen up (as result of draw_tick())
def draw_tick_marks():
    global pen, scale_factor
    pen.penup()
    pen.goto(0, 0)
    for tick in range(int(500/scale_factor)):
        pen.penup()
        pen.goto(scale_factor*tick, 0)
        draw_tick()
        pen.goto(0, scale_factor*tick)
        draw_tick()
        pen.goto(scale_factor*tick*-1, 0)
        draw_tick()
        pen.goto(0, scale_factor*tick*-1)
        draw_tick()

# Ends with pen up (as result of draw_tick_marks())
def setup_graph():
    global pen, wn, scale_factor
    draw_axis()
    draw_tick_marks()

def graph_function():
    global pen, wn, scale_factor, equation_input

### End function defining


### Run Replacement
re_replace()

### Set-Up Turtle Program
## Pen Set-Up
pen = trtl.Turtle()
pen.color(axis_color)
pen.speed(0)

## Window Set-Up
wn = trtl.Screen()
wn.bgcolor(whiteboard_color)

### End turtle Set-Up

setup_graph()

wn.mainloop()