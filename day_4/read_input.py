""" Read day 4's input """
from pprint import pprint
import itertools

from passport import Passport

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


def make_para(lines):
    para = []
    for line in lines:
        if not line:
            yield para
            para = []
        else:
            para.append(line)

def flatten(list_o_list_o_strings):
    return itertools.chain.from_iterable(list_o_list_o_strings)

def make_passports(input_file):
    paras = make_para(line.split() for line in open(input_file))
    flattened = (flatten(para) for para in paras)
    return (dict(item.split(':') for item in items)
            for items in flattened)

if __name__ == '__main__':
    for item in make_passports('test.txt'):
        print(item)
