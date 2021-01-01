""" Tests for day_9: the XMAS encryption problem """
import pytest

from read_input import *
from solution import *

@pytest.fixture
def codes():
    return list(read('test.txt'))

def test_read_input(codes):
    assert len(codes) == 20
    assert all(isinstance(rule, int) for rule in codes)

def test_find_sum_pair_and_is_valid(codes):
    for i, num in enumerate(codes[5:]):
        preamble = codes[i:i+5]
        if num == 127:
            assert find_sum_pair(num, preamble) == None
            assert is_valid(num, preamble) == False
            continue
        x, y = find_sum_pair(num, preamble)
        assert x in preamble and y in preamble
        assert is_valid(num, preamble)

def test_find_invalid_code(codes):
    assert find_invalid_code(codes, 5) == 127

def test_find_contiguous_components(codes):
    assert find_contiguous_components(codes, 127) == [15, 25, 47, 40]

    codes = [2, 3, 4, 1, 5]
    assert find_contiguous_components(codes, 8) == [3, 4, 1]
    codes = [5, 1, 2, 8, 4, 6, 3, 1]
    assert find_contiguous_components(codes, 13) == [4, 6, 3]

    codes = [45, 71, 73, 26, 41, 5, 54, 23, 35, 57, 22, 75, 21, 72, 77]
    assert find_contiguous_components(codes, sum([54,23,35])) == [54, 23, 35]
    assert find_contiguous_components(codes, sum([75,21,72])) == [75,21,72]

    codes = list(read('input.txt'))
    assert find_contiguous_components(codes, 23278925) == [865846, 920316, 975234, 934803, 1683508, 961814, 1072768, 1291799, 1108823, 1295819, 1461710, 1669021, 1467432, 1472332, 3145218, 1475958, 1476524]
