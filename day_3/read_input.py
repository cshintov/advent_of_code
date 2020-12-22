""" Read day 3's input """
from pprint import pprint

def process(line):
    return line.strip()

def read(input_file, process=process):
    rows = []
    with open(input_file) as map_file:
        for line in map_file:
            rows.append(process(line))
    return rows

def test():
    loc_map = read('test.txt', process)
    return loc_map

if __name__ == '__main__':
    pprint(test())
