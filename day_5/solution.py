""" Solve day 5 """
import re, math
from read_input import get_boarding_passes

ROWS, COLNS = 128, 8

def divide(start, end):
    diff = (end - start) + 1
    if (diff == 2):
        return (start, end)
    left = (start, int(start + (diff / 2)) - 1)
    right = (int(start + (diff / 2)), end)
    return left, right

def choose_half(endpoints, half):
    left, right = divide(*endpoints)
    return left if half in ('F', 'L') else right

def validate(bpass):
    try:
        assert len(bpass) == 10
        assert re.search(r'^[FB]{7}[LR]{3}', bpass)
        return True
    except AssertionError:
        return False

def find_seat_id(bpass):
    """ Return (row, coln, id) """
    assert validate(bpass), f"Invalid boarding pass: {bpass = }"

    def helper(ends, halfs):
        for half in halfs:
            ends = choose_half(ends, half)
        return ends

    row = helper((0, 127), bpass[:7])
    coln = helper((0, 7), bpass[7:])
    return (row, coln, row * 8 + coln)

def generate_bpasses(rows, colns):
    rs, cs = math.log2(rows), math.log2(colns)
    return []

def find_missing_seats(bpasses):
    seats = set(find_seat_id(p)[-1] for p in bpasses)
    return [s for s in range(1024) if not s in seats]

def find_your_seat(bpasses):
    """ Find the missing seat in the middle of the plane.
    Some of the seats in front and back of the plane is also missing.
    +1 and -1 of your seat will be there in the list."""
    middle = 512
    missing = find_missing_seats(bpasses)
    diffs = [(abs(middle - s), s) for s in missing]
    return sorted(diffs)[0][1]

if __name__ == '__main__':
    bpasses = set(get_boarding_passes('input.txt'))

    # Solution: Part 1
    print(f'Soution for part 1: {max(find_seat_id(p)[-1] for p in bpasses) = }')

    # Solution: Part 2
    # print(find_your_seat())
    print(f'Soution for part 2: {find_your_seat(bpasses) = }')
