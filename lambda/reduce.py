from functools import reduce

list1 = [1,2,3,4,5,6,7,8,9,10]
sum_of_number = reduce(lambda x, y: x+y, list1)

print(sum_of_number)