import math as math
import turtle as trtl
import re

input = input('Input equation: ')
filter = 'sin\('

equation = re.sub(filter, 'math.sin(', input)


print(equation)