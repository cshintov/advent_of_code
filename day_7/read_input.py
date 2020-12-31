""" Read in luggage rules for bag colors """
import re

EMPTY_STRING = ''

def remove_all(xs, item=EMPTY_STRING):
    """ Removes all occurrences of an item from the given list.
    By default removes all empty strings."""
    return [x.strip() for x in xs if x != item]

def read(input_file):
    def split_n_clean(line):
        return [x.strip(', ') 
                for x in re.split('bags|bag', line.replace('contain', ''))
                if not 'no other' in x]

    lines = (line.strip('.\n') for line in open(input_file))
    components = (remove_all(split_n_clean(line), '') for line in lines)
    return components

def make_rules(components):
    return {
        component[0]: {
            comp[1]: int(comp[0])
            for comp in (
                remove_all(re.split('(\d+)', c)) for c in component[1:])
        }
        for component in components
    }

if __name__ == '__main__':
    print('Read input')
