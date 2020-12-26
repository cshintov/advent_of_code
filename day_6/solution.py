""" Solution for day 6 """

from functools import reduce
from collections import Counter
from read_input import get_answers

def count(answers):
    return [Counter(answer) for answer in answers]

def count_unique(group):
    return len(reduce(set.union, 
        [set(individual) for individual in group]))

def count_everyone_said_yes(group):
    return len(reduce(set.intersection, 
        [set(individual) for individual in group]))

if __name__ == '__main__':
    solution_1 = sum([count_unique(group_answers) 
        for group_answers in get_answers('input.txt')])
    print(f'Part 1 solution: {solution_1}')

    solution_2 = sum([count_everyone_said_yes(group_answers) 
        for group_answers in get_answers('input.txt')])
    print(f'Part 2 solution: {solution_2}')
