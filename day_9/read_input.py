""" Read in XMAS encryption numbers"""

def read(code_file):
    return (int(line.strip()) for line in open(code_file))

if __name__ == '__main__':
    print('Read input')
