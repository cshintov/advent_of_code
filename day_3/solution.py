from read_input import read
from lmap import *
from operator import mul

def traverse(terra, slope):
    current_pos = Position(0, 0, terra)
    while current_pos:
        try:
            current_pos = slope(current_pos)
            yield what_is_at(current_pos)
        except IndexError as err:
            return

def count_item(terra, slope, item='#'):
    return len(list(filter(
        lambda x: x == item,
        traverse(terra, slope)
    )))

loc_map = Board(read('input.txt'))

output = reduce(mul, [  
    count_item(loc_map, slope, '#') 
    for slope in map(create_slope, 
        *zip(*[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
])

if __name__ == '__main__':
    # print(f"{count_item(loc_map, slope, '#') = }")
    print(f"{output: = }")
