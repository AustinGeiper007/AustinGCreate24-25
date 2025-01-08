import math as math
import turtle as trtl
import re
from lib2to3.pgen2.literals import evalString

equation = input("Enter equation: ")
filter = '/^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$/'

equation = re.findall(filter, equation)

print(equation)