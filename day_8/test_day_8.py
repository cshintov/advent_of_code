""" Tests for day_8: the game console problem """
import pytest

from read_input import *
from solution import *

@pytest.fixture
def instructions():
    return list(read_code('test.txt'))

def test_read_input(instructions):
    assert len(instructions) == 9
    assert all([isinstance(instr, Instruction) for instr in instructions])

def test_run(instructions):
    run = make_run()
    assert run(instructions)[0] == 5

def test_fix_code(instructions):
    assert fix_code(instructions) == 8
