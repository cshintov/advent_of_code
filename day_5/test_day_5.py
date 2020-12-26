""" Tests for day 5 """
import re
import pytest
from solution import *
from read_input import *

@pytest.fixture
def boarding_passes_test():
    return list(get_boarding_passes('test.txt'))

@pytest.fixture
def boarding_passes():
    return list(get_boarding_passes('input.txt'))

def test_read_input(boarding_passes_test):
    """ assert that the test data has 4 passports """
    assert len(list(boarding_passes_test)) == 4
    assert all([isinstance(p, str) for p in boarding_passes_test])
    for p in boarding_passes_test:
        assert validate(p)

def test_divide():
    """ Test finding half of a range """
    assert divide(44, 45) == (44, 45)
    assert divide(0, 127) == ((0, 63), (64, 127))
    assert divide(0, 63) == ((0, 31), (32, 63))
    assert divide(64, 127) == ((64, 95), (96, 127))
    assert divide(40, 47) == ((40, 43), (44, 47))
    assert divide(44, 47) == ((44, 45), (46, 47))

def test_choose_half():
    """ Test choosing half of a range """
    assert choose_half((44, 45), 'F') == 44
    assert choose_half((0, 127), 'F') == (0, 63)
    assert choose_half((0, 127), 'B') == (64, 127)
    assert choose_half((0, 7), 'R') == (4, 7)
    assert choose_half((0, 7), 'L') == (0, 3)
    assert choose_half((4, 7), 'L') == (4, 5)
    assert choose_half((4, 5), 'R') == 5

def test_find_seat_id(boarding_passes_test):
    assert find_seat_id(boarding_passes_test[0]) == (44, 5, 357)
    assert find_seat_id(boarding_passes_test[1]) == (70, 7, 567)
    assert find_seat_id(boarding_passes_test[2]) == (14, 7, 119)
    assert find_seat_id(boarding_passes_test[3]) == (102, 4, 820)

def test_validate():
    assert validate('FFFBBBFRRR') == True
    assert validate('FFFBBBFRRX') == False
    assert validate('RFFBBBFRRR') == False
    assert validate('LFFBBBFRRR') == False
    assert validate('') == False

def test_find_missing_seats(boarding_passes):
    assert len(find_missing_seats(boarding_passes)) == 140
