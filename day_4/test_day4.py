from read_input import *
import pytest
from solution import *

@pytest.fixture
def test_passports():
    return list(make_passports('test.txt'))

def test_read_input(test_passports):
    """ assert that the test data has 4 passports """
    assert len(list(test_passports)) == 4
    assert all([isinstance(p, dict) for p in test_passports])

def test_is_valid_byr():
    """ Four digits. 1920 < yr < 2002 """
    assert is_valid_byr('2002') == True
    assert is_valid_byr('2003') == False

def test_is_valid_eyr():
    """ Four digits. 2020 < yr < 2030 """
    assert is_valid_eyr('2022') == True
    assert is_valid_eyr('2033') == False

def test_is_valid_iyr():
    """ Four digits. 2020 < yr < 2030 """
    assert is_valid_iyr('2012') == True
    assert is_valid_iyr('2023') == False

def test_is_valid_height():
    """ number <cm/in>. 
    cm: 150 <= number <= 193.
    in: 59 <= number <= 76."""
    assert is_valid_hgt('60in') == True
    assert is_valid_hgt('190cm') == True
    assert is_valid_hgt('190in') == False
    assert is_valid_hgt('190') == False
    assert is_valid_hgt('190adf') == False
    assert is_valid_hgt('190icm') == False

def test_is_valid_hcl():
    assert is_valid_hcl('#123abc') == True
    assert is_valid_hcl('#123abz') == False
    assert is_valid_hcl('123abc') == False
    assert is_valid_hcl('#623a2f') == True

def test_is_valid_ecl():
    assert is_valid_ecl('brn') == True
    assert is_valid_ecl('wat') == False

def test_is_valid_pid():
    assert is_valid_pid('000000001') == True
    assert is_valid_pid('00000001c') == False
    assert is_valid_pid('0123456789') == False
    assert is_valid_pid('01234567899') == False

def test_valid_passports_part_1(test_passports):
    """ test test.txt inputs. 
    Expected valid, invalid, valid, invalid """
    assert ([is_valid_par_1(passport) for passport in test_passports] ==
            [True, False, True, False])

# @pytest.mark.skip
def test_valid_passports():
    """ test valid.txt inputs. 
    Expected All valid"""
    test_passports = make_passports('valid.txt')
    assert all([is_valid(passport) for passport in test_passports])

# @pytest.mark.skip
def test_invalid_passports():
    """ test invalid.txt inputs. 
    Expected all invalid"""
    test_passports = make_passports('invalid.txt')
    assert not all([is_valid(passport) for passport in test_passports])

# test_valid_passports()
