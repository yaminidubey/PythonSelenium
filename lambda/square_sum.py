"""
take a list of number and return sum of squares of their number
input:[1,2,3,4]
ouput: 30
"""
from functools import reduce

list1 = [2, 2, 3]
square = list(map(lambda x: x*x, list1))
sum_number = reduce(lambda x,y: x+y, square)

print(sum_number)