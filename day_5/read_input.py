""" Read input: boarding_passes """

def get_boarding_passes(input_file):
    return (line.strip() for line in open(input_file))
