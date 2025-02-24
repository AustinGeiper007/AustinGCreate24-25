### Import statements cus I need those
# There will be an error saying import math as m is unused and shouldn't be there
# That would be incorrect, it's just stored in strings, so it's not being seen properly
import math as m
import turtle as trtl
import re
### Imports End

### Personalization Start
# Colors (use words or hex code)
whiteboard_color = 'black'
axis_color = 'white'
graph_colors = ['red', 'blue', 'magenta', 'green', 'orange', 'brown']
graph_color = 'red'
# Scale for ticks (number of turtle units between ticks)
# Recommended value: 50
scale_factor = 50
# Width of each tick
# Recommended value: 10
tick_size = 10
# Constants for turtle window
# Recommended values: +/- 1000 +/- 800
screen_width = 1000
right_bound = screen_width / 2
left_bound = right_bound * -1
screen_height = 800
top_bound = screen_height / 2
bottom_bound = top_bound * -1
graph_width = right_bound - left_bound
# Resolution (points plotted)
# Recommended value: 200 (range 1-1000)
resolution = 500
### Personalization End

### Lists for filter
filter_list = [r'(sine|sin)\(?', r'(cosine|cos)\(?', r'(tangent|tan)\(?', r'e\^\(?', r'pi', r'\^']
replace_list = ['m.sin(', 'm.cos(', 'm.tan(', 'm.exp(', 'm.pi', '**']
### End Lists

### Defining functions
# Regex to replace text
def regex_replace(equation):
    # Run through list of filters and replaces them accordingly
    for filter_id in range(len(filter_list)):
        equation = re.sub(filter_list[filter_id], replace_list[filter_id], equation)
    return equation

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
    pen.left(90)
    pen.forward(tick_size)
    pen.left(180)
    pen.forward(tick_size*2)
    pen.penup()
    pen.left(180)
    pen.forward(tick_size)
    pen.setheading(0)

# Ends with pen up (as result of draw_tick())
def draw_tick_marks():
    global pen, scale_factor
    pen.penup()
    pen.goto(0, 0)
    #tick_set refers to the 4 tick group a specified number of units from the origin
    for tick_set in range(int(right_bound/scale_factor)):
        if 0 < tick_set <= 10:
            pen.penup()
            pen.goto(scale_factor*tick_set, 0)
            draw_tick()
            pen.goto(0, scale_factor*tick_set)
            pen.left(90)
            draw_tick()
            pen.goto(scale_factor*tick_set*-1, 0)
            draw_tick()
            pen.goto(0, scale_factor*tick_set*-1)
            pen.left(90)
            draw_tick()
        else:
            pen.penup()
            pen.goto(scale_factor*tick_set, 0)
            draw_tick()
            pen.goto(scale_factor*tick_set*-1, 0)
            draw_tick()


# Ends with pen up (as result of draw_tick_marks())
def setup_graph():
    pen.color(axis_color)
    draw_axis()
    draw_tick_marks()

def graph_rect_function(eq):
    global pen, scale_factor, graph_width
    x = left_bound
    x /= scale_factor
    y = eval(eq)
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
        if (y < 0 < pen.ycor()) or (pen.ycor() < 0 < y):
            pen.penup()
        pen.goto(x, y)
        pen.pendown()
        x += graph_width/resolution

def graph_parametric_function(xeq, yeq, t_min, t_max):
    global pen, scale_factor, x, y, graph_width
    t = t_min
    for t in range(resolution):
        x = eval(xeq)
        y = eval(yeq)
        pen.goto(x, y)
        t += (t_max - t_min) / resolution

def turtle_window_front():
    # Below 2 lines were written by cdlane on stackoverflow
    # https://stackoverflow.com/a/44787756
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

def start(eq_type, num_eqs):
    if eq_type == 'R' or eq_type == 'r':
        setup_graph()
        for equations in range(num_eqs):
            pen.color(graph_colors[equations - int((equations/len(graph_colors)*2))])
            input_equation = input('(in terms of x) y=')
            equation = regex_replace(input_equation)
            turtle_window_front()
            graph_rect_function(equation)
    elif eq_type == 'P' or eq_type == 'p':
        setup_graph()
        for equations in range(num_eqs):
            pen.color(graph_colors[equations - int((equations/len(graph_colors)*2))])
            x_input = input('(in terms of t) x=')
            x_equation = regex_replace(x_input)
            y_input = input('(in terms of t) y=')
            y_equation = regex_replace(y_input)
            print('What is your range (in terms of t)')
            t_minimum = int(input('Minimum Range: '))
            t_maximum = int(input('Maximum Range: '))
            turtle_window_front()
            graph_parametric_function(x_equation, y_equation, t_minimum, t_maximum)
    else:
        print('Please enter a valid input (R or P)')

### End function defining

### Set-Up Turtle Program
## Pen Set-Up
pen = trtl.Turtle()
pen.color(axis_color)
pen.speed(0)

## Window Set-Up
wn = trtl.Screen()
wn.setup(width=screen_width/2000, height=screen_height/1600)
wn.bgcolor(whiteboard_color)
# The next line was written by cdlane on stackoverflow
# https://stackoverflow.com/a/44787756
rootwindow = wn.getcanvas().winfo_toplevel()

### End turtle Set-Up

print('What type of equation would you like to graph? Rectangular (y=...) or Parametric (x=...; y=...)')
equation_type = input('R/P: ')
if equation_type == 'R' or equation_type == 'r':
    number_of_eqs = int(input('How many equations are you graphing: '))
    start(equation_type, number_of_eqs)
elif equation_type == 'P' or equation_type == 'p':
    number_of_eqs = 1
    start(equation_type, number_of_eqs)
else:
    print('Please enter a valid input (R or P)')

wn.mainloop()