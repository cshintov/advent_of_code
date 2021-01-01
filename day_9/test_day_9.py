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
    assert find_contiguous_components(codes) == [15, 25, 47, 40]
