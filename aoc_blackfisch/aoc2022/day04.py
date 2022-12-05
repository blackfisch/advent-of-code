"""
AoC 2022 Day 4: Camp Cleanup
https://adventofcode.com/2022/day/4
"""

from aocd import data as input_data


def prepare_data(data: str) -> list:
    """Prepare the input data"""
    lines = [line.split(',') for line in data.splitlines()]

    def string_to_range(inp: str) -> range:
        """Convert String in format 'from-to' to range(from,to) (inclusive)."""
        start, end = inp.split('-')
        return set(range(int(start), int(end)+1))

    lines = [(string_to_range(range_a), string_to_range(range_b))
             for range_a, range_b in lines]

    return lines


### Solutions ###

def part_a(data: str):
    """Solution for part A"""
    ranges = prepare_data(data)

    def is_subset(elves: tuple) -> bool:
        """Check if ones elf's range is fully contained in the other."""
        elf_1, elf_2 = elves
        return elf_1.issubset(elf_2) or elf_2.issubset(elf_1)

    return sum(map(is_subset, ranges))


def part_b(data: str):
    """Solution for part B"""
    ranges = prepare_data(data)

    def overlaps(elves: tuple) -> bool:
        """Check if ones elf's range overlaps the other."""
        elf_1, elf_2 = elves
        return len(elf_1.intersection(elf_2)) > 0

    return sum(map(overlaps, ranges))


if __name__ == '__main__':
    print(f'Part A: {part_a(input_data)}')
    print(f'Part B: {part_b(input_data)}')
