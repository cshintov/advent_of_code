""" Day 2 part 1 """
from pprint import pprint

def process_inputs(inputs):
    lines = []
    for line in inputs:
        components = line.strip().split()
        minim, maxim = components[0].split('-')
        minim, maxim = int(minim), int(maxim)
        char = components[1][0]
        lines.append({
            'minimum': minim,
            'maximum': maxim,
            'character': char,
            'password': components[-1]
        })
    return lines


def is_valid(line):
    """ Checks whether the password is valid """
    count = line['password'].count(line['character'])
    if line['minimum'] <= count <= line['maximum']:
        return True
    return False
    

def count_valid_passwords(inputs, is_valid=is_valid):
    count = 0
    for inp in inputs:
        if is_valid(inp):
            count += 1
    return count

def test():
    with open('tests.txt') as inputs:
        tests = process_inputs(inputs)

    # pprint(tests)

    assert is_valid(tests[0]) == True, f'Case 1: {tests[0]} Expected Valid'
    assert is_valid(tests[1]) == False, f'Case 1: {tests[1]} Expected Invalid'
    assert is_valid(tests[2]) == True, f'Case 1: {tests[2]} Expected Valid'

if __name__ == '__main__':
    with open('input.txt') as inputs:
        passwords = process_inputs(inputs)
    print(count_valid_passwords(passwords))
