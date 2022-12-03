"""
AoC 2022 Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2
"""

from aocd import data


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

    def __init__(self):
        pass

    def parse_data(self, data: str) -> list:
        """Parse data"""

        return [tuple(map(lambda el: self.RPS_VALUES.get(el, -1), game.split(" ")))
                for game in data.splitlines()]

    def winner_points(self, user_a: int, user_b: int) -> int:
        win_points = self.LOSE

        if user_a == user_b:
            win_points = self.DRAW
        elif user_a == self.ROCK and user_b == self.SCISSORS:
            pass
        elif (user_a == self.SCISSORS and user_b == self.ROCK) or user_a < user_b:
            win_points = self.WIN

        return (win_points + user_b)

    def solve_a(self, data: str) -> int:
        """RPS solver part A"""
        self.RPS_VALUES.update({
            "X": self.ROCK,
            "Y": self.PAPER,
            "Z": self.SCISSORS
        })

        self.data = self.parse_data(data)
        return sum(self.winner_points(*pair) for pair in self.data)

    def solve_b(self, data: str) -> int:
        """RPS solver part B"""
        self.RPS_VALUES.update({
            "X": self.LOSE,
            "Y": self.DRAW,
            "Z": self.WIN
        })
        self.data = self.parse_data(data)

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

        return sum([self.winner_points(*calc_move(*pair)) for pair in self.data])


### Solutions ###

def part_a(data: str):
    """Solution for part A"""
    return RPS().solve_a(data)


def part_b(data: str):
    """Solution for part B"""
    return RPS().solve_b(data)


if __name__ == '__main__':
    print(f'Part A: {part_a(data)}')
    print(f'Part B: {part_b(data)}')
