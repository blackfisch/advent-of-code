"""
AoC 2022 Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2
"""

from aocd import data as input_data


class RPS:
    """Rock Paper Scissors class"""
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    WIN = 6
    DRAW = 3
    LOSE = 0

    RPS_VALUES = {
        "A": ROCK,
        "B": PAPER,
        "C": SCISSORS
    }

    def __init__(self, data: str, xyz_values: dict):
        self.RPS_VALUES.update(xyz_values)
        self.data = self.parse_data(data)

    def parse_data(self, data: str) -> list:
        """Parse input data"""
        return [tuple(map(lambda el: self.RPS_VALUES.get(el, -1), game.split(" ")))
                for game in data.splitlines()]

    def player_points(self, user_a: int, user_b: int) -> int:
        """Calculate the points for the player (user_b)."""
        win_points = self.LOSE

        if user_a == user_b:
            win_points = self.DRAW
        elif user_a == self.ROCK and user_b == self.SCISSORS:
            pass
        elif (user_a == self.SCISSORS and user_b == self.ROCK) or user_a < user_b:
            win_points = self.WIN

        return win_points + user_b

    def solve_a(self) -> int:
        """RPS solver part A"""

        return sum(self.player_points(*pair) for pair in self.data)

    def solve_b(self) -> int:
        """RPS solver part B"""

        def calc_move(user_a: int, goal: int) -> int:
            ret = 0
            if goal == self.LOSE:
                ret = user_a - 1
            elif goal == self.DRAW:
                ret = user_a
            elif goal == self.WIN:
                ret = user_a + 1

            if ret <= 0:
                ret = self.RPS_VALUES["C"]
            elif ret > self.RPS_VALUES["C"]:
                ret = self.RPS_VALUES["A"]

            return user_a, ret

        points = [self.player_points(*calc_move(*pair)) for pair in self.data]
        return sum(points)


### Solutions ###

def part_a(data: str):
    """Solution for part A"""
    return RPS(data, {"X": RPS.ROCK, "Y": RPS.PAPER, "Z": RPS.SCISSORS}).solve_a()


def part_b(data: str):
    """Solution for part B"""
    return RPS(data, {"X": RPS.LOSE, "Y": RPS.DRAW, "Z": RPS.WIN}).solve_b()


if __name__ == '__main__':
    print(f'Part A: {part_a(input_data)}')
    print(f'Part B: {part_b(input_data)}')
