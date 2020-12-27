""" Tests for day 7: the luggage problem """
import pytest

from read_input import *
from solution import *

@pytest.fixture
def rules():
    return list((line.strip() for line in open('test.txt')))

def test_read_input(rules):
    assert len(rules) == 9
    assert all(isinstance(rule, dict) for rule in rules)

