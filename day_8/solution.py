""" Solutions for day_8: the game console problem """
from read_input import *

class InfiniteLoop(Exception):
    pass

def make_run():
    accumulator = 0
    instruction_ptr = 0
    stack = []

    def run(instructions):
        nonlocal accumulator, instruction_ptr

        try:
            while True:
                instr = instructions[instruction_ptr]
                stack.append((instruction_ptr, instr))
                execute(instr)
                if instruction_ptr == len(instructions):
                    return accumulator, None, stack
        except InfiniteLoop as err:
            return accumulator, instruction_ptr, stack
        except IndexError as err:
            print('Error: Trying to execute nonexisting instruction!')
            return _, 'Error', _

    def execute(instr):
        nonlocal accumulator, instruction_ptr

        if instr.done:
            raise InfiniteLoop(instr)

        if instr.op == 'acc':
            accumulator += instr.arg
            instr.done = True
            instruction_ptr += 1
        elif instr.op == 'jmp':
            instruction_ptr += instr.arg
            instr.done = True
        elif instr.op == 'nop':
            instr.done = True
            instruction_ptr += 1
            pass
        else:
            raise Exception('Unknown Operation!')

    return run

def try_fix(instrns, stack):
    new = [Instruction(ins.op, ins.arg) for ins in instrns]
    while len(stack) != 0:
        ip, instr = stack.pop()
        if instr.op == 'nop':
            new[ip] = Instruction('jmp', instr.arg)
            break
        elif instr.op == 'jmp':
            new[ip] = Instruction('nop', instr.arg)
            break
    return new

def fix_code(instructions):
    run = make_run()
    result, ip, stack = run(instructions)

    while True:
        if ip == 'Error':
            break

        if ip is None: # means program terminated
            return result
        else:
            new_instrns = try_fix(instructions, stack)
            run = make_run()
            result, ip, _ = run(new_instrns)

    return 'No fix!'

if __name__ == '__main__':
    code = read_code('input.txt')
    run = make_run()
    solution_1, _, _ = run(list(code))
    print(f'Part 1 solution: {solution_1 = }')

    solution_2 = fix_code(list(code))
    print(f'Part 2 solution: {solution_2}')
