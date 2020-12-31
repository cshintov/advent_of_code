""" Tests for day 7: the luggage problem """
import pytest

from read_input import *
from solution import *

@pytest.fixture
def rules():
    return make_rules(read('test.txt'))

def test_read_input(rules):
    assert len(rules) == 9
    assert all(isinstance(rule, dict) and isinstance(bag, str)
            for bag, rule in rules.items())

def test_count_outerbags(rules):
    assert count_bags_that_can_contain('shiny gold', rules) == 4

def test_count_innerbags(rules):
    assert count_inner_bags('shiny gold', rules) == 32

def test_count_innerbags_deep_nesting():
    rules = make_rules(read('part2_test.txt'))
    assert count_inner_bags('shiny gold', rules) == 126
