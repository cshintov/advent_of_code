""" Solutions for day 7: the luggage problem """
from read_input import make_rules, read

def count_bags_that_can_contain(bag, rules, outer_bags={}):
    """ Count bags that contain the given bag color. """
    if bag in outer_bags:
        outer_bags[bag] = 1 # Mark as visited

    # search for bags that can contain <bag>
    for outer_bag, inner_bags in rules.items():
        if bag in inner_bags:
            outer_bags.setdefault(outer_bag, 0)

    # for each of those bags search for bags that can contain them
    for outer in list(outer_bags):
        if outer_bags[outer] != 1:
            count_bags_that_can_contain(outer, rules, outer_bags) 

    # count the unique bags identified thus far
    return len(outer_bags)

def count_inner_bags(bag, rules):
    return sum(
        count + count * count_inner_bags(inner, rules)
        for inner, count in rules[bag].items()
    )

if __name__ == '__main__':
    rules = make_rules(read('input.txt'))

    solution_1 = count_bags_that_can_contain('shiny gold', rules)
    print(f'Part 1 solution: {solution_1}')

    solution_2 = count_inner_bags('shiny gold', rules)
    print(f'Part 2 solution: {solution_2}')
