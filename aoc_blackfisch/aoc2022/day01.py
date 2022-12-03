"""
AoC 2022 Day 1: Calorie Counting
https://adventofcode.com/2022/day/1
"""

from aocd import data as input_data


def get_elves_calories(data: str):
    """Return calories for an elf."""
    elves_calories = [sum(map(int, elf.splitlines()))
                      for elf in data.split('\n\n')]

    return elves_calories


### Solutions ###

def part_a(data: str):
    """Solution for part A"""
    return max(get_elves_calories(data))


def part_b(data: str):
    """Solution for part B"""
    elves_calories = get_elves_calories(data)
    elves_calories.sort(reverse=True)
    return sum(elves_calories[:3])


if __name__ == '__main__':
    print(f'Part A: {part_a(input_data)}')
    print(f'Part B: {part_b(input_data)}')
