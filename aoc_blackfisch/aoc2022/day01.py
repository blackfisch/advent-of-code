"""
AoC 2022 Day 1: Calorie Counting
https://adventofcode.com/2022/day/1
"""

from aocd import data


def get_elves_calories(data):
    elves_calories = [[int(cal) for cal in elf.splitlines()]
                      for elf in data.split('\n\n')]
    elves_calories = [sum(cal_list) for cal_list in elves_calories]

    return elves_calories


### Solutions ###

def part_a(data):
    """Solution for part A"""
    return max(get_elves_calories(data))


def part_b(data):
    """Solution for part B"""
    elves_calories = get_elves_calories(data)
    elves_calories.sort(reverse=True)
    return sum(elves_calories[:3])


if __name__ == '__main__':
    print(f'Part A: {part_a(data)}')
    print(f'Part B: {part_b(data)}')
