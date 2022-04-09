"""
Find half of each number using map
input: [2,16,32,86]
output: [1,8,16,43]
"""
list1 = [2,16,32,86,102]
half_number = list(map(lambda x: int(x/2),list1))
print(half_number)