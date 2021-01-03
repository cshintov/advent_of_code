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


    for i in range(2, len(codes)):
        components = helper(i)
        if components:
            return components

    return components

def find_contiguous_components(codes, num):
    """ Find contiguous subarray which adds apt to num. """

    def watch1():
        print(f'{cur_sum=} : {i=} : {codes[i]=} : {start=} : {cur_sum > num = }')
    def watch2():
        print(f'\n{cur_sum=} : {codes[start]=};{cur_sum - codes[start] =} : {cur_sum > num = }')

    cur_sum = codes[0]
    start = end = 0
    for i in range(1, len(codes)):
        # watch1()
        if cur_sum == num:
            return codes[start : i]
        cur_sum = cur_sum + codes[i]
        if cur_sum > num:
            while cur_sum > num:
                # watch2()
                cur_sum -= codes[start]
                start += 1
    return []

if __name__ == '__main__':
    codes = list(read('test.txt'))
    codes = [45, 71, 73, 26, 41, 5, 54, 23, 35, 57, 22, 75, 21, 72, 77]
    assert find_contiguous_components(codes, sum([75,21,72])) == [75,21,72]

    # solution_1 = find_invalid_code(codes, 25)
    # print(f'Part 1 solution: {solution_1}')

    # solution_1 = 23278925
    # solution_2 = find_contiguous_components(codes, solution_1)
    # print(solution_2)
    # print(f'Part 2 solution: {min(solution_2) + max(solution_2)}')
