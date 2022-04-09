"""
take alist and filter number divisible by 5
input: [1, 20, 122, 344, 535, 23]
output;[20, 535]
"""
list1 = [1,20,30,33,22,54,55,45]
numbers = list(filter(lambda x: x%5 == 0, list1))
print(numbers)