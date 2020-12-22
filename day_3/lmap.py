""" Simulation of the location map.

A frame is simply a list of strings.

A location map is infinite repetition of the frame."""

from pprint import pformat
from read_input import test
from dataclasses import dataclass
from functools import wraps, reduce

class Board:
    def __init__(self, frame):
        self.current = frame

    def __str__(self):
        return pformat(self.current)

@dataclass
class Position:
    row: int
    col: int
    board: Board

    def __str__(self):
        return f"{self.row = }, {self.col = } val = {what_is_at(self)}"

def continue_if_end(movement):
    @wraps(movement)
    def inner(*args, **kwargs):
        pos = movement(*args, **kwargs)
        try:
            pos.board.current[pos.row][pos.col]
            return pos
        except IndexError as err:
            # print(f"Continue with the next frame!")
            pos.col = (pos.col + 1) % (len(pos.board.current[0]) + 1)
            return pos
    return inner

def quit_if_end(movement):
    @wraps(movement)
    def inner(*args, **kwargs):
        pos = movement(*args, **kwargs)
        try:
            if movement.__name__ in ['up', 'down']:
                pos.board.current[pos.row]
            else:
                pos.board.current[pos.row][pos.col]
            return pos
        except IndexError as err:
            # print(f"Can't move further {movement.__name__}! End of the world!")
            raise err
    return inner

@continue_if_end
def right(pos):
    pos.col += 1
    return pos

@quit_if_end
def down(pos):
    pos.row += 1
    return pos

def what_is_at(pos):
    return pos.board.current[pos.row][pos.col]

def move(move_in_dirn):
    def helper(pos):
        """ Move in the direction on the frame from pos. 
        Find next position. Try moving to the next position.
        Return new position or signal to Quit (False).
        """
        new_pos = move_in_dirn(pos)
        return new_pos
    return helper

def two_compose(f, g):
    """A higher order function that accepts two functions f, g
    and returns f(g(args))
    """
    def inner(*args):
        result = g(f(*args))
        return result
    return inner

move_right = move(right)
move_down = move(down)

def compose(*funcs):
    return reduce(two_compose, funcs)

def create_slope(r, d):
    return compose(* [move_down] * d + [move_right] * r)

if __name__ == '__main__':
    frame = Board(test())
    print(frame)
