""" Solution for day 4 """
import re
from read_input import make_passports

def is_valid_year(min, max):
    def inner(yr):
        return len(yr) == 4 and min <= int(yr) <= max
    return inner

is_valid_byr = is_valid_year(1920, 2002)
is_valid_iyr = is_valid_year(2010, 2020)
is_valid_eyr = is_valid_year(2020, 2030)

def is_valid_hgt(height):
    """ number <cm/in>. 
    cm: 150 <= number <= 193.
    in: 59 <= number <= 76."""
    try:
        hgt, unit = height[:-2], height[-2:]
        if unit == 'cm':
            return 150 <= int(hgt) <= 193
        if unit == 'in':
            return 59 <= int(hgt) <= 76
        return False
    except Exception as err:
        return False
    
def is_valid_hcl(hcolor):
    """ Starts with #. Total length 7. 
    Exactly 6 characters [0-9] or [a-f]"""
    try:
        assert hcolor.startswith('#')
        assert len(hcolor) == 7
        assert re.search('[0-9a-f]+', hcolor[1:]).span() == (0, 6)
        return True
    except AssertionError as err:
        return False

def is_valid_ecl(ecolor):
    """ One of amb blu brn gry grn hzl oth """
    return ecolor in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_valid_pid(pid):
    """ A 9 digit number including leading zeroes. """
    try:
        assert len(pid) == 9
        assert re.search('[0-9]*', pid).span() == (0, 9)
        return True
    except AssertionError as err:
        return False

def is_valid_par_1(passport):
    """ Part 1: checks whether the passport is valid. """
    for key in ['hgt', 'hcl', 'ecl', 'byr', 'iyr', 'eyr', 'pid']:
        if not key in passport:
            return False
    return True

def is_valid(passport):
    """ Checks whether the passport is valid. """
    def validate(check, prop): 
        try:
            return check(passport[prop])
        except KeyError as err:
            return False

    return all(map(lambda args: validate(*args),
            [(is_valid_byr, 'byr'), (is_valid_eyr, 'eyr'), (is_valid_iyr, 'iyr'), 
            (is_valid_ecl, 'ecl'), (is_valid_hcl, 'hcl'), 
            (is_valid_hgt, 'hgt'), (is_valid_pid, 'pid')]))

if __name__ == '__main__':
    passports = make_passports('input.txt')
    print(len(list(filter(is_valid, passports))))
