""" Solutions for day_9: the XMAS encryption problem """
from read_input import read

def find_sum_pair(num, array):
    if not isinstance(array, set):
        array = set(array)
    for x in array:
        y = num - x
        if y in array:
            return x, y
    return None

def is_valid(num, preamble):
    return not find_sum_pair(num, preamble) is None

def find_invalid_code(codes, preamble_length):
    for i, num in enumerate(codes[preamble_length:]):
        preamble = codes[i:i+preamble_length]
        if not is_valid(num, preamble):
            return num
    return None

def find_contiguous_components(codes):
    return []

if __name__ == '__main__':
    codes = list(read('test.txt'))
    codes = list(read('input.txt'))

    solution_1 = find_invalid_code(codes, 25)
    print(f'Part 1 solution: {solution_1}')

    solution_2 = ''
    print(f'Part 2 solution: {solution_2}')
