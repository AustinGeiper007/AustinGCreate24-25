### Import statements cus I need those
import math as m
import turtle as trtl
import re
### Imports End

### Set-Up Turtle Program
## Pen Set-Up
pen = trtl.Turtle()
pen.color('white')
## Window Set-Up
wn = trtl.Screen()
wn.bgcolor('black')
### End turtle Set-Up

### Lists for filter
filter_list = [r'(sine|sin)\(?', r'(cosine|cos)\(?', r'(tangent|tan)\(?', r'e\^\(?']
replace_list = ['m.sin(', 'm.cos(', 'm.tan(', 'm.exp(']
### End Lists

### Globaling variables
global input, x, y
### End global

### Defining functions
# Regex to replace text
def re_replace():
    global input
    # Run thru list of filters and replaces them accordingly
    for id in range(len(filter_list)):
        input = re.sub(filter_list[id], replace_list[id], input)

def draw_axis():
    global pen, wn
    pen.penup()
    pen.goto(0, -400)
    pen.pendown()
    pen.goto(0, 400)
    pen.penup()
    pen.goto(-500, 0)
    pen.pendown()
    pen.goto(500, 0)
### End function defining


# Ask for input equations
input = input('Input equation: ')

re_replace()

wn.mainloop()