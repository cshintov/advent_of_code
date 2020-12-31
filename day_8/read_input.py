""" Read in the boot code of the console """
from dataclasses import dataclass

@dataclass
class Instruction:
    op: str
    arg: int
    done: bool = False

def read_code(code_file):
    lines = (line.strip() for line in open(code_file))
    splits = (line.split() for line in lines)
    instructions = (
                Instruction(split[0], int(split[1])) 
                for split in splits
            )
    return instructions

if __name__ == '__main__':
    print('Read input')
