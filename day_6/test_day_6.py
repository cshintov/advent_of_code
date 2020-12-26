""" Tests for day 6 """
import pytest
from solution import *
from read_input import *

@pytest.fixture
def test_answers():
    return list(get_answers('test.txt'))

def test_read_input(test_answers):
    assert len(test_answers) == 5
    assert all([isinstance(a, list) for a in test_answers])

def test_count():
    assert count(['ab', 'ac']) == [{'a': 1, 'b': 1}, {'a': 1, 'c': 1}]
    assert count(['a', 'a']) == [{'a': 1}, {'a': 1}]
    assert count(['a', 'b', 'c']) == [{'a': 1}, {'b': 1}, {'c': 1}]
    assert count(['abc']) == [{'a': 1, 'b': 1, 'c': 1}]

def test_count_unique_answers():
    assert count_unique(['ab', 'ac']) == 3
    assert count_unique(['a', 'a']) == 1
    assert count_unique(['a', 'b', 'c']) == 3
    assert count_unique(['abc']) == 3

def test_count_unique_answers_in_test():
    assert sum([count_unique(group_answers) 
        for group_answers in get_answers('test.txt')]) == 11

def test_count_everyone_said_yes():
    assert sum([count_everyone_said_yes(group_answers) 
        for group_answers in get_answers('test.txt')]) == 6
