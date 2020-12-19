""" Day 2 part 1 """
from pprint import pprint

from part_1 import count_valid_passwords

def process_inputs(inputs):
    lines = []
    for line in inputs:
        components = line.strip().split()
        positions = list(map(int, components[0].split('-')))
        char = components[1][0]
        lines.append({
            'positions': positions,
            'character': char,
            'password': components[-1]
        })
    return lines


def exclusive_or(a, b):
    """ Return True only when a and b are different booleans. """
    return (a and not b) or (b and not a)

def is_valid(password):
    """ Checks whether the password is valid.
    Password is valid if exactly one of the two positions
    has the given character."""
    is_at_pos_one, is_at_pos_two = map(
            lambda pos: password['character'] == password['password'][pos-1],
            password['positions'])
    return exclusive_or(is_at_pos_one, is_at_pos_two)

def test():
    with open('tests.txt') as inputs:
        tests = process_inputs(inputs)

    assert is_valid(tests[0]) == True, f'Case 1: {tests[0]} Expected Valid'
    assert is_valid(tests[1]) == False, f'Case 1: {tests[1]} Expected Invalid'
    assert is_valid(tests[2]) == False, f'Case 1: {tests[2]} Expected Invalid'

if __name__ == '__main__':
    with open('input.txt') as inputs:
        passwords = process_inputs(inputs)
    print(count_valid_passwords(passwords, is_valid))
    # test()
