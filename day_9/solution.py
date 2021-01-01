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

def find_contiguous_components_brute_force(codes, num):
    def helper(n):
        for i, _ in enumerate(codes):
            if sum(codes[i:i+n]) == num:
                return codes[i:i+n]
        return []

    for i in range(2, len(codes)):
        components = helper(i)
        if components:
            return components

    return components

def find_contiguous_components(codes, num):
    def look_back(i):
        cur_sum = 0
        for j in range(i, 0, -1):
            cur_sum += codes[j]
            if cur_sum == num:
                return j
        return None

    for i, code in enumerate(codes):
        start = look_back(i)
        if not start is None:
            return codes[start:i+1]
    return []
        

if __name__ == '__main__':
    codes = list(read('input.txt'))

    solution_1 = find_invalid_code(codes, 25)
    print(f'Part 1 solution: {solution_1}')

    solution_2 = find_contiguous_components(codes, solution_1)
    print(solution_2)
    print(f'Part 2 solution: {min(solution_2) + max(solution_2)}')
