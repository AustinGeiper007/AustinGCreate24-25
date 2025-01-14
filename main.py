# Import statements cus I need those
import math as m
import turtle as trtl
import re
from lib2to3.pgen2.literals import evalString

filter_list = [r'(sine|sin)\(?', r'(cosine|cos)\(?', r'(tangent|tan)\(?', r'e\^\(?']
replace_list = ['m.sin(', 'm.cos(', 'm.tan(', 'm.exp(']

global input
input = input('Input equation: ')

def re_replace():
    global input
    for filt in range(len(filter_list)):
        input = re.sub(filter_list[filt], replace_list[filt], input)

re_replace()

for num in range (-500, 500):
   x = num
   y = eval(input)
   print(x, y)


'''
result = eval(input)
print(result)
'''