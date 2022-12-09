"""
AoC 2022 Day 7: No Space Left On Device
https://adventofcode.com/2022/day/7
"""

from aocd import data as input_data


### Solutions ###

def part_a(data: str):
    """Solution for part A"""
    lines = data.splitlines()

    directory_sizes = []
    total_size = 0

    for line in lines:
        split_line = line.split(' ')
        if '$ cd' in line:
            if '..' in line:
                last_dir_size = directory_sizes.pop()
                directory_sizes[-1] += last_dir_size
                if last_dir_size <= 100000:
                    total_size += last_dir_size
            else:
                directory_sizes.append(0)
        elif split_line[0].isdigit():
            file_size = int(split_line[0])
            directory_sizes[-1] += file_size
        # ignore 'ls' command and 'dir' output

    return total_size


def part_b(data: str):
    """Solution for part B"""


if __name__ == '__main__':
    print(f'Part A: {part_a(input_data)}')
    print(f'Part B: {part_b(input_data)}')
