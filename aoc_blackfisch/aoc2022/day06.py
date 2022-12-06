"""
AoC 2022 Day 6: Tuning Trouble
https://adventofcode.com/2022/day/6
"""

from collections import Counter
from aocd import data as input_data


def detect_start(data: str, start_marker_length: int) -> int:
    """
    Detect the character count until a start marker ended.
    Start markers have no duplicate characters in them.
    """
    for i in range(start_marker_length, len(data) + 1):
        dupes = [char for char, count in Counter(
            data[i-start_marker_length:i]).items() if count > 1]

        if len(dupes) == 0:
            return i

    return -1  # probably an error?


### Solutions ###

def part_a(data: str):
    """Solution for part A"""
    return detect_start(data, 4)


def part_b(data: str):
    """Solution for part B"""
    return detect_start(data, 14)


if __name__ == '__main__':
    print(f'Part A: {part_a(input_data)}')
    print(f'Part B: {part_b(input_data)}')
