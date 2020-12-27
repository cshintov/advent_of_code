""" Tests for $problem: the <> problem """
import pytest

from read_input import *
from solution import *

@pytest.fixture
def inputs():
    return list((line.strip() for line in open('test.txt')))

def test_read_input(inputs):
    assert len(inputs) == 9
    assert all(isinstance(rule, dict) for rule in inputs)

