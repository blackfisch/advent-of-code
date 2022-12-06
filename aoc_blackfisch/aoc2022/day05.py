"""
AoC 2022 Day 5: Supply Stacks
https://adventofcode.com/2022/day/5
"""

from re import match
from pprint import pprint
from aocd import data as input_data

END_STACKS = 8
NUMBER_OF_STACKS = 9
START_MOVES = 10


def prepare_data(data: str, **kwargs) -> list:
    """Prepare the input data"""
    lines = data.splitlines()

    # prepare stacks
    stacks = []
    for idx in range(0, NUMBER_OF_STACKS):
        stacks.append([])

    for line in lines[:END_STACKS]:
        for stack_no, idx in enumerate(range(1, 35, 4)):
            char = line[idx]
            if not char.isspace():
                stacks[stack_no].append(char)

    for stack in stacks:
        stack.reverse()

    if kwargs.get('debug'):
        pprint(stacks)

    # prepare moves
    moves = []
    for line in lines[START_MOVES:]:
        amt, move_b, move_c = match(
            r'move (\d+) from (\d) to (\d)', line).groups()
        cur_moves = (int(amt), int(move_b)-1, int(move_c)-1)
        moves.append(tuple(cur_moves))

    return stacks, moves


### Solutions ###

def part_a(data: str, **kwargs):
    """Solution for part A"""
    stacks, moves = prepare_data(data, **kwargs)

    for amt, start, dest in moves:
        for _ in range(0, amt):
            stacks[dest].append(stacks[start].pop())

    result = [str(stack.pop()) for stack in stacks]
    return ''.join(result)


def part_b(data: str, **kwargs):
    """Solution for part B"""
    stacks, moves = prepare_data(data, **kwargs)

    for amt, start, dest in moves:
        tmp = []
        for _ in range(0, amt):
            tmp.append(stacks[start].pop())

        for _ in range(0, len(tmp)):
            stacks[dest].append(tmp.pop())

    result = [str(stack.pop()) for stack in stacks]
    return ''.join(result)


if __name__ == '__main__':
    print(f'Part A: {part_a(input_data)}')
    print(f'Part B: {part_b(input_data)}')
