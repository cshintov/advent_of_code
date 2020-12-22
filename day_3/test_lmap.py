from lmap import *
from operator import mul
from solution import count_item

loc_map = Board(test())

output = reduce(mul, [  
    count_item(loc_map, slope, '#') 
    for slope in map(create_slope, 
        *zip(*[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
])

# print(f"{count_item(loc_map, slope, '#') = }")
print(f"{output: = }")

